import sys, re, html
sys.path.insert(0,'/tmp/cv-python-deps')
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, PageTemplate, Frame, FrameBreak, NextPageTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from html.parser import HTMLParser
import pymupdf
ROOT=Path.cwd(); OUT=ROOT/'output/pdf/Puja_Majumder_Academic_CV.pdf'
fontdir=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Arial','Arial.ttf'),('Arial-Bold','Arial Bold.ttf'),('Arial-Italic','Arial Italic.ttf'),('Arial-BoldItalic','Arial Bold Italic.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold',italic='Arial-Italic',boldItalic='Arial-BoldItalic')
INK=colors.HexColor('#172B32'); MUTED=colors.HexColor('#4D5E66'); ACCENT=colors.HexColor('#236B72')
styles={
 'name':ParagraphStyle('Name',fontName='Arial-Bold',fontSize=26,leading=31,textColor=INK,spaceAfter=8),
 'role':ParagraphStyle('Role',fontName='Arial-Bold',fontSize=12,leading=17,spaceAfter=5),
 'contact':ParagraphStyle('Contact',fontName='Arial',fontSize=9,leading=13,textColor=MUTED,spaceAfter=4),
 'section':ParagraphStyle('Section',fontName='Arial-Bold',fontSize=12,leading=16,textColor=INK,spaceBefore=12,spaceAfter=7,keepWithNext=True),
 'body':ParagraphStyle('Body',fontName='Arial',fontSize=10,leading=13.3,spaceAfter=6,textColor=INK),
 'overview_heading':ParagraphStyle('OverviewHeading',fontName='Arial-Bold',fontSize=10.5,leading=14,textColor=INK,spaceBefore=10,spaceAfter=6,keepWithNext=True),
 'overview_entry':ParagraphStyle('OverviewEntry',fontName='Arial',fontSize=9.3,leading=12.5,spaceAfter=7,textColor=INK),
 'overview_text':ParagraphStyle('OverviewText',fontName='Arial',fontSize=9.5,leading=13,spaceAfter=8,textColor=INK),
 'overview_bullet':ParagraphStyle('OverviewBullet',fontName='Arial',fontSize=9.2,leading=12.5,leftIndent=8,firstLineIndent=-8,spaceAfter=8,textColor=INK),
 'research':ParagraphStyle('ResearchNarrative',fontName='Arial',fontSize=10.8,leading=15.5,spaceAfter=10,textColor=INK),
 'entry':ParagraphStyle('Entry',fontName='Arial',fontSize=9.7,leading=13.4,spaceAfter=4,textColor=INK),
 'small':ParagraphStyle('Small',fontName='Arial',fontSize=9.3,leading=13,spaceAfter=5,textColor=MUTED),
 'highlight':ParagraphStyle('Highlight',fontName='Arial',fontSize=9.5,leading=13,leftIndent=10,firstLineIndent=-10,spaceAfter=5,textColor=MUTED),
 'pub':ParagraphStyle('Publication',fontName='Arial',fontSize=9.3,leading=12.5,leftIndent=19,firstLineIndent=-19,spaceAfter=10,textColor=INK),
 'kicker':ParagraphStyle('Kicker',fontName='Arial-Bold',fontSize=9,leading=12,textColor=ACCENT,spaceAfter=7),
}
story=[]; record=[]
def p(t,style='body'):
 story.append(Paragraph(t,styles[style]));record.append(re.sub('<[^>]+>','',html.unescape(t)))
def h(t):
 p(t,'section')
def page(k,title):
 story.append(PageBreak());p(k.upper(),'kicker');p(title,'name')
def e(date,title,detail=''):
 p(f'<b>{date}</b> &nbsp; | &nbsp; <b>{title}</b>'+('<br/>'+detail if detail else ''),'entry')
