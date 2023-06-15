#! /usr/bin/env python 3
import time

class Taxi:
    def __init__(self):
        self.en_movimiento = False
        self.tiempo_inicio = None
        self.tarifa_parado = 2
        self.tarifa_movimiento = 5
        
    def empezar_carrera(self):
        self.total = 0
        self.tiempo_inicio = time.time()
        self.tiempo_ultimo_cambio = self.tiempo_inicio
        print("La carrera ha comenzado, ¡allá vamos!")


    
    def continuar_carrera(self):
        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = True
            self.total += tiempo_transcurrido * self.tarifa_parado
            euros = self.total /100
            print(f"El taxi continua su recorrido. Total acumulado {euros:.2f} euros.")



    def pausar_carrera(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.total += tiempo_transcurrido * self.tarifa_movimiento 
            euros = self.total /100
            print(f"El taxi se ha detenido temporalmente. Total acumulado {euros:.2f} euros.")

    
    
    def calcular_total(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.total += tiempo_transcurrido * self.tarifa_movimiento 

        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = True
            self.total += tiempo_transcurrido * self.tarifa_parado

        euros =self.total/ 100       
        

def main():

def mostrar_bienvenida():
    print("Bienvenido a DigiTaxi")
    print("El programa para calcular las tarifas de tus carreras")



