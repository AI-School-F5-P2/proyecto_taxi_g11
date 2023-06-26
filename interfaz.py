from tkinter import *
import tkinter as tk
import time
import logging
import taxi as tx

# Designamos la clase TaxiApp para la interfaz gráfica
class TaxiApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DigiTaxi")
        self.taxi = tx.Taxi()


        # Definimos un Frame para las tarifas
        self.frame_tarifa =tk.Frame(self.window)
        self.frame_tarifa.pack()

        # Creamos el spinbox de tarifa parado
        self.tarifa_parado = tk.StringVar(value=self.taxi.tarifa_parado)
        self.label_tarifa_parado = tk.Label(self.frame_tarifa,
                                            text="Tarifa Parado:")
        self.label_tarifa_parado.grid(row=0, column=0)
        self.spinbox_tarifa_parado = tk.Spinbox(self.frame_tarifa,
                                                from_=0,
                                                to=30,
                                                textvariable=self.tarifa_parado)
        self.spinbox_tarifa_parado.grid(row=0, column=1)
        self.button_tarifa_parado = tk.Button(self.frame_tarifa,
                                              text="\N{check mark}",
                                              command=self.actualizar_tarifa_parado)
        self.button_tarifa_parado.grid(row=0, column=3)

        #Creamos el spinbox de tarifa en movimiento
        self.frame_tarifa_movimiento =tk.Frame(self.window)
        self.frame_tarifa_movimiento.pack()
        self.tarifa_movimiento = tk.StringVar(value=self.taxi.tarifa_movimiento)
        self.label_tarifa_movimiento = tk.Label(self.frame_tarifa,
                                            text="Tarifa Movimiento:")
        self.label_tarifa_movimiento.grid(row=1, column=0)
        self.spinbox_tarifa_movimiento = tk.Spinbox(self.frame_tarifa,
                                                from_=0,
                                                to=30,
                                                textvariable=self.tarifa_movimiento)
        self.spinbox_tarifa_movimiento.grid(row=1, column=1)
        self.button_tarifa_movimiento = tk.Button(self.frame_tarifa,
                                                  text="\N{check mark}",
                                                  command=self.actualizar_tarifa_movimiento)
        self.button_tarifa_movimiento.grid(row=1, column=3)

        # Mostramos el total acumulado
        self.label_costo = tk.Label(self.window, text="Costo de la carrera: €0.00")
        self.label_costo.pack()

        # Creamos los botones del taxímetro
        self.button_start = tk.Button(self.window,
                                      text="Inicio de carrera",
                                      command=self.iniciar_taximetro,
                                      width=20,
                                      height=1)
        self.button_start.pack()

        self.button_continue = tk.Button(self.window,
                                    text="Continuar",
                                    command=self.continuar_carrera,
                                    width=20,
                                    height=1,
                                    state=tk.DISABLED)
        self.button_continue.pack()

        self.button_pause = tk.Button(self.window,
                                 text="Pausar",
                                 command=self.pausar_carrera,
                                 width=20,
                                 height=1,
                                 state=tk.DISABLED)
        self.button_pause.pack()

        self.button_end = tk.Button(self.window,
                               text="Terminar carrera",
                               command=self.calcular_total,
                               width=20,
                               height=1,
                               state=tk.DISABLED)
        self.button_end.pack()

    # Creamos el método que llama a iniciar_taximetro de Taxi()
    def iniciar_taximetro(self):
        self.taxi.iniciar_taximetro()
        self.actualizar_interfaz()
        self.button_start.config(state=tk.DISABLED)
        self.button_continue.config(state=tk.ACTIVE)
        self.button_end.config(state=tk.ACTIVE)

    # Creamos el método que llama a continuar_carrera de Taxi()
    def continuar_carrera(self):
        self.taxi.continuar_carrera()
        self.actualizar_interfaz()
        self.button_continue.config(state=tk.DISABLED)
        self.button_pause.config(state=tk.ACTIVE)

    # Creamos el método que llama a pausar_carrera de Taxi()
    def pausar_carrera(self):
        self.taxi.pausar_carrera()
        self.actualizar_interfaz()
        self.button_continue.config(state=tk.ACTIVE)
        self.button_pause.config(state=tk.DISABLED)

    # Creamos el método que llama a calcular_total de Taxi()
    def calcular_total(self):
        self.taxi.calcular_total()
        self.actualizar_interfaz()
        self.button_start.config(state=tk.ACTIVE)
        self.button_continue.config(state=tk.DISABLED)
        self.button_pause.config(state=tk.DISABLED)
        self.button_end.config(state=tk.DISABLED)

    # Definimos el método que actualiza la tarifa en parado
    def actualizar_tarifa_parado(self):
        self.taxi.tarifa_parado = int(self.tarifa_parado.get())

    # Definimos el método que actualiza la tarifa en movimiento
    def actualizar_tarifa_movimiento(self):
        self.taxi.tarifa_movimiento = int(self.tarifa_movimiento.get())

    # Definimos el método que muestra el total en euros y céntimos
    def actualizar_interfaz(self):
        self.label_costo.config(text="Costo de la carrera: %d euros y %d céntimos" %(self.taxi.total//100, self.taxi.total%100))

    # Definimos el método que inicia la interfaz
    def iniciar_aplicacion(self):
        self.actualizar_interfaz()
        self.window.mainloop()



app = TaxiApp()
app.iniciar_aplicacion()
