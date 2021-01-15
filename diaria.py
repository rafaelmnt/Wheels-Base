from tkinter import *
from PIL import ImageTk, Image
import datetime

#Criando a raiz do programa com o título e o ícone

menu_diaria = Tk()
menu_diaria.title('Diária')
menu_diaria.iconbitmap('imagens/favicon.ico')

#Criando um método que lê o horário atual da máquina

agora = datetime.datetime.now()
horario = agora.strftime('%H:%M')

#Modificando o tamanho da imagem do menu e a inserindo no programa

img_relogio = Image.open('imagens/imagem_diaria.png')
img_relogio = img_relogio.resize((100, 100))
img_relogio = ImageTk.PhotoImage(img_relogio)
relogio = Label(image=img_relogio)

#Criando o título e a barra de pesquisa da placa

texto_placa = Label(menu_diaria, text='Placa:', pady=5, padx=2)
input_placa = Entry(menu_diaria, borderwidth=2)

#Criando o título e a barra de pesquisa do modelo

texto_modelo = Label(menu_diaria, text='Modelo:', pady=5, padx=2)
input_modelo = Entry(menu_diaria, borderwidth=2)

#Criando o título e a barra de pesquisa do horário de chegada

texto_entrada = Label(menu_diaria, text='Horário de Chegada', pady=8, padx=2)
input_entrada = Entry(menu_diaria, borderwidth=2)

#Inserindo o horário atual já na barra de pesquisa para facilitar para o usuário, ele pode alterar caso desejar

input_entrada.insert(0, horario)

#Criando o botão para cadastrar todas as informações

cadastro_diaria = Button(menu_diaria, text='Cadastrar')

#placa = Label(menu_diaria, text=agora.strftime("%d/%m/%Y %H:%M:%S"), pady=5, padx=20)

#Posicionando todos os títulos e as barras de pesquisas

texto_placa.grid(row=0, column=0)
input_placa.grid(row=1, column=0)

texto_modelo.grid(row=2, column=0)
input_modelo.grid(row=3, column=0)

texto_entrada.grid(row=4, column=0)
input_entrada.grid(row=5, column=0)

#Posicionando a imagem

relogio.grid(row=0, column=1, rowspan=4, padx=10, pady=5)

#Posicionando o botão

cadastro_diaria.grid(row=4, column=1, rowspan=2)

#Colocando o programa em loop para que ele não feche

menu_diaria.mainloop()