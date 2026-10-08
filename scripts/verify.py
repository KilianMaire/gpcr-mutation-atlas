"""Verify embedded data, local downloads and sparse-position density handling."""
from pathlib import Path
from html.parser import HTMLParser
import base64,collections,csv,gzip,html,json,re
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'index.html').read_text()
viewer=base64.b64decode(re.search(r"const INDIVIDUAL_VIEW='([^']+)'",s)[1]).decode()
data=gzip.decompress(base64.b64decode(re.search(r'<script id="compressed-data"[^>]*>(.*?)</script>',s,re.S)[1])).decode()
D=json.loads(data)
assert data==gzip.decompress((ROOT/'src/data.json.gz').read_bytes()).decode()
assert viewer==(ROOT/'src/individual.html').read_text()
assert len(D['receptors'])==845
labels=generic=0;cells=collections.defaultdict(lambda:[0,0])
for r in D['receptors'].values():
 for p,alts in r['v'].items():
  assert 1<=int(p)<=len(r['q']);labels+=len(alts)
 if r['class'] not in ['Unclassified','Hors classification GPCRdb']:
  generic+=sum(len(r['v'].get(str(p),{})) for p in r['genericIndex'].values())
 if r['class']=='Class A (Rhodopsin)':
  for gn,p in r['genericIndex'].items():cells[gn][0]+=1;cells[gn][1]+=len(r['v'].get(str(p),{}))
assert labels==104042 and generic==58890
assert cells['1x411']==[1,2]
class_count=sum(r['class']=='Class A (Rhodopsin)' for r in D['receptors'].values())
assert class_count==287
maximum=max((n/k,key) for key,(k,n) in cells.items() if k>=class_count*.5)
assert maximum==(308/287,'3x50')
assert "if($('metric').value==='density'&&insufficientCoverage(c))return 'url(#low-coverage-pattern)'" in s
assert 'densityScaleMaximum(MODEL.cells)' in s
class LinkParser(HTMLParser):
 def __init__(self):super().__init__();self.local=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['href','src'] and v and not re.match(r'^[a-zA-Z][\w+.-]*:|^#|^//',v):self.local.append(v)
for text in [s,viewer]:
 p=LinkParser();p.feed(text)
 for path in p.local:assert (ROOT/path.split('#')[0].split('?')[0]).is_file(),path
for path,column,total in [('comptages_positions_equivalentes_par_classe.csv','variants',58890),('comptages_regions_par_classe.csv','variants',104042)]:
 with (ROOT/path).open(encoding='utf-8-sig') as f:assert sum(int(row[column]) for row in csv.DictReader(f))==total
for p in ROOT.rglob('*'):
 if not p.is_file() or '.git' in p.parts:continue
 assert p.stat().st_size<100_000_000,p
 if p.suffix in ['.html','.json','.csv','.fasta','.md','.txt','.py','.svg']:
  text=p.read_text(encoding='utf-8-sig')
  if p.name!='verify.py':assert not re.search(r'/Users/|/var/folders/|gho_[A-Za-z0-9]{20}|github_pat_[A-Za-z0-9]{20}',text,re.I),p
print('PASS: 845 entries, 104042 placed labels, 58890 comparable generic labels, sparse-position masking, source identity, CSV totals and local assets')
