from pathlib import Path
p=Path('tmp/cv/build_cv.py');s=p.read_text()
s=s.replace('SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable','SimpleDocTemplate, BaseDocTemplate, PageTemplate, Frame, FrameBreak, NextPageTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable')
# Separate styles for the first-page overview preserve larger text in the extended CV.
s=s.replace(" 'research':ParagraphStyle", " 'overview_heading':ParagraphStyle('OverviewHeading',fontName='Arial-Bold',fontSize=10.5,leading=14,textColor=INK,spaceBefore=10,spaceAfter=6,keepWithNext=True),\n 'overview_entry':ParagraphStyle('OverviewEntry',fontName='Arial',fontSize=9.3,leading=12.5,spaceAfter=7,textColor=INK),\n 'overview_text':ParagraphStyle('OverviewText',fontName='Arial',fontSize=9.5,leading=13,spaceAfter=8,textColor=INK),\n 'overview_bullet':ParagraphStyle('OverviewBullet',fontName='Arial',fontSize=9.2,leading=12.5,leftIndent=8,firstLineIndent=-8,spaceAfter=8,textColor=INK),\n 'research':ParagraphStyle")
a=s.index('# PAGE 1');b=s.index("page('Extended curriculum vitae','Appointments and education')",a)
new='''# PAGE 1
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
p('I investigate how bacterial antiphage defense systems translate immune signals into molecular responses that restrict viral replication. My lab combines cryo-EM, X-ray crystallography, biophysics, biochemistry, and microbiology to connect protein structure with immune function.','overview_text')
oh('Selected research outputs')
for role,url,label in [
('First author','https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1','Cap1 | Accepted in Nature Structural &amp; Molecular Biology (2026)'),
('First and co-corresponding author','https://www.biorxiv.org/content/10.64898/2026.08.05.743128v1','Chp1 | bioRxiv (2026)'),
('Co-first and co-corresponding author','https://doi.org/10.1126/science.adv9045','Cat1 | Science (2025)'),
('Co-first author','https://doi.org/10.1016/j.cell.2024.10.002','Cad1 | Cell (2024)'),
('Contributor','https://doi.org/10.1038/s41586-023-06902-y','Cam1 | Nature (2024)'),
('First author','https://doi.org/10.15252/embj.2023113418','QacA | The EMBO Journal (2023)')]:p('• '+link(url,'<b>'+label+'</b>')+'<br/>'+role,'overview_bullet')
oh('Scientific contributions')
p('<b>Membrane pores</b><br/>Signal-triggered pore opening and lipid gating in CRISPR-associated effectors.','overview_text')
p('<b>Metabolite depletion</b><br/>ATP-to-ITP conversion and filament-dependent NAD degradation during antiphage defense.','overview_text')
p('<b>Antimicrobial efflux</b><br/>Substrate recognition, proton coupling, and allosteric regulation in QacA.','overview_text')
story.append(NextPageTemplate('Extended'))
'''
s=s[:a]+new+s[b:]
a=s.index('doc=SimpleDocTemplate');b=s.index("Path('tmp/cv/cv_text.txt')",a)
new='''doc=BaseDocTemplate(str(OUT),pagesize=(595.276,841.89),rightMargin=45,leftMargin=45,topMargin=41,bottomMargin=53,title='Puja Majumder Academic Curriculum Vitae',author='Puja Majumder')
header=Frame(45,666,505.276,135,id='overview_header',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
left=Frame(45,53,292,605,id='overview_career',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
right=Frame(362,53,188.276,605,id='overview_research',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
body=Frame(45,53,505.276,747.89,id='extended_body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
def overview_footer(c,doc):
 footer(c,doc)
 c.saveState();c.setStrokeColor(colors.HexColor('#D8E2E4'));c.setLineWidth(.5);c.line(349,60,349,648);c.restoreState()
doc.addPageTemplates([PageTemplate(id='Overview',frames=[header,left,right],onPage=overview_footer),PageTemplate(id='Extended',frames=[body],onPage=footer)])
doc.build(story)
'''
s=s[:a]+new+s[b:]
p.write_text(s)
