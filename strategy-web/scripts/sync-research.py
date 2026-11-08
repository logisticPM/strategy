"""Build a read-only research snapshot from the canonical strategy-agent files."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

SITE = Path(__file__).resolve().parents[1]
SOURCE = SITE.parent / 'strategy-agent'

def table(text, prefix=None):
    rows = []
    for line in text.splitlines():
        if not line.startswith('| '):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if prefix is None or re.match(prefix, cells[0]):
            rows.append(cells)
    return rows

def build():
    audit=json.loads((SOURCE/'sources/audit-R021.json').read_text(encoding='utf-8'))
    names = ['dashboard.md', 'enterprise-diagnosis.md', 'strategy-options.md', 'economics.md',
             'evidence-ledger.md', 'hypotheses.md', 'research-plan.md',
             'decisions/D001-north-america.md', 'decisions/D002-enterprise-strategy.md']
    names += [p.relative_to(SOURCE).as_posix() for p in sorted((SOURCE/'sources').glob('*.md'))]
    docs = {name: (SOURCE/name).read_text(encoding='utf-8-sig') for name in names}
    ledger = docs['evidence-ledger.md']
    entries = []
    for match in re.finditer(r'^### (E\d{3})\s+([^\n]+)\n([\s\S]*?)(?=^#{1,3} |\Z)', ledger, re.M):
        eid, title, body = match.groups()
        status_line = next((x for x in body.splitlines() if '状态' in x), '')
        status = '部分核查' if '部分核查' in status_line else '已核查' if '已核查' in status_line else '待复核'
        preceding = ledger[:match.start()]
        group_start = preceding.rfind('\n## ')
        context = preceding[group_start:].split('\n### ')[0]
        if '](' in context:
            body += '\n\n### 本组来源与阅读边界\n\n' + '\n'.join(context.strip().splitlines()[1:])
        entries.append(dict(id=eid, title=title.lstrip('— ').strip(), body=body.strip(), status=status))
    for row in table(ledger, r'E\d{3}$'):
        entries.append(dict(id=row[0], title=re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1',row[1]), body=row[1]+'\n\n'+row[2], status='待复核'))
    entries.sort(key=lambda x:x['id'])
    for entry in entries:
        entry['audit']=audit['evidence'].get(entry['id'],dict(action='未纳入',review='本轮未复核',reason='保持原记录，不提升为本轮审计结论。',family='见原记录',period='见原记录'))
    assert len(entries)==56 and len(set(x['id'] for x in entries))==56
    hypotheses=table(docs['hypotheses.md'],r'H\d{3}$')
    assert len(hypotheses)==14
    updates={}
    heading=''
    for line in docs['hypotheses.md'].splitlines():
        if line.startswith('## '):
            heading=line[3:]
        if line.startswith('|') or line.startswith('#'):
            continue
        for hid in set(re.findall(r'\bH\d{3}\b', line)):
            if 'R00' in heading:
                updates.setdefault(hid, []).append('### '+heading+'\n\n'+line)
    result=dict(updated='2026-11-07', caseCutoff='2026-10-08', researchVersion='R021',
                audit=audit, auditHash=hashlib.sha256((SOURCE/'sources/audit-R021.json').read_bytes()).hexdigest(),
                hypothesisUpdates=updates,
                generated=datetime.now(ZoneInfo('America/Vancouver')).isoformat(),
                docs=docs, evidence=entries, hypotheses=hypotheses,
                options=table(docs['strategy-options.md'],r'P[1-4] '),
                decisions=table(docs['decisions/D002-enterprise-strategy.md'],r'P[1-4]'),
                queue=table(docs['research-plan.md'],r'[1-5]$'),
                signals=table(docs['dashboard.md'],r'规模$|地理$|利润$|顾客$|新方向$'),
                lenses=table(docs['dashboard.md'],r'Brand$|Geography$|Categories$|Competition$|Value$'),
                financial=json.loads((SOURCE/'models/enterprise-economics-results.json').read_text()),
                sourceHashes={name:hashlib.sha256((SOURCE/name).read_bytes()).hexdigest() for name in names})
    target=SITE/'data/research.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(evidence=len(entries),hypotheses=len(hypotheses),documents=len(docs),output=str(target))))

if __name__=='__main__':
    build()
