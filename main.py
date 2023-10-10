import PySimpleGUI as Sg
import pdf


class TelaRPG:
    def __init__(self):
        self.button = None
        self.values = None
        Sg.change_look_and_feel('DarkTeal4')
        # layout
        layout = [
            [Sg.Text('Informações Básicas', size=(23, 0), justification='center', pad=(15, 15), font='Arial 15 bold')],
            [Sg.Text('Nome: ', size=(6, 0)), Sg.Input(size=(30, 0), key='nome', background_color='white')],
            [Sg.Text('Raça: ', size=(6, 0)), Sg.Input(size=(30, 0), key='raca', background_color='white')],
            [Sg.Text('Classe: ', size=(6, 0)), Sg.Input(size=(30, 0), key='classe', background_color='white')],
            [Sg.Text('Nível: ', size=(6, 0)), Sg.Input(size=(30, 0), key='nivel', background_color='white')],
            [Sg.Text('Antecedente: ', size=(11, 0)), Sg.Input(size=(25, 0), key='antecedente', background_color='white')],
            [Sg.Text('Alinhamento: ', size=(11, 0)), Sg.Input(size=(25, 0), key='alinhamento', background_color='white')],
            [Sg.Text('Atributos', size=(22, 0), justification='center', pad=(15, 15), font='Arial 15 bold')],

            # Atributos

            [Sg.Text('Força: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='forca', background_color='white')],
            [Sg.Text('Destreza: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='destreza', background_color='white')],
            [Sg.Text('Constituição: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='constituicao', background_color='white')],
            [Sg.Text('Inteligência: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='inteligencia', background_color='white')],
            [Sg.Text('Sabedoria: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='sabedoria', background_color='white')],
            [Sg.Text('Carisma: ', size=(11, 0), justification='right'), Sg.Input(size=(5, 0), key='carisma', background_color='white')],
            [Sg.Text('', size=(1, 1))],

            [Sg.Button('Generate')],
            [Sg.Output(size=(36, 5))]

        ]

        # Janelas
        self.janela = Sg.Window("RPG Sheet Generator").layout(layout)
        # Extrair os dados da tela

    def start(self):
        # self.pdf_generator()
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            raca = self.values['raca']
            classe = self.values['classe']
            nivel = self.values['nivel']
            print(f'''
Nome: {nome}
Raça: {raca}
Classe: {classe}
Idade: {nivel}
''')
            print(self.button)
            pdf.generate(nome, raca, classe, nivel)


tela = TelaRPG()
tela.start()
