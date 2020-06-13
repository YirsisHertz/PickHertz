#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import colorchooser

color = "#FFFFFF"

def seleccion():

    global color

    try:
    
        color = colorchooser.askcolor(title = "Selecciona Tu Color")

        red_code.set(int(color[0][0]))
        green_code.set(int(color[0][1]))
        blue_code.set(int(color[0][2]))
        hexadecimal_code.set(color[1])

        rotulo_red.config(background = color[1])
        rotulo_green.config(background = color[1])
        rotulo_blue.config(background = color[1])
        rotulo_hexadecimal.config(background = color[1])
        root.config(bg = color[1])

    except:

        color = "#FFFFFF"

root = Tk()
root.geometry("330x160")
root.title("Paleta De Colores")
root.resizable(0, 0)

red_code = IntVar()
green_code = IntVar()
blue_code = IntVar()
hexadecimal_code = StringVar()

rotulo_red = Label(root, text = "Rojo", font = ("Montserrat", 10))
rotulo_red.grid(row = 0, column = 0, pady = 5, padx = 5)
entrada_red = Entry(root, textvariable = red_code).grid(row = 0, column = 1)

rotulo_green = Label(root, text = "Verde", font = ("Montserrat", 10))
rotulo_green.grid(row = 1, column = 0, pady = 5)
entrada_green = Entry(root, textvariable = green_code).grid(row = 1, column = 1)

rotulo_blue = Label(root, text = "Azul", font = ("Montserrat", 10))
rotulo_blue.grid(row = 2, column = 0, pady = 5)
entrada_blue = Entry(root, textvariable = blue_code).grid(row = 2, column = 1)

rotulo_hexadecimal = Label(root, text = "Hexadecimal", font = ("Montserrat", 10))
rotulo_hexadecimal.grid(row = 3, column = 0, padx = 10, pady = 5)
entrada_hexadecimal = Entry(root, textvariable = hexadecimal_code).grid(row = 3, column = 1, padx = 10)

btn_aplicar = Button(root)
btn_aplicar.config(text = "Aplicar", command = seleccion, width = 25)
btn_aplicar.grid(row = 4, column = 0, columnspan = 3, padx = 10)

root.mainloop()
