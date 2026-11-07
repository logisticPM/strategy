"""Validate local research references and source versions; no network/model calls."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent


def main():
    errors = []
    required = [
        'README.md', 'AGENTS.md', 'dashboard.md', 'evidence-ledger.md',
        'hypotheses.md', 'decisions/D001-north-america.md',
        'runs/R001-north-america.md', 'research-plan.md', 'run-prompt.md',
        'sources/manifest.json',
        'enterprise-diagnosis.md', 'strategy-options.md', 'economics.md',
        'decisions/D002-enterprise-strategy.md',
        'models/enterprise_economics.py', 'models/enterprise-economics-results.json',
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append(f'Missing {rel}')
    docs = {p: p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md')}
    evidence_text = docs.get(ROOT / 'evidence-ledger.md', '')
    hypothesis_text = docs.get(ROOT / 'hypotheses.md', '')
    evidence = [a or b for a, b in re.findall(
        r'^### (E\d{3})\b|^\| (E\d{3}) \|', evidence_text, re.M)]
    hypotheses = re.findall(r'^\| (H\d{3})\b', hypothesis_text, re.M)
    known = set(evidence + hypotheses)
    for group, ids in [('evidence', evidence), ('hypotheses', hypotheses)]:
        if len(ids) != len(set(ids)):
            errors.append(f'Duplicate {group} IDs')
        if not ids:
            errors.append(f'No {group} definitions')
    links_checked = 0
    for path, body in docs.items():
        for token in set(re.findall(r'\b[EH]\d{3}\b', body)):
            if token not in known:
                errors.append(f'{path.relative_to(ROOT)}: undefined {token}')
        for href in re.findall(r'\]\(([^)]+)\)', body):
            if re.match(r'^[a-z]+://', href) or href.startswith('#'):
                continue
            target = unquote(href.split('#')[0].strip('<>'))
            if not (path.parent / target).exists():
                errors.append(f'{path.relative_to(ROOT)}: missing link {target}')
            links_checked += 1
    manifest_path = ROOT / 'sources/manifest.json'
    source_count = 0
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for item in manifest['sources']:
            source = ROOT.parent / item['path']
            if not source.is_file():
                errors.append(f'Missing source {source.name}')
                continue
            if hashlib.sha256(source.read_bytes()).hexdigest() != item['sha256']:
                errors.append(f'Source changed; review before refreshing manifest: {source.name}')
            if item.get('extraction') and not (ROOT / item['extraction']).is_file():
                errors.append(f'Missing extraction {item["extraction"]}')
            source_count += 1
    report = {
        'passed': not errors,
        'scope': 'Local file integrity and references only; not factual or strategic validation',
        'markdown_files': len(docs), 'evidence_entries': len(evidence),
        'hypotheses': len(hypotheses), 'local_links_checked': links_checked,
        'source_hashes_checked': source_count, 'errors': errors,
    }
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
