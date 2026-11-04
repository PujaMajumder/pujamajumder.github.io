from pathlib import Path
import re, sys, html
sys.path.insert(0, '/tmp/cv-python-deps')
from PIL import Image

descriptions = {
 'Team.html': 'Meet Puja Majumder and the Majumder Lab team at IIT Kharagpur, studying bacterial immunity and structural biology.',
 'Profile.html': 'Academic appointments, education, awards, and curriculum vitae of Dr. Puja Majumder, Assistant Professor at IIT Kharagpur.',
 'Publications.html': 'Publications and preprints by Puja Majumder on CRISPR immunity, bacterial antiphage defense, and membrane protein structure and function.',
 'Opportunity.html': 'Explore postdoctoral, PhD, and student research opportunities in bacterial immunity and structural biology at the Majumder Lab, IIT Kharagpur.',
 'News.html': 'Research news, publications, talks, milestones, and updates from the Majumder Lab at IIT Kharagpur.',
}
for p in Path('.').glob('*.html'):
 s=p.read_text()
 if p.name in descriptions and 'name="description"' not in s:
  s=s.replace('</title>', '</title><meta name="description" content="'+descriptions[p.name]+'">',1)
 if p.name=='index.html':
  s=s.replace('href="index.html" aria-current="page"','href="index.html"',1)
  s=s.replace('<a href="index.html">Home</a>','<a href="index.html" aria-current="page">Home</a>',1)
  s=s.replace('Three new routes to','Three routes to')
 if p.name in ('Team.html','Profile.html'):
  for a,b in [('Ph. D in','PhD in'),('M.Sc in','MSc in'),('B. Sc. (Hons.)','BSc (Hons.)'),('St. Xaviers','St. Xavier’s'),('DST Inspire','DST INSPIRE'),('First class first','First Class First')]:s=s.replace(a,b)
  s=s.replace('GATE Doctoral Fellowship, Science and Engineering Research Board (SERB), Government of India','GATE Doctoral Fellowship')
 if p.name=='Profile.html':
  s=s.replace('href="Team.html" aria-current="page"','href="Team.html"')
 if p.name=='Publications.html':
  s=s.replace('C.F.Baca','C. F. Baca').replace('S. Dudey','S. Dubey').replace('solvent-exposed acidic residue;','solvent-exposed acidic residues;')
  s=s.replace('<strong>P. Majumder</strong>,<sup>&#8225;,</sup>*  J.', '<strong>P. Majumder</strong><sup>&#8225;,*</sup>, J.')
  s=s.replace('P. Majumder</strong>,<sup>&#8225;</sup>', 'P. Majumder</strong><sup>&#8225;</sup>,')
  s=s.replace('C. W. Cahir,<sup>&#8225;</sup>', 'C. W. Cahir<sup>&#8225;</sup>,')
  s=s.replace('C. F. Baca,<sup>&#8225;</sup>', 'C. F. Baca<sup>&#8225;</sup>,')
  s=s.replace('L. A. Marraffini*;', 'L. A. Marraffini<sup>*</sup>;')
  s=s.replace('n→ π∗', 'n→π*')
 if p.name=='Opportunity.html':
  s=s.replace('Department of Bioscience & Biotechnology', 'Department of Bioscience &amp; Biotechnology')
  start=s.index('<h2>Postdoctoral Research Associate</h2>');end=s.index('</section></main>',start)
  s=s[:start]+'''<h2>Postdoctoral researchers</h2><p>We welcome enquiries from recent PhD graduates and early-career researchers in structural biology or biochemistry. Positions on externally funded projects will be advertised here as they become available.</p><p>You may also explore the <a href="https://www.anrfonline.in/ANRF/npdf">ANRF National Postdoctoral Fellowship</a>, <a href="https://dst.gov.in/scientific-programmes/scientific-engineering-research/women-scientists-programs">DST programmes for women scientists</a>, and the <a href="https://www.iitkgp.ac.in/pdf">IIT Kharagpur Postdoctoral Fellowship</a>. Please contact Dr. Puja Majumder in advance to discuss a suitable project and research proposal. Eligibility and application dates are set by each scheme.</p><a class="paper-link" href="mailto:puja@bt.iitkgp.ac.in">Discuss a project ↗</a></article><article class="role-card"><p class="eyebrow">02 / OPPORTUNITIES</p><h2>Prospective PhD students</h2><p>We welcome motivated students interested in cryo-EM, structural biology, biochemistry, and bacterial immunity. Please consult the <a href="https://www.iitkgp.ac.in/admission-phd">IIT Kharagpur PhD admissions page</a> for eligibility and application details, and contact Dr. Puja Majumder to discuss your research interests and possible projects.</p><a class="paper-link" href="mailto:puja@bt.iitkgp.ac.in">Discuss a project ↗</a></article><article class="role-card"><p class="eyebrow">03 / OPPORTUNITIES</p><h2>Undergraduate and master’s project students</h2><p>IIT Kharagpur students interested in an undergraduate or master’s thesis in the lab are welcome to get in touch. We encourage enquiries from students with a background in biochemistry, as well as engineering students with coding experience, preferably in Python, who would like to explore bioinformatics questions in bacterial antiphage defense.</p><a class="paper-link" href="mailto:puja@bt.iitkgp.ac.in">Discuss a project ↗</a></article>'''+s[end:]
 if p.name=='News.html':
  for a,b in [('Rockeller','Rockefeller'),('Genetic Engineering and Biology News','Genetic Engineering &amp; Biotechnology News'),('Cell Host and Microbe','Cell Host &amp; Microbe'),('structuaral','structural'),('fruitition','fruition'),('endavour','endeavour'),('Ph. D thesis','PhD thesis'),('at the NYC','in New York City'),('on June-6, 2024','on June 6, 2024'),('adenosine deaminase1','adenosine deaminase 1')]:s=s.replace(a,b)
  s=s.replace('structural-biology/ "','structural-biology/"')
  s=s.replace('Delighted to deliver an invited lecture at','Delighted to have delivered an invited lecture at')
  s=s.replace('This is the oldest IIT and the campus green does mitigate the heat of Indian summer!', 'The green campus is a welcome respite from the Indian summer!')
  s=s.replace('On the left, there is an animated view of the structure which was of great fun to solve!', 'The accompanying animation shows the structure, which was great fun to solve!')
  s=s.replace('The structural part of the PhD thesis work', 'The structural part of my PhD thesis work')
 if p.name=='Research.html':
  # Apply the shared footer and base page layout to Research as well.
  s=s.replace('<link rel="stylesheet" href="assets/css/site.css?v=antiphage-20261104">', '<link rel="stylesheet" href="assets/css/site.css?v=antiphage-20261104"><link rel="stylesheet" href="assets/css/pages.css?v=antiphage-20261104">')
  for a,b in [('two Cat1 dimers forms','two Cat1 dimers form'),('the product reveals','the product reveal'),('All together our study','Together, our study'),('in presence of','in the presence of'),('contains deaminase enzyme domain which is repurposed to antiphage defense','contains a deaminase domain repurposed for antiphage defense'),('x-ray crystallography','X-ray crystallography'),('cA 4 bound','cA4-bound'),('cA4 -bound','cA4-bound'),('ITP accumulation leads','ITP accumulation lead'),('effectors that belongs','effectors that belong'),('state-of the art','state-of-the-art'),('employ similar approach','employ a similar approach')]:s=s.replace(a,b)
  # Remove outdated proposal language from the completed Cam1 study.
  s=re.sub(r'To\s+explore the mechanistic details of activation of Cam1.*?To know more,', 'These findings provide a structural basis for understanding cOA-activated membrane effectors in CRISPR-Cas immunity. To know more,', s, flags=re.S)
 # Responsive images reserve their correct aspect ratio to avoid page jumps.
 def dimensions(m):
  tag=m.group();src=re.search(r'src="([^"]+)"',tag)
  if not src or not Path(src[1]).is_file():return tag
  try:
   with Image.open(src[1]) as im:w,h=im.size
  except Exception:return tag
  if 'width=' not in tag:tag=tag[:-1]+f' width="{w}" height="{h}">'
  if 'decoding=' not in tag:tag=tag[:-1]+' decoding="async">'
  return tag
 s=re.sub(r'<img\b[^>]*>',dimensions,s)
 s=s.replace('v=antiphage-20261104','v=review-20261104')
 p.write_text(s)

