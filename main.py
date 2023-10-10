import PySimpleGUI as Sg
import pdf


class TelaRPG:
    def __init__(self):
        self.button = None
        self.values = None
        Sg.change_look_and_feel('DarkTeal4')
        # layout
        layout = [
            [Sg.Text('Nome: ', size=(6, 0)), Sg.Input(size=(30, 0), key='nome', background_color='white')],
            [Sg.Text('Raça: ', size=(6, 0)), Sg.Input(size=(10, 0), key='raca', background_color='white')],
            [Sg.Text('Classe: ', size=(6, 0)), Sg.Input(size=(10, 0), key='classe', background_color='white')],
            [Sg.Text('Idade: ', size=(6, 0)), Sg.Input(size=(10, 0), key='idade', background_color='white')],
            [Sg.Button('Generate')],
            [Sg.Output(size=(40, 20))]

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
            idade = self.values['idade']
            print(f'''
Nome: {nome}
Raça: {raca}
Classe: {classe}
Idade: {idade}
''')
            print(self.button)
            pdf.generate(nome, raca, classe, idade)


tela = TelaRPG()
tela.start()
