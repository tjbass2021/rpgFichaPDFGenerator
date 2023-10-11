from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4


def generate(nomepersonagem, nomejogador, raca, classe, nivel, antecedente, alinhamento,
             forca, destreza, constituicao, inteligencia, sabedoria, carisma):
    nomepersonagem = str(nomepersonagem).upper()
    nomejogador = str(nomejogador).upper()
    raca = str(raca).upper()
    classe = str(classe).upper()
    antecedente = str(antecedente).upper()
    alinhamento = str(alinhamento).upper()

    style1 = ParagraphStyle('Estilo 1',
                            fontName='Helvetica',
                            backColor='#F1F1F1',
                            fontSize=14,
                            borderColor='#000000',
                            borderWidth=2,
                            borderPadding=(20, 20, 20),
                            leading=20,
                            alignment=0)

    c = canvas.Canvas(f'{nomepersonagem}.pdf', pagesize=A4)

    p1 = Paragraph(f'''
    <b>DADOS BÁSICOS</b><br/>
    <br/>
    <b>Nome:</b> {nomepersonagem}<br/>
    <b>Nome do jogador:</b> {nomejogador}<br/>
    <b>Nível:</b> {nivel}  <b>Classe:</b> {classe}
    <b>Raça:</b> {raca}<br/>
    <b>Alinhamento:</b> {alinhamento} <b>Antecedente:</b> {antecedente}<br/>
''', style1)

    p2 = Paragraph(f'''<b>ATRIBUTOS</b> <br/><br/>
    <b>Força:</b> {forca}<br/>
    <b>Destreza:</b> {destreza}<br/>
    <b>Constituição:</b> {constituicao}<br/>
    <b>Inteligência:</b> {inteligencia}<br/>
    <b>Sabedoria:</b> {sabedoria}<br/>
    <b>Carisma:</b> {carisma}''', style1)

    p2.wrapOn(c, 500, 100)
    p2.drawOn(c, 40, 350)
    p1.wrapOn(c, 500, 50)
    p1.drawOn(c, 40, 600)
    c.drawImage('./ded.png', 450, 700, 60, preserveAspectRatio=True)
    c.setFont('Helvetica-Bold', 28)
    c.drawString(50, 775, 'FICHA DE PERSONAGEM')

    c.save()

