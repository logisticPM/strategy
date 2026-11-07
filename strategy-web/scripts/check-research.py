"""Check snapshot consistency and economic scenario equivalence."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/research.json').read_text(encoding='utf-8'))
source=root.parent/'strategy-agent'
for name,expected in data['sourceHashes'].items():
    assert hashlib.sha256((source/name).read_bytes()).hexdigest()==expected, f'Stale source: {name}'
    assert (source/name).read_text(encoding='utf-8-sig')==data['docs'][name], f'Altered content: {name}'
ids={e['id'] for e in data['evidence']}|{h[0] for h in data['hypotheses']}
for entry in data['evidence']:
    assert set(re.findall(r'\b[EH]\d{3}\b',entry['body']))<=ids, entry['id']
for row in data['financial']['assumed_sensitivity_matrix']:
    actual=7847.044*row['assumed_recovery_fraction']*row['assumed_incremental_contribution_margin']-row['assumed_fixed_cost']
    assert abs(actual-row['incremental_contribution_after_fixed_cost'])<.00051
assert 'reddit-review-R004.md' in next(e['body'] for e in data['evidence'] if e['id']=='E027')
assert 'x-verification-R005.md' in next(e['body'] for e in data['evidence'] if e['id']=='E033')
assert data['researchVersion']=='R013'
assert hashlib.sha256((source/'sources/audit-R013.json').read_bytes()).hexdigest()==data['auditHash']
assert len(data['audit']['evidence'])==45
assert len(data['audit']['hypotheses'])==14
assert data['audit']['hypotheses']['H012']['action']=='降级'
assert '已有实际减购自述' in next(h[2] for h in data['hypotheses'] if h[0]=='H002')
assert len([e for e in data['evidence'] if e['audit']['action']=='未纳入'])==0
print(json.dumps({'passed':True,'source_hashes':len(data['sourceHashes']),'evidence':len(data['evidence']),'hypotheses':len(data['hypotheses']),'scenario_cells':9,'scope':'Snapshot/source equivalence and arithmetic, not factual validation'}))
