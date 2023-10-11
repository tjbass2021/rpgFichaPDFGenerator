from reportlab.pdfgen import canvas


# from reportlab.lib.pagesizes import A5


def generate(nomepersonagem, nomejogador, raca, classe, nivel, antecedente, alinhamento,
             forca, destreza, constituicao, inteligencia, sabedoria, carisma):
    nomepersonagem = str(nomepersonagem).upper()
    nomejogador = str(nomejogador).upper()
    raca = str(raca).upper()
    classe = str(classe).upper()
    antecedente = str(antecedente).upper()
    alinhamento = str(alinhamento).upper()

    c = canvas.Canvas(f'{nomepersonagem}.pdf')
    c.drawImage('./ded.png', 370, 720, 60, preserveAspectRatio=True)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(50, 800, 'DADOS')
    c.setFont('Helvetica', 12)
    c.drawString(50, 760, f'Nome do Personagem: {nomepersonagem}  Jogador: {nomejogador}')
    c.drawString(50, 740, f'Nível: {nivel}  Classe: {classe}')
    c.drawString(50, 720, f'Raça: {raca}')
    c.drawString(50, 700, f'Alinhamento: {alinhamento}  Antecedente: {antecedente}')

    c.setFont('Helvetica-Bold', 14)

    # ATRIBUTOS


    c.drawString(50, 660, 'ATRIBUTOS')
    c.setFont('Helvetica', 12)
    c.drawString(50, 620, f'Força: {forca}')
    c.drawString(180, 620, f'Destreza: {destreza}')
    c.drawString(50, 600, f'Constituição: {constituicao}')
    c.drawString(180, 600, f'Inteligência: {inteligencia}')
    c.drawString(50, 580, f'Sabedoria: {sabedoria}')
    c.drawString(180, 580, f'Carisma: {carisma}')

    # my_text = "Meu nome é Thiago\ntenho 29 anos"
    # textobject = c.beginText(50, 500)
    # for line in my_text.splitlines(False):
    #     textobject.textLine(line.rstrip())
    # c.drawText(textobject)

    c.showPage()
    c.save()

# generate('Thiago', 'Humano', 'Estudante', '20')
