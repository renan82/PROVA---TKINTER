from tkinter import *
janela = Tk()
janela.title("  *** CONVERSOR DE CM PARA METROS *** ")
janela.geometry("800x600")
janela.configure(bg="#908279")

def converter():
    n1 = int(texto_input.get())
    conversao = n1 / 100
    resultado.configure(text=f"O número digitado convertido para METROS ficou em {conversao} metros!")

def cadastro1():
    nome = nome_input.get().upper()
    cadastro_concluido.configure(text=f"Parabéns {nome}, seu cadastro foi concluído!")

nome = Label(text="Digite seu nome para cadastro: ")
nome.grid(row=1, column=1)

nome_input = Entry(width=40)
nome_input.grid(row=1, column=2)

botao_cadastro = Button(janela, text=f"Clique para completar o cadastro", command=cadastro1)
botao_cadastro.grid(row=1, column=3)

cadastro_concluido = Label(text="", bg="#908279")
cadastro_concluido.grid(row=15, column=1)

texto = Label(text="Escolha um número: ")
texto.grid(row=4, column=2)

texto_input = Entry()
texto_input.grid(row=5, column=2)

resultado = Label(text="", bg="#908279", font="bold")
resultado.grid(row=13, column=2)

botao1 = Button(janela, text= "CLIQUE PARA CONVERTER", command=converter, bg="black", fg="white")
botao1.grid(row=8, column=2)

janela.mainloop()