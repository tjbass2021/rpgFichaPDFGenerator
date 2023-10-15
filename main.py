import PySimpleGUI as Sg
from pdf import generate


class TelaRPG:
    def __init__(self):
        self.button = None
        self.values = None
        Sg.change_look_and_feel('DarkTeal4')
        # layout
        layout = [
            [Sg.Text('Informações Básicas', size=(23, 0), justification='center', pad=(15, 15), font='Arial 15 bold')],
            [Sg.Text('Nome: ', size=(6, 0)), Sg.Input(size=(30, 0), key='nome', background_color='white')],
            [Sg.Text('Nome do Jogador: ', size=(10, 0)),
             Sg.Input(size=(26, 0), key='nomejogador', background_color='white')],
            [Sg.Text('Raça: ', size=(6, 0)), Sg.Input(size=(30, 0), key='raca', background_color='white')],
            [Sg.Text('Classe: ', size=(6, 0)), Sg.Input(size=(30, 0), key='classe', background_color='white')],
            [Sg.Text('Nível: ', size=(6, 0)), Sg.Input(size=(30, 0), key='nivel', background_color='white')],
            [Sg.Text('Antecedente: ', size=(11, 0)),
             Sg.Input(size=(25, 0), key='antecedente', background_color='white')],
            [Sg.Text('Alinhamento: ', size=(11, 0)),
             Sg.Input(size=(25, 0), key='alinhamento', background_color='white')],
            [Sg.Text('Atributos', size=(22, 0), justification='center', pad=(15, 15), font='Arial 15 bold')],

            # Atributos

            [Sg.Text('Força: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='forca', background_color='white')],
            [Sg.Text('Destreza: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='destreza', background_color='white')],
            [Sg.Text('Constituição: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='constituicao', background_color='white')],
            [Sg.Text('Inteligência: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='inteligencia', background_color='white')],
            [Sg.Text('Sabedoria: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='sabedoria', background_color='white')],
            [Sg.Text('Carisma: ', size=(11, 0), justification='right'),
             Sg.Input(size=(5, 0), key='carisma', background_color='white')],
            [Sg.Text('', size=(1, 1))],

            [Sg.Button('Clear'), Sg.Button('Generate'), Sg.Button('Exit', button_color='red')],
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
            nomejogador = self.values['nomejogador']
            alinhamento = self.values['alinhamento']
            antecedente = self.values['antecedente']
            # Atributos

            forca = self.values['forca']
            destreza = self.values['destreza']
            constituicao = self.values['constituicao']
            inteligencia = self.values['inteligencia']
            sabedoria = self.values['sabedoria']
            carisma = self.values['carisma']

            if self.button == 'Generate':
                generate(nome, nomejogador, raca, classe, nivel, antecedente,
                         alinhamento, forca, destreza, constituicao, inteligencia,
                         sabedoria, carisma)
                Sg.popup(f'{nome}.pdf gerado com sucesso!', title="Sucesso!")
                # Limpa os dados da janela
                self.janela['nome'].update('')
                self.janela['nomejogador'].update('')
                self.janela['raca'].update('')
                self.janela['classe'].update('')
                self.janela['nivel'].update('')
                self.janela['alinhamento'].update('')
                self.janela['antecedente'].update('')
                self.janela['forca'].update('')
                self.janela['constituicao'].update('')
                self.janela['destreza'].update('')
                self.janela['inteligencia'].update('')
                self.janela['sabedoria'].update('')
                self.janela['carisma'].update('')
            # except ValueError:
            #     pass
                # Sg.popup("Erro ao executar a função 'generate()", title="Erro!")

            if self.button == 'Exit':
                break
            if self.button == 'Clear':
                self.janela['nome'].update('')
                self.janela['nomejogador'].update('')
                self.janela['raca'].update('')
                self.janela['classe'].update('')
                self.janela['nivel'].update('')
                self.janela['alinhamento'].update('')
                self.janela['antecedente'].update('')
                self.janela['forca'].update('')
                self.janela['constituicao'].update('')
                self.janela['destreza'].update('')
                self.janela['inteligencia'].update('')
                self.janela['sabedoria'].update('')
                self.janela['carisma'].update('')


tela = TelaRPG()
tela.start()
