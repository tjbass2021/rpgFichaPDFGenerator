from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A5


def generate(nome, raca, classe, idade):
    cnv = canvas.Canvas(f"Ficha_Personagem-{nome}.pdf")
    cnv.drawString(40, 800, f'Nome: {nome}')
    cnv.drawString(40, 780, f'Raça: {raca}')
    cnv.drawString(40, 760, f'Classe: {classe}')
    cnv.drawString(40, 740, f'Idade: {idade}')
    cnv.save()


# generate('Thiago', 'Humano', 'Estudante', '20')