def link(url,label):return f'<link href="{url}" color="#24646D">{label}</link>'
# PAGE 1
p('Puja Majumder','name')
p('Assistant Professor | Principal Investigator, Majumder Lab','role')
p('Department of Bioscience and Biotechnology, IIT Kharagpur, India','contact')
p(link('mailto:puja@bt.iitkgp.ac.in','puja@bt.iitkgp.ac.in')+' &nbsp; | &nbsp; +91-3222-284524 &nbsp; | &nbsp; '+link('https://pujamajumder.github.io/','Lab website'),'contact')
p(link('https://orcid.org/0000-0002-5421-6814','ORCID 0000-0002-5421-6814')+' &nbsp; | &nbsp; '+link('https://scholar.google.com/citations?user=a9JYDr4AAAAJ','Google Scholar'),'contact')
story.append(FrameBreak())
def oh(t):p(t,'overview_heading')
def oe(date,title,detail):p('<b>'+date+' | '+title+'</b><br/>'+detail,'overview_entry')
oh('Academic appointments')
oe('June 2026 - present','Assistant Professor','Department of Bioscience and Biotechnology, IIT Kharagpur, India')
oe('2025 - 2026','Senior Research Scientist','Memorial Sloan Kettering Cancer Center, New York, USA')
oe('2024 - 2025','Research Associate','Memorial Sloan Kettering Cancer Center, New York, USA')
oe('2022 - 2024','Research Scholar','Memorial Sloan Kettering Cancer Center, New York, USA | Dinshaw J. Patel Lab')
oe('February 2021 - March 2022','Research Associate','Molecular Biophysics Unit, Indian Institute of Science, Bengaluru, India')
oh('Education')
oe('2015 - 2021','PhD in Structural Biology','Indian Institute of Science, Bengaluru<br/>Supervisor: Prof. Aravind Penmatsa<br/>Thesis: Structural and Functional Investigation of a Multi-drug Efflux Transporter QacA')
oe('2013 - 2015','MSc in Biotechnology','Jawaharlal Nehru University, New Delhi<br/>First Class First, Gold Medal')
oe('2011 - 2013','BSc Honours in Microbiology',"St. Xavier’s College (Autonomous), Kolkata<br/>First Class Honours")
oh('Awards and fellowships')
for t in ['<b>2025</b> Ludwig Cancer Research Postdoctoral Fellowship and Award','<b>2019</b> Best Poster Award, EMBO Workshop on Tools for Structural Biology of Membrane Proteins','<b>2018</b> Best Poster Award, Indian Biophysical Society Meeting, IISER Pune','<b>2015</b> GATE Doctoral Fellowship; DST INSPIRE Scholarship; MSc Gold Medal, JNU','<b>2013</b> CEEB Fellowship, Combined Entrance Examination for Biotechnology']:p(t,'overview_entry')
story.append(FrameBreak())
oh('Research focus')
p('I investigate how bacterial antiphage defense systems translate immune signals into molecular responses that restrict viral replication. My lab combines cryo-EM, X-ray crystallography, biophysics, biochemistry, microbiology, and computational biology to connect protein structure with immune function.','overview_text')
oh('Selected research outputs')
for role,url,label in [
('Co-first author','https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1','Cap1 | Accepted in Nature Structural &amp; Molecular Biology (2026)'),
('First and co-corresponding author','https://www.biorxiv.org/content/10.64898/2026.08.05.743128v1','Chp1 | bioRxiv (2026)'),
('Co-first and co-corresponding author','https://doi.org/10.1126/science.adv9045','Cat1 | Science (2025)'),
('Co-first author','https://doi.org/10.1016/j.cell.2024.10.002','Cad1 | Cell (2024)'),
('Co-author','https://doi.org/10.1038/s41586-023-06902-y','Cam1 | Nature (2024)'),
('First author','https://doi.org/10.15252/embj.2023113418','QacA | The EMBO Journal (2023)')]:p('• '+link(url,'<b>'+label+'</b>')+'<br/>'+role,'overview_bullet')
oh('Scientific contributions')
p('<b>Membrane pores</b><br/>Signal-triggered pore opening and lipid gating in CRISPR-associated effectors.','overview_text')
p('<b>Metabolic changes</b><br/>ATP-to-ITP conversion and filament-dependent NAD degradation during antiphage defense.','overview_text')
p('<b>Antimicrobial efflux</b><br/>Substrate recognition, proton coupling, and allosteric regulation in QacA.','overview_text')
story.append(NextPageTemplate('Extended'))
page('Extended curriculum vitae','Appointments and education')
h('Academic appointments')
e('June 2026 - present','Assistant Professor','Department of Bioscience and Biotechnology, IIT Kharagpur, India')
e('2025 - 2026','Senior Research Scientist','Memorial Sloan Kettering Cancer Center, New York, USA')
e('2024 - 2025','Research Associate','Memorial Sloan Kettering Cancer Center, New York, USA')
e('2022 - 2024','Research Scholar','Memorial Sloan Kettering Cancer Center, New York, USA | Dinshaw J. Patel Lab')
e('February 2021 - March 2022','Research Associate','Molecular Biophysics Unit, Indian Institute of Science, Bengaluru, India')
h('Education')
e('2015 - 2021','PhD in Structural Biology','Indian Institute of Science, Bengaluru | Supervisor: Prof. Aravind Penmatsa<br/>Thesis: Structural and Functional Investigation of a Multi-drug Efflux Transporter QacA')
e('2013 - 2015','MSc in Biotechnology','Jawaharlal Nehru University, New Delhi | First Class First, Gold Medal')
e('2011 - 2013','BSc Honours in Microbiology',"St. Xavier’s College (Autonomous), Kolkata | First Class Honours")
h('Awards and fellowships')
for t in ['<b>2025</b> Ludwig Cancer Research Postdoctoral Fellowship and Award','<b>2019</b> Best Poster Award, EMBO Workshop on Tools for Structural Biology of Membrane Proteins','<b>2018</b> Best Poster Award, Indian Biophysical Society Meeting, IISER Pune','<b>2015</b> GATE Doctoral Fellowship; DST INSPIRE Scholarship; MSc Gold Medal, JNU','<b>2013</b> CEEB Fellowship, Combined Entrance Examination for Biotechnology']:p(t,'small')
h('Methods and technical expertise')
for title,body in [
('Cryo-EM','Sample preparation, Vitrobot grid freezing and clipping; independent microscope use; EPU and SerialEM data collection; CryoSPARC and RELION processing; soluble and membrane proteins, filaments, and supramolecular complexes.'),
('Crystallography and molecular analysis','Protein crystallization, synchrotron data collection, structure determination and refinement; HKL-3000, CCP4, REFMAC, Coot, and Phenix.'),
('Biochemistry and biophysics','Protein purification; antibody, Fab, and nanobody approaches; ITC, MST, SEC-MALS, mass photometry, fluorescence spectroscopy, circular dichroism, nano-DSF, and membrane transport assays.'),
('Computation and analysis','GROMACS molecular dynamics; AlphaFold, Foldseek, DALI, and BLAST; ChimeraX, PyMOL, GraphPad Prism, Origin, and Illustrator.')]:p('<b>'+title+'</b> '+body,'small')
h('Laboratory development and mentorship')
p('Established the Majumder Lab at IIT Kharagpur in June 2026, focusing on bacterial antiphage defence through structural biology, biophysics, biochemistry, and microbiology. Bishnupada Mandal joined the PhD programme in November 2026 as the lab’s first research scholar.','small')
# PAGE 2
page('Extended curriculum vitae','Contributions to science')
for title,body in [
('CRISPR membrane pores and lipid gating','Membrane-associated immune effectors link intracellular infection signals to growth arrest, but the structural basis of their activation requires direct mechanistic analysis. Cap1 and Chp1 reveal distinct routes from cyclic oligoadenylate recognition to membrane depolarization. Cap1 opens a preformed tetrameric pore following cyclic tetra-adenylate binding. Chp1 undergoes a lipid-gated conformational switch that removes pore obstruction and permits ion flow. These studies connect second-messenger signalling to antiviral growth arrest. Cap1: co-first author; accepted in Nature Structural &amp; Molecular Biology. Chp1: first and co-corresponding author, bioRxiv 2026.'),
('Filament assembly and NAD depletion','TIR-domain immune proteins can couple higher-order assembly to catalytic activity. I resolved the active supramolecular assembly of the Cat1 CARF-TIR effector by cryo-EM. Structural and functional studies linked cyclic signal recognition, filament-network formation, and a composite NADase active site to depletion of cellular NAD during antiviral defence. Co-first and co-corresponding author, Science 2025.'),
('Metabolic reprogramming in antiviral defence','Type III CRISPR-Cas effectors can defend cells by changing essential metabolite pools. I combined X-ray crystallography, cryo-EM, and biochemical characterization to define signal recognition and catalytic regulation in Cad1. The work established how a cyclic nucleotide-activated adenosine deaminase converts ATP to ITP, arrests infected-cell growth, and limits phage propagation. Co-first author, Cell 2024.'),
('Antibody-assisted structural biology of membrane effectors','I used high-affinity antibody fragments as fiducial markers to resolve the small membrane-associated CRISPR effector Cam1. Its tetrameric architecture provides a structural basis for understanding membrane depolarization during type III CRISPR immunity. Nature 2024.'),
('Antibacterial transport and allosteric regulation','Multidrug efflux pumps protect bacteria from chemically diverse antibacterial compounds and contribute to antimicrobial resistance. I determined the nanobody-bound QacA transporter structure at 3.6 angstrom resolution and used structure-guided functional assays to establish the role of an extracellular helical hairpin in efflux. Earlier work identified acidic residues governing substrate recognition, proton coupling, and multidrug transport. First-author papers in The EMBO Journal 2023 and Journal of Molecular Biology 2019.')]:
 h(title);p(body,'research')
