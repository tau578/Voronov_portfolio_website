from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/Sergei_Voronov_CV_2026_RU.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, file in [('Arial','arial.ttf'), ('Arial-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/'+file))
c = canvas.Canvas(str(OUT), pagesize=(595.276,841.89))
c.setTitle('Сергей Воронов — Технический геймдизайнер')
c.setAuthor('Сергей Воронов')
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
    return p(escape(text),x+11,y,w-11,ParagraphStyle('ru_bullet',parent=base,leading=12),3)
def link(label,url):
    return '<link href="'+escape(url,{'"':'&quot;'})+'"><u>'+escape(label)+'</u></link>'

x=32; w=531.276; y=811
y=p('Сергей Воронов',x,y,w,ParagraphStyle('name',parent=bold,fontSize=25,leading=29),3)
y=p('Технический геймдизайнер',x,y,w,ParagraphStyle('role',parent=bold,fontSize=13,leading=17),4)
y=p('Игровые системы · Реализация в Unity · Визуальный скриптинг · Дизайн уровней',x,y,w,base,8)
y=p('Берлин, Германия, готов к переезду',x,y,w,base,3)
y=p(link('sergei.voronov.workspace.1991@gmail.com','mailto:sergei.voronov.workspace.1991@gmail.com'),x,y,w,base,3)
y=p('Портфолио: '+link('sergeivoronov.dev','https://sergeivoronov.dev/')+' &nbsp;&nbsp; LinkedIn: '+link('linkedin.com/in/sergei-voronov-96aa3284','https://www.linkedin.com/in/sergei-voronov-96aa3284'),x,y,w,small,6)
y=p('Рассматриваю позиции Working Student и младшего технического геймдизайнера',x,y,w,bold,14)
top=y
lw=329; rx=379; rw=184.276
y=bar('О СЕБЕ',x,y,lw)
y=p('Младший технический геймдизайнер с опытом коммерческой разработки в Paintbucket Games. Проектирую и реализую игровые системы в Unity, воплощаю идеи в игровой контент и уверенно работаю в существующих фреймворках. Мои сильные стороны — игровые системы, визуальный скриптинг, дизайн уровней и быстрые итерации.',x,y,lw,base,12)
y=bar('ОПЫТ РАБОТЫ',x,y,lw)
y=p('Paintbucket Games — Стажёр по техническому дизайну',x,y,lw,bold,3)
y=p('Берлин · Март 2026 – Июль 2026',x,y,lw,base,6)
for t in [
'Работал над DLC The Darkest Files: The Battalion, получив первый опыт коммерческой разработки игр.',
'Реализовывал игровые системы и логику прогрессии в Unity и Articy: Draft X на базе собственного фреймворка студии.',
'Работал с программистами, нарративными дизайнерами, теххудожниками и продюсерами: еженедельные спринты, ежедневные стендапы.',
'Использовал Plastic SCM, Codecks, внутренние ревью и плейтесты для доработки функций и стабильной работы игровых систем.']:
    y=bullet(t,x,y,lw)
y-=5
y=p('Предыдущий опыт — Юриспруденция и образование',x,y,lw,bold,5)
for t in ['Развитые навыки системного анализа, работы с документацией и исследования; ответственный подход к работе.','Опыт ясной коммуникации, работы со сложной информацией и самостоятельного выполнения задач.']:
    y=bullet(t,x,y,lw)
experience_bottom=y
projects=[
('The Darkest Files: Battalion','https://store.steampowered.com/app/2058730/The_Darkest_Files/','Реализовывал логику прогрессии, нарративные сценарии и судебный игровой процесс в Unity и Articy: Draft X. Настраивал сцены, точки перемещения и камеры; тестировал и отлаживал игровые последовательности.'),
('Berlin Delivery Driver','https://prabhdeep-chhatwal.itch.io/berlin-delivery-driver','Игра о вождении и доставке с системой маршрутов, взаимодействиями, ИИ дорожного движения, обратной связью интерфейса и настройкой игрового процесса.'),
('What ‘Actually’ Makes Us Punk?','https://lol-wal.itch.io/what-actually-makes-us-punk','Ремейк игры с акцентом на диалоги, дополненный новой системой ритм-игры и дизайном уровней.')]
y=bar('НАВЫКИ',rx,top,rw)
for title,items in [
('Технические',['Движок Unity (2D / 3D)','Игровой скриптинг на C#','Unity Visual Scripting','Articy: Draft X','Реализация игровых систем','Интеграция и отладка систем','Логика интерфейса','Plastic SCM','Codecks','Miro']),
('Дизайн',['Прототипирование игровых механик','Дизайн уровней и игровой темп','Системы взаимодействия','Быстрые итерации и плейтесты','Междисциплинарная работа']),
('Производство',['Разработка по Agile','Еженедельные спринты','Ежедневные стендапы','Внутренние ревью и плейтесты'])]:
    y=p(title,rx,y,rw,bold,5)
    for t in items:
        y=p(escape(t),rx,y,rw,small,2)
    y-=7
education_top=y
y=bar('ОБРАЗОВАНИЕ',rx,y,rw)
y=p('Бакалавриат: геймдизайн (B.A.)',rx,y,rw,bold,4)
y=p('University of Europe for Applied Sciences, Берлин',rx,y,rw,base,4)
y=p('2023 – 2027',rx,y,rw,base,7)
y=p('Специализация: прототипирование игр, технический дизайн, скриптинг уровней, системы взаимодействия',rx,y,rw,base,12)
y=bar('ЯЗЫКИ',rx,y,rw)
for t in ['Русский — Родной','Английский — B2 (IELTS 6.5)','Немецкий — A1.2']:
    y=p(t,rx,y,rw,base,5)
right_bottom=y+5
assert experience_bottom-education_top>=4,(experience_bottom,education_top)
y=bar('ИЗБРАННЫЕ ПРОЕКТЫ',x,education_top,lw)
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
