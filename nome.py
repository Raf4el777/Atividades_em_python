import tkinter as tk

def saudacao():
    nome = entrada.get()
    label.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Aplicativo de Saudação")

label = tk.Label(janela, text="Digite seu nome:")
label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Saudar", command=saudacao)
botao.pack()

janela.mainloop()