p=Path('assets/css/pages.css');s=p.read_text();s+='''
/* Keep long names, contact links, and headings readable on narrow screens. */
.role-card p+p,.news-card p+p,.detail-copy p+p{margin-top:14px}
.principal-overview>div,.graduate-member>div{min-width:0}
@media(max-width:380px){.principal-overview,.graduate-member{flex-direction:column;align-items:flex-start}.principal-overview>img{width:135px;height:150px}}
''';p.write_text(s)
p=Path('assets/css/site.css');s=p.read_text();s+='''
@media(max-width:380px){h1{font-size:36px}.project-nav{grid-template-columns:repeat(2,minmax(0,1fr))}.project-nav a{font-size:11px}.closing{padding:24px}}
''';p.write_text(s)

p=Path('tmp/cv/build_cv.py');s=p.read_text().replace("('First author','https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1'", "('Co-first author','https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1'")
s=s.replace('Cap1: first author;', 'Cap1: co-first author;').replace('<b>Metabolite depletion</b>', '<b>Metabolic changes</b>')
s=s.replace('Eight journal articles and two preprints.', 'Eight published journal articles and two preprints (one accepted for journal publication).')
s=s.replace("('Contributor','https://doi.org/10.1038/s41586-023-06902-y'", "('Co-author','https://doi.org/10.1038/s41586-023-06902-y'")
p.write_text(s)
print('Content, metadata, image dimensions, narrow-screen styles, and CV source updated.')