# PAGE 3
page('Extended curriculum vitae','Publications')
p('Eight published journal articles and two preprints (one accepted for journal publication). Authorship contributions are indicated explicitly.','small')
class Lists(HTMLParser):
 def __init__(self):super().__init__();self.items=[];self.buf='';self.active=False
 def handle_starttag(self,t,a):
  if t=='li':self.active=True;self.buf=''
  elif self.active and t in ('strong','em','sup'):self.buf+={'strong':'<b>','em':'<i>','sup':'<super>'}[t]
  elif self.active and t=='a':self.buf+='<link href="'+dict(a)['href']+'" color="#24646D">'
 def handle_endtag(self,t):
  if t=='li':self.items.append(re.sub(r'\s+',' ',self.buf).strip());self.active=False
  elif self.active and t in ('strong','em','sup'):self.buf+={'strong':'</b>','em':'</i>','sup':'</super>'}[t]
  elif self.active and t=='a':self.buf+='</link>'
 def handle_data(self,d):
  if self.active:self.buf+=html.escape(d)
parser=Lists();parser.feed(Path('Publications.html').read_text())
h('Preprints')
for i,t in enumerate(parser.items[:2],1):
 t=t.replace('&#8225;','‡');p(f'{i}. '+t,'pub')
h('Journal articles')
for i,t in enumerate(parser.items[2:],1):p(f'{i}. '+t.replace('∗','*'),'pub')
# PAGE 4
page('Extended curriculum vitae','Scientific engagement')
h('Invited and selected lectures')
for date,title,detail in [
('2027','Bose Institute, Kolkata','Invited lecture | Upcoming; date to be announced'),
('October 2026','EMSI 2026, Kolkata','Invited lecture on Chp1 membrane pore activation and lipid gating'),
('July 2026','Bhabha Atomic Research Centre, Mumbai','Invited lecture on the Cap1 membrane pore complex and bacterial antiviral defence'),
('May 2026','Symposium on the Immune System of Bacteria','Selected speaker | Mechanistic diversity of cOA-activated CARF membrane effectors in CRISPR defence'),
('November 2025','SciensPUR','Invited speaker | Diverse immune systems in bacteria'),
('July 2025','US Cryo-EM National Facilities Current Practices Webinar','Invited speaker | Structural basis of a filamentous CRISPR effector revealed by cryo-EM'),
('July 2025','EMSI 2025, Indian Institute of Science, Bengaluru','Keynote speaker | CRISPR beyond nucleases')]:e(date,title,detail)
h('Selected research presentations and training')
for t in ['<b>October 2026</b> Attended the G. N. Ramachandran Lecture Series on Bioinformatics and Computational Biology, IIT Kharagpur.','<b>October 2025</b> CryoET Workshop, Brookhaven National Laboratory.','<b>June 2025</b> Fifth Annual NY Area Cryo-EM Meeting, NYU Langone; oral presentation on Cat1 filament networks and NAD degradation.','<b>October 2024</b> MSKCC Basic Science Retreat; oral presentation on Cat1-mediated antiviral defence.','<b>June 2024</b> Fourth Annual NY Area Cryo-EM Meeting, Columbia University Medical Center; oral presentation on Cad1 and Cam1.','<b>May 2024</b> MSKCC Structural Biology Retreat; oral presentation on Cad1.','<b>October 2019</b> EMBO Workshop, EMBL Hamburg; poster on QacA substrate recognition and transport.']:p(t,'small')
h('Professional memberships')
p('<b>Electron Microscope Society of India</b> | Life member, 2026','entry')
p('<b>Society of Biological Chemists (India)</b> | Life member since August 2026','entry')
h('Research recognition and outreach')
p('<b>IIT Kharagpur Foundation feature</b> | July 25, 2026<br/>Research on the molecular machinery of bacterial immunity featured in the Foundation newsletter. '+link('https://www.iitkgpfoundation.org/article.html?nl=3333','Read feature'),'entry')
p('<b>Research coverage</b> | Rockefeller University press releases highlighted the Cat1 and Cad1 studies, with additional coverage of Cad1 in Genetic Engineering &amp; Biotechnology News and a commentary in Cell Host &amp; Microbe.','entry')

