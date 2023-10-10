from reportlab.pdfgen import canvas


# from reportlab.lib.pagesizes import A5


def generate(nomepersonagem, nomejogador, raca, classe, nivel, antecedente, alinhamento,
             forca, destreza, constituicao, inteligencia, sabedoria, carisma):
    c = canvas.Canvas(f'{nomepersonagem}.pdf')
    c.drawString(100, 800, f'NOME DO PERSONAGEM: {nomepersonagem}')
    c.drawString(300, 800, f'NÍVEL: {nivel}')
    c.drawString(100, 780, f'NOME DO JOGADOR: {nomejogador}')
    c.drawString(300, 780, f'CLASSE: {classe}')
    c.drawString(100, 760, f'RAÇA: {raca}')
    c.drawString(300, 760, f'ALINHAMENTO: {alinhamento}')
    c.drawString(100, 740, f'ANTECEDENTE: {antecedente}')

    # ATRIBUTOS

    c.drawString(220, 700, 'ATRIBUTOS')
    c.drawString(120, 670, f'Força: {forca}')
    c.drawString(250, 670, f'Destreza: {destreza}')
    c.drawString(120, 650, f'Constituição: {constituicao}')
    c.drawString(250, 650, f'Inteligência: {inteligencia}')
    c.drawString(120, 630, f'Sabedoria: {sabedoria}')
    c.drawString(250, 630, f'Carisma: {carisma}')

    c.showPage()
    c.save()

# generate('Thiago', 'Humano', 'Estudante', '20')
