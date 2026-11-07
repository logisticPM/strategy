"""Copy the self-contained build to the GitHub Pages publishing directory."""
from pathlib import Path
import hashlib
import json
root=Path(__file__).resolve().parents[2]
source=root/'strategy-web/offline/index.html'
content=source.read_bytes()
assert b'<div id="root"></div>' in content
target=root/'docs'
target.mkdir(exist_ok=True)
(target/'index.html').write_bytes(content)
(target/'.nojekyll').write_text('',encoding='utf-8')
print(json.dumps({'path':str(target/'index.html'),'sha256':hashlib.sha256(content).hexdigest(),'bytes':len(content)}))
