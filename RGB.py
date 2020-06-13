#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *

color = (255, 255, 255)

def rgb(escala):
    return "#%02x%02x%02x" % escala

def R():
    
    lista_rojo = ()
    
    
    for i in range(0, 257):
        if i <= 256:
            combo_red['values'] = (lista_rojo)
            lista_rojo = lista_rojo + (i, )
        else:
            break


def G():
    

    lista_verde = ()
    
    
    for i in range(0, 257):
        if i <= 256:
            combo_green['values'] = (lista_verde)
            lista_verde = lista_verde + (i, )
        else:
            break
    


def B():
    
    lista_azul = ()
    
    for i in range(0, 257):
        if i <= 256:
            combo_blue['values'] = (lista_azul)
            lista_azul = lista_azul + (i, )
        else:
            break


def obten_escala():
    global color
    
    escala = (int(combo_red.get()), int(combo_green.get()), int(combo_blue.get()))
    color = escala

    rotulo_red.config(background = rgb(color))
    rotulo_green.config(background = rgb(color))
    rotulo_blue.config(background = rgb(color))
    root.config(bg = rgb(color))

root = Tk()
root.geometry("260x220")
root.title("Selector RGB")
root.resizable(0, 0)

rotulo_red = Label(root, text = "Rojo")
rotulo_red.pack(pady = 5)
combo_red = Combobox(root)
R()
combo_red.current(0)
combo_red.pack(pady = 5)

rotulo_green = Label(root, text = "Verde")
rotulo_green.pack(pady = 5)
combo_green = Combobox(root)
G()
combo_green.current(0)
combo_green.pack(pady = 5)

rotulo_blue = Label(root, text = "Blue")
rotulo_blue.pack(pady = 5)
combo_blue = Combobox(root)
B()
combo_blue.current(0)
combo_blue.pack(pady = 5)

btn_aplicar = Button(root)
btn_aplicar.config(text = "Aplicar", command = obten_escala)
btn_aplicar.pack(pady = 5)

root.config(bg = rgb(color))

root.mainloop()
