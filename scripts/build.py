"""Build the standalone atlas from its readable templates and compressed data."""
from pathlib import Path
import base64,gzip,json
ROOT=Path(__file__).resolve().parents[1]
viewer=(ROOT/'src/individual.html').read_bytes()
data=gzip.decompress((ROOT/'src/data.json.gz').read_bytes())
json.loads(data)
template=(ROOT/'src/template.html').read_text()
assert template.count('__INDIVIDUAL_VIEW__')==1
assert template.count('__PAYLOAD__')==1
result=template.replace('__INDIVIDUAL_VIEW__',base64.b64encode(viewer).decode()).replace('__PAYLOAD__',base64.b64encode(gzip.compress(data,compresslevel=9,mtime=0)).decode())
(ROOT/'index.html').write_text(result)
print('Built index.html')
