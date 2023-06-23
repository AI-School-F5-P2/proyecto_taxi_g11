from tkinter import *
import tkinter as tk
import time
import logging
from PIL import Image, ImageTk


class TaxiApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DigiTaxi")
        self.taxi = Taxi()
        self.taxi.logger.addHandler(InterfazHandler(self))

        self.label_tarifa = tk.Label(self.window, text="Tarifa: €0.00")
        self.label_tarifa.pack()

        self.label_costo = tk.Label(self.window, text="Costo de la carrera: €0.00")
        self.label_costo.pack()

        button_start = tk.Button(self.window, text="Inicio de carrera", command=self.iniciar_carrera, width=20, height=1)
        button_start.pack()

        button_continue = tk.Button(self.window, text="Continuar", command=self.continuar_carrera, width=20, height=1)
        button_continue.pack()

        button_pause = tk.Button(self.window, text="Pausar", command=self.pausar_carrera, width=20, height=1)
        button_pause.pack()

        button_end = tk.Button(self.window, text="Terminar carrera", command=self.terminar_carrera, width=20, height=1)
        button_end.pack()

        self.timer_running = False

    def iniciar_carrera(self):
        if not self.timer_running:
            self.taxi.iniciar_taximetro()
            self.timer_running = True
            self.update_timer()
            self.actualizar_interfaz()

    def continuar_carrera(self):
        if self.timer_running:
            self.taxi.continuar_carrera()
            self.actualizar_interfaz()

    def pausar_carrera(self):
        if self.timer_running:
            self.taxi.pausar_carrera()
            self.actualizar_interfaz()

    def terminar_carrera(self):
        if self.timer_running:
            self.taxi.calcular_total()
            self.timer_running = False
            self.actualizar_interfaz()

    def update_timer(self):
        if self.timer_running:
            self.taxi.actualizar_tiempo()
            self.window.after(1000, self.update_timer)

    def actualizar_interfaz(self):
        self.label_tarifa.config(text="Tarifa: €{:.2f} por segundo".format(self.taxi.tarifa_actual))
        self.label_costo.config(text="Costo de la carrera: €{:.2f}".format(self.taxi.costo_carrera))

    def iniciar_aplicacion(self):
        self.actualizar_interfaz()
        self.window.mainloop()

class InterfazHandler(logging.Handler):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def emit(self, record):
        msg = self.format(record)
        self.app.taxi.mensajes.append(msg)
        self.app.actualizar_interfaz()

class Taxi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.mensajes = []
        self.tarifa_en_movimiento = 0.05
        self.tarifa_detenido = 0.02
        self.tarifa_actual = 0.0
        self.costo_carrera = 0.0
        self.tiempo_inicio = 0
        self.tiempo_ultimo_cambio = 0
        self.en_movimiento = False

    def iniciar_taximetro(self):
        self.mensajes.append("La carrera ha comenzado, ¡allá vamos!")
        self.logger.info('La carrera ha comenzado')
        self.tarifa_actual = self.tarifa_detenido
        self.tiempo_inicio = time.time()
        self.tiempo_ultimo_cambio = self.tiempo_inicio
        self.en_movimiento = True

    def continuar_carrera(self):
        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = True
            self.costo_carrera += tiempo_transcurrido * self.tarifa_actual
            self.mensajes.append("El taxi continua su recorrido. Total acumulado: €{:.2f}".format(self.costo_carrera))
            self.logger.info('El taxi continúa su recorrido')
            self.logger.debug("Se han añadido €{:.2f} al total".format(tiempo_transcurrido * self.tarifa_actual))

    def pausar_carrera(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.en_movimiento = False
            self.costo_carrera += tiempo_transcurrido * self.tarifa_actual
            self.mensajes.append("El taxi se ha detenido temporalmente. Total acumulado: €{:.2f}".format(self.costo_carrera))
            self.logger.info('El taxi se ha detenido temporalmente')
            self.logger.debug("Se han añadido €{:.2f} al total".format(tiempo_transcurrido * self.tarifa_actual))

    def calcular_total(self):
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.tiempo_ultimo_cambio
        self.tiempo_ultimo_cambio = tiempo_actual
        self.costo_carrera += tiempo_transcurrido * self.tarifa_actual
        self.mensajes.append("La carrera ha terminado. Total a pagar: €{:.2f}".format(self.costo_carrera))
        self.en_movimiento = False
        self.tarifa_actual = 0.0
        self.costo_carrera = 0.0
        self.logger.info('La carrera ha terminado')

    def actualizar_tiempo(self):
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.tiempo_ultimo_cambio
        self.tiempo_ultimo_cambio = tiempo_actual
        if self.en_movimiento:
            self.tarifa_actual = self.tarifa_en_movimiento
        else:
            self.tarifa_actual = self.tarifa_detenido
        self.costo_carrera += tiempo_transcurrido * self.tarifa_actual

app = TaxiApp()
app.iniciar_aplicacion()



