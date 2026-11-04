from pathlib import Path
p=Path('tmp/cv/build_cv.py');s=p.read_text()
s=s.replace('SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether','SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable')
s=s.replace("INK=colors.HexColor('#182D35'); MUTED=colors.HexColor('#54646B'); ACCENT=colors.HexColor('#24646D')","INK=colors.HexColor('#172B32'); MUTED=colors.HexColor('#4D5E66'); ACCENT=colors.HexColor('#236B72')")
s=s.replace("fontSize=29,leading=34,textColor=INK,spaceAfter=7","fontSize=26,leading=31,textColor=INK,spaceAfter=8")
s=s.replace("fontSize=13,leading=17,textColor=INK,spaceBefore=8,spaceAfter=6","fontSize=12,leading=16,textColor=INK,spaceBefore=12,spaceAfter=7")
s=s.replace("fontSize=9,leading=12.5,spaceAfter=4","fontSize=9.3,leading=13,spaceAfter=5")
s=s.replace("fontSize=9,leading=12,leftIndent=9,firstLineIndent=-9,spaceAfter=3","fontSize=9.5,leading=13,leftIndent=10,firstLineIndent=-10,spaceAfter=5")
s=s.replace("def h(t):p(t,'section')","def h(t):\n p(t,'section')")
a=s.index('# PAGE 1');b=s.index("h('Academic appointments')",a)
new='''# PAGE 1
p('RESEARCH SUMMARY','kicker')
p('Puja Majumder','name')
p('Assistant Professor and Principal Investigator','role')
p('Majumder Lab | Department of Bioscience and Biotechnology<br/>Indian Institute of Technology Kharagpur, India','contact')
p(link('mailto:puja@bt.iitkgp.ac.in','puja@bt.iitkgp.ac.in')+' &nbsp; | &nbsp; +91-3222-284524 &nbsp; | &nbsp; '+link('https://pujamajumder.github.io/','Lab website'),'contact')
p(link('https://orcid.org/0000-0002-5421-6814','ORCID 0000-0002-5421-6814')+' &nbsp; | &nbsp; '+link('https://scholar.google.com/citations?user=a9JYDr4AAAAJ','Google Scholar'),'contact')
h('Personal statement')
p('I investigate how bacterial antiphage defense systems convert immune signals into molecular responses that restrict viral replication. My research combines single-particle cryo-EM, X-ray crystallography, biophysics, biochemistry, and microbiology to connect protein structure with function. Building on doctoral work on the QacA multidrug efflux transporter at IISc and postdoctoral research in the Dinshaw Patel Lab at MSKCC, I established the Majumder Lab at IIT Kharagpur in June 2026.')
h('Contributions to science')
p('<b>Membrane pore activation.</b> Structural and functional studies of Cap1, Chp1, and Cam1 connect cyclic nucleotide recognition to membrane depolarization. Cap1 and Chp1 reveal distinct mechanisms of pore opening and lipid gating.','entry')
p('<b>Metabolite depletion and immune assembly.</b> Work on Cad1 and Cat1 explains how ATP-to-ITP conversion and filament-dependent NAD degradation can arrest infected-cell growth and limit phage propagation.','entry')
p('<b>Antimicrobial efflux.</b> Nanobody-assisted structural analysis and biochemical assays of QacA identified molecular determinants of substrate recognition, proton coupling, and allosteric regulation.','entry')
h('Selected research outputs')
for role,url,label in [
('Co-first and co-corresponding author','https://doi.org/10.1126/science.adv9045','Science (2025) - Cat1'),
('Co-first author','https://doi.org/10.1016/j.cell.2024.10.002','Cell (2024) - Cad1'),
('Contributor','https://doi.org/10.1038/s41586-023-06902-y','Nature (2024) - Cam1'),
('First author','https://doi.org/10.15252/embj.2023113418','The EMBO Journal (2023) - QacA'),
('First author','https://www.biorxiv.org/content/10.1101/2025.11.13.688252v1','Cap1 - accepted in Nature Structural &amp; Molecular Biology'),
('First and co-corresponding author','https://www.biorxiv.org/content/10.64898/2026.08.05.743128v1','Chp1 preprint (2026)')]:
 p('• '+link(url,'<b>'+label+'</b>')+'<br/>'+role,'highlight')
h('Selected honors and leadership')
p('<b>2025</b> Ludwig Cancer Research Postdoctoral Fellowship and Award<br/><b>2019</b> EMBO Workshop Best Poster Award &nbsp; | &nbsp; <b>2018</b> Indian Biophysical Society Best Poster Award<br/><b>Since June 2026</b> Principal Investigator, Majumder Lab, IIT Kharagpur','small')
page('Extended curriculum vitae','Appointments and education')
'''
s=s[:a]+new+s[b:]
# Keep page 2 as the full academic record; move methods and mentorship here.
a=s.index("h('Methods and technical expertise')");b=s.index('# PAGE 3',a)
expertise=s[a:b]
s=s[:a]+s[b:]
a=s.index('# PAGE 2')
s=s[:a]+expertise+s[a:]
# Give each extended page a concise title.
s=s.replace("page('Research and laboratory leadership','Research contributions')","page('Extended curriculum vitae','Contributions to science')")
s=s.replace("page('Research outputs','Publications')","page('Extended curriculum vitae','Publications')")
s=s.replace("page('Scientific engagement','Lectures and professional activities')","page('Extended curriculum vitae','Scientific engagement')")
# Add concise research-context paragraphs so the contributions page stands on its own.
s=s.replace("('CRISPR membrane pores and lipid gating','Cap1", "('CRISPR membrane pores and lipid gating','Membrane-associated immune effectors link intracellular infection signals to growth arrest, but the structural basis of their activation requires direct mechanistic analysis. Cap1")
s=s.replace("('Filament assembly and NAD depletion','Resolved", "('Filament assembly and NAD depletion','TIR-domain immune proteins can couple higher-order assembly to catalytic activity. Resolved")
s=s.replace("('Metabolic reprogramming in antiviral defence','Combined", "('Metabolic reprogramming in antiviral defence','Type III CRISPR-Cas effectors can defend cells by changing essential metabolite pools. Combined")
s=s.replace("('Antibacterial transport and allosteric regulation','Determined", "('Antibacterial transport and allosteric regulation','Multidrug efflux pumps protect bacteria from chemically diverse antibacterial compounds and contribute to antimicrobial resistance. Determined")
# Footer reads as a coherent CV, with a restrained running header on later pages.
s=s.replace("c.setStrokeColor(colors.HexColor('#D8E2E4'))", "c.setStrokeColor(colors.HexColor('#D8E2E4'))")
s=s.replace("c.setFont('Arial',8);c.setFillColor(MUTED);c.drawString(45,26,'PUJA MAJUMDER  |  ACADEMIC CURRICULUM VITAE');c.drawRightString(w-45,26,f'November 2026  |  {doc.page}');c.restoreState()", "c.setFont('Arial',8);c.setFillColor(MUTED);c.drawString(45,26,'PUJA MAJUMDER  |  CURRICULUM VITAE');c.drawRightString(w-45,26,f'November 2026  |  {doc.page}');c.restoreState()")
p.write_text(s)
