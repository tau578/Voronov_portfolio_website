from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/Sergei_Voronov_CV_2026.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, file in [('Arial','arial.ttf'), ('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/'+file))
c = canvas.Canvas(str(OUT), pagesize=(595.276,841.89))
c.setTitle('Sergei Voronov - Technical Game Designer')
c.setAuthor('Sergei Voronov')
base = ParagraphStyle('base',fontName='Arial',fontSize=9.5,leading=13,textColor=colors.black)
bold = ParagraphStyle('bold',parent=base,fontName='Arial-Bold',fontSize=10,leading=13)
small = ParagraphStyle('small',parent=base,fontSize=9,leading=12)
def p(text,x,y,w,style=base,gap=5):
    para=Paragraph(text,style)
    _,h=para.wrap(w,800)
    para.drawOn(c,x,y-h)
    return y-h-gap
def bar(title,x,y,w):
    c.setFillColor(colors.HexColor('#c4c4c4'))
    c.rect(x,y-19,w,19,stroke=0,fill=1)
    p(title,x+6,y-3,w-12,bold,0)
    return y-27
def bullet(text,x,y,w):
    p('•',x,y,10,base,0)
    return p(escape(text),x+11,y,w-11,base,3)
def link(label,url):
    return '<link href="'+escape(url,{'"':'&quot;'})+'"><u>'+escape(label)+'</u></link>'

x=32; w=531.276; y=811
y=p('Sergei Voronov',x,y,w,ParagraphStyle('name',parent=bold,fontSize=25,leading=29),3)
y=p('Technical Game Designer',x,y,w,ParagraphStyle('role',parent=bold,fontSize=13,leading=17),4)
y=p('Gameplay Systems · Unity Implementation · Visual Scripting · Level Design',x,y,w,base,8)
y=p('Berlin, Germany, open to relocate',x,y,w,base,3)
y=p(link('sergei.voronov.workspace.1991@gmail.com','mailto:sergei.voronov.workspace.1991@gmail.com'),x,y,w,base,3)
y=p('Portfolio: '+link('sergeivoronov.dev','https://sergeivoronov.dev/')+' &nbsp;&nbsp; LinkedIn: '+link('linkedin.com/in/sergei-voronov-96aa3284','https://www.linkedin.com/in/sergei-voronov-96aa3284'),x,y,w,small,6)
y=p('Open to Working Student and Junior Technical Game Design roles',x,y,w,bold,14)
top=y
lw=329; rx=379; rw=184.276
y=bar('PROFILE',x,y,lw)
y=p('Junior Technical Game Designer with commercial production experience at Paintbucket Games. I design and implement gameplay systems in Unity, translate design ideas into playable content, and work comfortably within existing production frameworks. My main strengths are gameplay systems, visual scripting, level design, and rapid iteration.',x,y,lw,base,12)
y=bar('EXPERIENCE',x,y,lw)
y=p('Paintbucket Games — Technical Design Intern',x,y,lw,bold,3)
y=p('Berlin · Mar 2026 – Jul 2026',x,y,lw,base,6)
for t in [
'Worked on The Darkest Files: The Battalion DLC, gaining first commercial production experience in game development.',
'Implemented gameplay systems and progression logic using Unity and Articy: Draft X within the studio’s custom framework.',
'Collaborated with programmers, narrative designers, technical artists and producers in weekly sprints and daily stand-ups.',
'Used Plastic SCM, Codecks and internal reviews/playtests to iterate on features and maintain gameplay reliability.']:
    y=bullet(t,x,y,lw)
y-=5
y=p('Previous Professional Background — Law &amp; Education',x,y,lw,bold,5)
for t in ['Strong background in structured analysis, documentation, research and responsibility.','Experience communicating clearly, handling complex information and working independently.']:
    y=bullet(t,x,y,lw)
experience_bottom=y
projects=[
('The Darkest Files: Battalion','https://store.steampowered.com/app/2058730/The_Darkest_Files/','Implemented progression logic, narrative scripting and courtroom gameplay in Unity and Articy: Draft X. Configured scenes, waypoints and cameras; tested and debugged gameplay sequences.'),
('Berlin Delivery Driver','https://prabhdeep-chhatwal.itch.io/berlin-delivery-driver','Driving and delivery game featuring route flow, interaction systems, AI traffic, UI feedback and gameplay tuning.'),
('What ‘Actually’ Makes Us Punk?','https://lol-wal.itch.io/what-actually-makes-us-punk','Remake of a dialogue-focused game expanded with a newly designed rhythm-game system and level design.')]
y=bar('SKILLS',rx,top,rw)
for title,items in [
('Technical',['Unity Engine (2D / 3D)','C# gameplay scripting','Unity Visual Scripting','Articy: Draft X','Gameplay systems implementation','System integration & debugging','UI logic','Plastic SCM','Codecks','Miro']),
('Design',['Gameplay mechanics prototyping','Level design & pacing','Interaction systems','Rapid iteration & playtesting','Cross-disciplinary collaboration']),
('Production',['Agile production','Weekly sprints','Daily stand-ups','Internal reviews & playtests'])]:
    y=p(title,rx,y,rw,bold,5)
    for t in items:
        y=p(escape(t),rx,y,rw,small,2)
    y-=7
education_top=y
y=bar('EDUCATION',rx,y,rw)
y=p('B.A. Game Design',rx,y,rw,bold,4)
y=p('University of Europe for Applied Sciences, Berlin',rx,y,rw,base,4)
y=p('2023 – 2027',rx,y,rw,base,7)
y=p('Focus: gameplay prototyping, technical design, level scripting, interaction systems',rx,y,rw,base,12)
y=bar('LANGUAGES',rx,y,rw)
for t in ['Russian — Native','English — B2 (IELTS 6.5)','German — A1.2']:
    y=p(t,rx,y,rw,base,5)
right_bottom=y+5
assert experience_bottom-education_top>=4,(experience_bottom,education_top)
y=bar('SELECTED PROJECTS',x,education_top,lw)
heights=[]
for title,url,desc in projects:
    ht=Paragraph(link(title,url),bold).wrap(lw,800)[1]
    hd=Paragraph(desc,base).wrap(lw,800)[1]
    heights.append(ht+3+hd)
project_gap=(y-right_bottom-sum(heights))/(len(projects)-1)
assert project_gap>=6,project_gap
for i,(title,url,desc) in enumerate(projects):
    y=p(link(title,url),x,y,lw,bold,3)
    y=p(desc,x,y,lw,base,project_gap if i<len(projects)-1 else 0)
left_bottom=y
assert abs(left_bottom-right_bottom)<0.01
assert min(y,left_bottom)>25,(y,left_bottom)
c.showPage(); c.save()
print(OUT)
print('Bottom positions:',left_bottom,y)
