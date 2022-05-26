#========== Micro Notes Edit ==========
#Criado por: CHFR
#Data: 04/01/2018
#Versão: 1.0
#Python 3
#======================================

from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import *

#inicia a janela.
main = Tk()
main.title("Micro Notes Edit")


#============ Funçoes ========

#Salva o documento
def salva():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Documentos de texto (*.txt)", "*.txt"),))
    textosaida = texto.get(0.0, END)
    file = open(arquivo, 'w')
    file.write(textosaida)
    file.close()

#Abre um arquivo
def abre():
    arquivo = filedialog.askopenfilename()
    file = open(arquivo, 'r')
    contents = file.read()
    texto.delete(0.0, END)
    texto.insert(0.0, contents)

#Mostra informaçoes sobre o programa
def sobre():
    informacao = """\n========== Micro Notes Edit ========== 
Criado por: CHFR 
Data: 04/01/2018 
Versão: 1.0
Python 3
======================================"""
    texto.insert(INSERT, informacao,END)


#============ Menu ==========
lm = Label(main, bg="orange")
lm.grid(row=0, column=1, sticky="W, E")
main.grid_columnconfigure(1, weight=1)                     #Cria uma label que sera o background dos botoes do menu .

#====== Botoes Menu =========

lbesp1 = Label(lm, bg="orange")
lbesp1.grid(row=0, column=0)                               #Cria uma label de espaçamento entre o logo e a borda.

iconome = PhotoImage(file="img/nomeico.png")
lbnome = Label(lm)
lbnome.config(image=iconome, highlightthickness=0, bd=0)   #Cria uma label que adiciona o logo.
lbnome.grid(row=0, column=1)

lbesp2 = Label(lm, bg="orange")
lbesp2.grid(row=0, column=2)                               #Cria uma label de espaçamento entre logo e salve.

icosalve = PhotoImage(file="img/saveicon.png")
btsalve = Button(lm, command=salva)
btsalve.config(image=icosalve, highlightthickness=0, bd=0) #configura botão salve e coloca uma imagem nele.
btsalve.grid(row=0, column=3)

lbesp3 = Label(lm, bg="orange")
lbesp3.grid(row=0, column=4)                              #Cria uma label de espaçamento entre salve e abre.

icoabre = PhotoImage(file="img/abreicon.png")
btabre = Button(lm, command=abre)
btabre.config(image=icoabre, highlightthickness=0, bd=0)  #configura botão abre e coloca uma imagem nele.
btabre.grid(row=0, column=5)

lbesp6 = Label(lm, bg="orange")
lbesp6.grid(row=0, column=6)                              #Cria uma label de espaçamento entre abre e sobre.

infico = PhotoImage(file="img/inficon.png")
btsobre = Button(lm, command=sobre)
btsobre.config(image=infico, highlightthickness=0, bd=0)  #configura botão sobre e coloca uma imagem nele.
btsobre.grid(row=0, column=7)

#=========== Texto =========

lbesp4 = Label(main)
lbesp4.grid(row=1,column=0)                              #Cria uma label de espaçamento entre o texto e o menu.

texto = Text(main)
texto.grid(row=2, column=1, sticky="N, E, S, W")         #Cria a caixa de texto e expande ela em todas as direções.

main.grid_rowconfigure(2, weight=1)                      #Redimenciona a linha da caixa de texto.

#========== Lateral ==========

#Mostra a scrollbar
scrollbar = Scrollbar(main)
scrollbar.grid(row=2, column=2, sticky="N, S")

#Configura a scrollbar
texto.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto.yview)

#========= Rodape ============

lbesp5 = Label(main)
lbesp5.grid(row=3,column=1)                             #Cria uma label de espaçamento entre a caixa de texto e o rodape.

rodape = Label(main, bg="orange")                       #Cria a label laranja no fim do programa.
rodape.grid(row=4,column=1, sticky="E, W")

#========== Final ============

main.geometry("660x490+100+80")                         #Define o tamanho inicial da janela.
main.mainloop()                                         #Faz a janela funcionar.
