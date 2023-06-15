#! /usr/bin/env python 3
import time

# Designamos la clase Taxi
class Taxi:

    # Definimos el constructor.
    def __init__(self):
        self.en_movimiento = False
        self.tiempo_inicio = None
        self.tarifa_parado = 2
        self.tarifa_movimiento = 5  

    # Definimos el método que arranca el taximetro.    
    def empezar_carrera(self):
        self.total = 0
        self.tiempo_inicio = time.time()
        self.tiempo_ultimo_cambio = self.tiempo_inicio
        print("La carrera ha comenzado, ¡allá vamos!")


    # Definimos el método que calcula la tarifa acumulada cuando nos ponemos en movimiento. 
    def continuar_carrera(self):
        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = True
            self.total += tiempo_transcurrido * self.tarifa_parado
            euros = self.total /100
            print(f"El taxi continua su recorrido. Total acumulado {euros:.2f} euros.")


    # Definimos el método que calcula la tarifa acumulada cuando nos detenemos.
    def pausar_carrera(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.total += tiempo_transcurrido * self.tarifa_movimiento 
            euros = self.total /100
            print(f"El taxi se ha detenido temporalmente. Total acumulado {euros:.2f} euros.")

    
    # Definimos el método que calcula el total de la tarifa al final de la carrera.
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
        print(f"La carrera ha terminado. Total a pagar {euros:.2f} euros.")
        
# Definimos la función principal del programa que llamará a la clase y los métodos de taxi.
def main():
    print("Bienvenido a DigiTaxi")
    print("El programa para calcular las tarifas de tus carreras")

if __name__ == "__main__":
    main()    # Esto hace que si queremos importar el código en otro programa omita la función main



