from tkinter import *


class Application:
    def __init__(self, master=None):
        # Criando o widget principal e adicionando propriedades

        self.main_widget = Frame(master)
        self.main_widget.pack()
        self.msg = Label(self.main_widget, text="RPG Sheet Generator")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        # Recebimento de dados do usuário
        # Primeiro container

        self.default_font = ("Arial", "12")
        self.first_container = Frame(master)
        self.first_container["pady"] = 10
        self.first_container.pack()

        # Segundo container
        self.second_container = Frame(master)
        self.second_container["padx"] = 20
        self.second_container["pady"] = 10
        self.second_container.pack()

        # Terceiro container
        self.third_container = Frame(master)
        self.third_container["padx"] = 20
        self.third_container["pady"] = 10
        self.third_container.pack()

        # Quarto container
        self.four_container = Frame(master)
        self.four_container["pady"] = 10
        self.four_container.pack()

        # Quinto container
        self.five_container = Frame(master)
        self.five_container["pady"] = 60
        self.five_container.pack()

        # Label do primeiro container

        self.title = Label(self.first_container, text="Seção de preenchimento de ficha")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        # Entrada de dados para nome

        self.label_nome = Label(self.second_container, text="Nome", font=self.default_font)
        self.label_nome["padx"] = 5
        self.label_nome.pack(side=LEFT)

        self.name = Entry(self.second_container)
        self.name["width"] = 30
        self.name["font"] = self.default_font
        self.name.pack(side=LEFT)

        # Entrada de dados para Raça

        self.label_raca = Label(self.third_container, text="Raça", font=self.default_font)
        self.label_raca["padx"] = 5
        self.label_raca.pack(side=LEFT)

        self.raca = Entry(self.third_container)
        self.raca["width"] = 30
        self.raca["font"] = self.default_font
        self.raca.pack(side=LEFT)

        # Entrada de dados para Classe

        self.label_classe = Label(self.four_container, text="Classe", font=self.default_font)
        self.label_classe["padx"] = 5
        self.label_classe.pack(side=LEFT)

        self.classe = Entry(self.four_container)
        self.classe["width"] = 30
        self.classe["font"] = self.default_font
        self.classe.pack(side=LEFT)

        # Botão de gerar ficha

        self.button = Button(self.five_container, text="Generate", font="Arial")
        self.button["width"] = 15
        self.button.pack()

        # Criando um botão e adicionando propriedades e dentro do widget principal

        # self.exit = Button(self.main_widget)
        # self.exit["text"] = "Exit"
        # self.exit["font"] = ("Calibri", "10")
        # self.exit["width"] = 10
        # self.exit["command"] = self.main_widget.quit
        # # self.exit.bind("<Button-1>", self.change_text)
        # self.exit.pack(side=BOTTOM)

    # def change_text(self, event):
    #     if self.msg["text"] == "RPG Sheet Generator":
    #         self.msg["text"] = "O botão foi clicado"
    #     else:
    #         self.msg["text"] = "RPG Sheet Generator"


window = Tk()
Application(window)
window.mainloop()