def footer(c,doc):
 c.saveState();w,h=doc.pagesize
 c.setStrokeColor(colors.HexColor('#D8E2E4'));c.setLineWidth(.5);c.line(45,39,w-45,39)
 c.setFont('Arial',8);c.setFillColor(MUTED);c.drawString(45,26,'PUJA MAJUMDER  |  CURRICULUM VITAE');c.drawRightString(w-45,26,f'November 2026  |  {doc.page}');c.restoreState()
doc=BaseDocTemplate(str(OUT),pagesize=(595.276,841.89),rightMargin=45,leftMargin=45,topMargin=41,bottomMargin=53,title='Puja Majumder Academic Curriculum Vitae',author='Puja Majumder')
header=Frame(45,666,505.276,135,id='overview_header',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
left=Frame(45,53,292,605,id='overview_career',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
right=Frame(362,53,188.276,605,id='overview_research',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
body=Frame(45,53,505.276,747.89,id='extended_body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
def overview_footer(c,doc):
 footer(c,doc)
 c.saveState();c.setStrokeColor(colors.HexColor('#D8E2E4'));c.setLineWidth(.5);c.line(349,60,349,648);c.restoreState()
doc.addPageTemplates([PageTemplate(id='Overview',frames=[header,left,right],onPage=overview_footer),PageTemplate(id='Extended',frames=[body],onPage=footer)])
doc.build(story)
Path('tmp/cv/cv_text.txt').write_text('\n\n'.join(record))
f=pymupdf.open(OUT)
f.set_toc([[1,'Research summary',1],[1,'Appointments and education',2],[1,'Contributions to science',3],[1,'Publications',4],[1,'Scientific engagement',5]])
f.saveIncr()
for i,pg in enumerate(f):pg.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(f'tmp/cv/page-{i+1}.png')
print('PDF pages:',len(f))
for i,pg in enumerate(f): print(i+1,len(pg.get_text()),pg.get_text()[:85].replace('\n',' | '))
