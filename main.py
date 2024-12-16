# Janela -> 500x500
# Titulo -> Conversor de Moedas
# Campos de selecionar moedas de origem e destino (campos de listas) com labels Selecione a moeda de origem
# Botao de "Converter"
# Lista de exibicao com os nomes das moedas

import customtkinter

# criar e configurara a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

# criar os botoes, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selcione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selcione a moeda de destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "MZN", "EUR", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "MZN", "EUR", "BTC"])

def converter_moeda():
    print("Converter moeda")
    

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dólar americano","MZN: Metical moçambicano","BTC: Bitcoin"] 
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()


# colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()
