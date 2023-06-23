from tkinter import *
from PIL import Image, ImageTk
import time
import logging

root = Tk()
root.title("DigiTaxi")
root.resizable(1,1)

# Posición del titulo
miframe = Frame(root, width=700, height=600)
miframe.pack()
milabel = Label(miframe, text="Estamos listos", font=("Comic Sanz MS", 25)).place(x=240, y=25)

# Cargar la imagen utilizando PIL
imagen_pil = Image.open("taxi3-remov.png")

# Redimensionar la imagen
nuevo_tamano = (300, 200)
imagen_redimensionada = imagen_pil.resize(nuevo_tamano)

# Convertir la imagen en un objeto compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear el widget Label para mostrar la imagen
etiqueta_imagen = Label(root, image=imagen_tk)
etiqueta_imagen.pack()
etiqueta_imagen.place(x=200, y=70)  # Posición (50, 50) en píxeles

# Creacion de botones

from tkinter import Tk, Button
from Programa_taxi import Taxi

taxi_interfaz = Taxi()

boton_inicio = Button(root, text="Inicio de carrera", width=20, command= taxi_interfaz.iniciar_taximetro).place(x=265, y=270)
boton_salir = Button(root, text="Salir del programa", width=20).place(x=265, y=300)

# Agregar una etiqueta de dirección
'''direccion = "Calle Principal, Ciudad, País"
etiqueta_direccion = Label(root, text=direccion)
etiqueta_direccion.place(x=50, y=250)  # Posición (50, 250) en píxeles'''

root.mainloop()
