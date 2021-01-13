from tkinter import *
from PIL import ImageTk, Image

# Definindo a raiz do programa, o título e o ícone

root = Tk()
root.title('Wheels Base')
root.iconbitmap('imagens/favicon.ico')

#Criando uma frame para os botões do menu inicial

menu_inicial = LabelFrame(root, padx=5, pady=5)

#Criando os botões do menu inicial na frame criada

entrada_diaria = Button(menu_inicial, text='Diária', padx=29, pady=10)
cadastrar_mensalista = Button(menu_inicial, text='Mensalista', padx=16, pady=10)
pesquisar = Button(menu_inicial, text='Pesquisar', padx=19, pady=10)
pagamentos = Button(menu_inicial, text='Pagamentos', padx=11, pady=10)

#Modificando o tamanho da imagem do menu e a inserindo no programa

img_pneus = Image.open('imagens/imagem_menu.png')
img_pneus = img_pneus.resize((250, 250))
img_pneus = ImageTk.PhotoImage(img_pneus)
pneus = Label(image=img_pneus)

#Posicionando a imagem

pneus.grid(row=0, column=0, padx=30)

#Posicionando a frame na raiz do programa

menu_inicial.grid(row=0, column=1, pady=10, padx=10)

#Posicionando os botões na frame

entrada_diaria.grid(row=0, column=0)
cadastrar_mensalista.grid(row=1, column=0)
pesquisar.grid(row=2, column=0)
pagamentos.grid(row=3, column=0)

#Impedindo que o programa feche automaticamente colocando ele em loop

root.mainloop()