from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
from functions import *


def generate(nomepersonagem, nomejogador, raca, classe, nivel, antecedente, alinhamento,
             forca, destreza, constituicao, inteligencia, sabedoria, carisma):
    nomepersonagem = str(nomepersonagem).upper()
    nomejogador = str(nomejogador).upper()
    raca = str(raca).upper()
    classe = str(classe).upper()
    antecedente = str(antecedente).upper()
    alinhamento = str(alinhamento).upper()
    forca = int(forca)
    destreza = int(destreza)
    constituicao = int(constituicao)
    inteligencia = int(inteligencia)
    sabedoria = int(sabedoria)
    carisma = int(carisma)

    # Bônus de atributo a partir da raça escolhida
    forca = aumentoatributoforca(raca, forca)
    destreza = aumentoatributodestreza(raca, destreza)
    constituicao = aumentoatributoconstituicao(raca, constituicao)
    inteligencia = aumentoatributointeligencia(raca, inteligencia)
    sabedoria = aumentoatributosabedoria(raca, sabedoria)
    carisma = aumentoatributocarisma(raca, carisma)

    # Cálculo de modificadores
    modforca = modificador(forca)
    moddestreza = modificador(destreza)
    modconstituicao = modificador(constituicao)
    modinteligencia = modificador(inteligencia)
    modsabedoria = modificador(sabedoria)
    modcarisma = modificador(carisma)

    # Cálculo de vida do personagem
    vida = calcvida(classe, modconstituicao)


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
    <b>Força:</b> ........... <b><font color="blue">({forca})</font></b> ..... 
    Modificador: <b><font color="red">[{modforca}]</font></b><br/>
    <b>Destreza:</b> ........ <b><font color="blue">({destreza})</font></b> ..... 
    Modificador: <b><font color="red">[{moddestreza}]</font></b><br/>
    <b>Constituição:</b> .... <b><font color="blue">({constituicao})</font></b> ..... 
    Modificador: <b><font color="red">[{modconstituicao}]</font></b><br/>
    <b>Inteligência:</b> .... <b><font color="blue">({inteligencia})</font></b> ..... 
    Modificador: <b><font color="red">[{modinteligencia}]</font></b><br/>
    <b>Sabedoria:</b> ....... <b><font color="blue">({sabedoria})</font></b> ..... 
    Modificador: <b><font color="red">[{modsabedoria}]</font></b><br/>
    <b>Carisma:</b> ......... <b><font color="blue">({carisma})</font></b> ..... 
    Modificador: <b><font color="red">[{modcarisma}]</font></b>''', style1)

    p2.wrapOn(c, 500, 100)
    p2.drawOn(c, 40, 350)
    p1.wrapOn(c, 500, 50)
    p1.drawOn(c, 40, 600)
    c.drawImage('./ded.png', 450, 700, 60, preserveAspectRatio=True)
    c.setFont('Helvetica-Bold', 28)
    c.drawString(50, 775, 'FICHA DE PERSONAGEM')

    c.save()
