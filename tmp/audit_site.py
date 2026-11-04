from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, collections, sys
sys.path.insert(0,'/tmp/cv-python-deps')
from PIL import Image

class Page(HTMLParser):
 def __init__(self,p):
  super().__init__(convert_charrefs=True);self.p=p;self.ids=[];self.refs=[];self.images=[];self.errors=[];self.stack=[];self.count=collections.Counter();self.metas={}
 def handle_starttag(self,t,attrs):
  a=dict(attrs);self.count[t]+=1
  if 'id' in a:self.ids.append(a['id'])
  for k in ('href','src'):
   if a.get(k):self.refs.append(a[k])
  if t=='meta':self.metas[a.get('name')]=a.get('content')
  if t=='img':self.images.append(a)
  if t not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):self.stack.append(t)
 def handle_endtag(self,t):
  if not self.stack or self.stack[-1]!=t:self.errors.append('Unbalanced closing '+t+' after '+str(self.stack[-3:]))
  elif self.stack:self.stack.pop()

pages={p.name:Page(p) for p in sorted(Path('.').glob('*.html'))}
for name,p in pages.items():p.feed(p.p.read_text())
errors=[];external=set();local=set();nimages=0
for name,p in pages.items():
 errors += [name+': '+e for e in p.errors]
 if p.stack:errors.append(name+': unclosed '+str(p.stack))
 if p.count['h1']!=1:errors.append(name+': must have one h1')
 if not p.metas.get('description'):errors.append(name+': missing description')
 if len(p.ids)!=len(set(p.ids)):errors.append(name+': duplicate ids')
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme in ('http','https'):external.add(ref);continue
  if u.scheme:continue
  target=Path(unquote(u.path)) if u.path else p.p
  local.add(str(target))
  if not target.is_file():errors.append(name+': missing '+ref)
  if u.fragment and str(target) in pages and unquote(u.fragment) not in pages[str(target)].ids:errors.append(name+': missing anchor '+ref)
 for im in p.images:
  nimages+=1
  if not im.get('alt'):errors.append(name+': missing image alt '+im['src'])
  if not all(k in im for k in ('width','height')):errors.append(name+': missing image dimensions '+im['src'])
  try:
   with Image.open(im['src']) as pic:
    pic.verify()
  except Exception as e:errors.append(name+': invalid image '+str(e))
result={'pages':len(pages),'image_instances':nimages,'local_targets':len(local),'external_urls':sorted(external),'errors':errors}
Path('tmp/site-audit.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='external_urls'},indent=2))
if errors:sys.exit(1)
