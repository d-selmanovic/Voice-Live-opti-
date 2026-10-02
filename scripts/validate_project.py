"""Offline integrity checks; these do not test voice runtime behavior."""
from pathlib import Path
import json
import re
import sys
import tomllib

root = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok:
        errors.append(message)

def read(path):
    return json.loads((root / path).read_text())

req = read('docs/audit/requirements.json')
sources = read('docs/references/sources.json')
if isinstance(sources, dict):
    sources = sources.get('sources', sources.get('items', []))
audit = read('docs/audit/structure-review.json')['items']
rids = {x['id'] for x in req}
sids = {x['id'] for x in sources}
check(len(req) == len(rids) == 16, 'requirement IDs/count')
check(len(sources) == len(sids) == 17, 'source IDs/count')
check(len(audit) == len({x['id'] for x in audit}) == 43, 'audit IDs/count')
covered = set()
for row in audit:
    check(set(row['requirements']) <= rids, row['id'] + ': unknown requirement')
    check(set(row['sources']) <= sids, row['id'] + ': unknown source')
    check((root / row['target']).exists(), row['id'] + ': missing target')
    for field in ('reason', 'alternative', 'practical_proof_needed'):
        check(bool(row[field].strip()), row['id'] + ': empty ' + field)
    covered.update(row['requirements'])
check(covered == rids, 'requirements not fully mapped')
for path in root.rglob('*.json'):
    if '.git' not in path.parts:
        json.loads(path.read_text())
tomllib.loads((root / 'pyproject.toml').read_text())
links = 0
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    content = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if re.match(r'^[a-zA-Z]+:', link) or link.startswith('#'):
            continue
        target = link.split('#')[0]
        if not target:
            continue
        links += 1
        check((path.parent / target).exists(), str(path.relative_to(root)) + ': broken link ' + target)
issues = re.findall(r'^## (ISS-\d+)', (root / 'docs/issues.md').read_text(), re.M)
check(len(issues) == len(set(issues)) == 12, 'issue IDs/count')
check(not (root / 'planning/backlog.md').exists(), 'duplicate backlog')
check((root / 'AGENTS.md').stat().st_size < 16384, 'root rules too large')
for path in root.rglob('.env'):
    check('.git' in path.parts, 'real environment file included')
for error in errors:
    print('ERROR:', error)
if errors:
    sys.exit(1)
print(f'OK: {len(req)} requirements, {len(sources)} sources, {len(audit)} audit points, {len(issues)} issues, {links} local links; JSON/TOML valid.')
