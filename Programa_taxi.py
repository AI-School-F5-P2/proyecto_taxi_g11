#! /usr/bin/env python 3
import time
import keyboard

# Designamos la clase Taxi
class Taxi:

    # Definimos el constructor.
    def __init__(self):
        self.en_movimiento = False
        self.tiempo_inicio = None
        self.tiempo_ultimo_cambio = None
        self.tarifa_parado = 2
        self.tarifa_movimiento = 5
        self.total = None
        self.carrera_iniciada = False

    # Definimos el método que arranca el taximetro.    
    def empezar_carrera(self):
        self.carrera_iniciada = True
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
            self.en_movimiento = False
            self.total += tiempo_transcurrido * self.tarifa_movimiento 
            euros = self.total /100
            print(f"El taxi se ha detenido temporalmente. Total acumulado {euros:.2f} euros.")

    
    # Definimos el método que calcula el total de la tarifa al final de la carrera.
    def calcular_total(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.en_movimiento = False
            self.total += tiempo_transcurrido * self.tarifa_movimiento 

        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = False
            self.total += tiempo_transcurrido * self.tarifa_parado

        euros =self.total/ 100       
        print(f"La carrera ha terminado. Total a pagar {euros:.2f} euros.")
    
    # Definimos el método que muestran las opciones cuando has iniciado la carrera.
    def mostrar_opciones(self):
        if self.carrera_iniciada:
            if self.en_movimiento:
                print("Opciones disponibles: ")
                print("Escribe 'p' cuando pares el taxi")
                print("Escribe 't' para terminar la carrera y obtener el monto total")
            else:
                print("Opciones disponibles: ")
                print("Escribe 'c' cuando continues el recorrido del taxi")
                print("Escribe 't' para terminar la carrera y obtener el monto total")
        else:
            print("Instrucciones de uso: ")
            print("Escribe 'i' para iniciar una nueva carrera")
            print("Escribe 's' para salir del programa")
        
# Definimos la función principal del programa que llamará a la clase y los métodos de taxi.
def main():
    taxi = Taxi()

    def presionando_enter(event):
        if taxi.carrera_iniciada






    print("Bienvenido a DigiTaxi")
    print("El programa para calcular las tarifas de tus carreras")


"""    while True:
        
        if not carrera_iniciada:
            taxi.mostrar_instrucciones()
            comando = input(">> ")
        
            if comando == "i":
                if not carrera_iniciada:
                    taxi.empezar_carrera()
                    carrera_iniciada = True
                else:
                    print("La carrera ya ha comenzado")
            elif comando == 's':
                print("Gracias por usar el programa. ¡Hasta la próxima!")
                break

            else:
                print("comando inválido. Por favor inténtalo de nuevo.")

        if carrera_iniciada:
            taxi.mostrar_opciones()
            comando = input(">")

            if taxi.en_movimiento:
                if comando == "p":
                    taxi.pausar_carrera()

                elif comando == "t":
                    taxi.calcular_total()
                    carrera_iniciada = False
                
                else:
                    print("comando inválido. Por favor inténtalo de nuevo.")
            
            else:
                if comando == "c":
                    taxi.continuar_carrera()
                
                elif comando == "t":
                    taxi.calcular_total()
                    carrera_iniciada = False

                else:
                    print("comando inválido. Por favor inténtalo de nuevo.")"""


if __name__ == "__main__":
    main()    # Esto hace que si queremos importar el código en otro programa omita la función main






