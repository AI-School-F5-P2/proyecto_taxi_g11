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
        self.taximetro_iniciado = False

    # Definimos el método que arranca el taximetro.
    def iniciar_taximetro(self):
        self.taximetro_iniciado = True
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
        self.taximetro_iniciado = False

    # Definimos el método que muestran las opciones cuando has iniciado la carrera.
    def mostrar_opciones(self):
        if self.taximetro_iniciado:
            if self.en_movimiento:
                print("Opciones disponibles: ")
                print("- Pulsa 'down' cuando pares temporalmente el taxi.")
                print("- Pulsa 'space' para terminar la carrera y obtener el total a pagar.")
                print("------------------------------------------------------------------------")
            else:
                print("Opciones disponibles: ")
                print("- Pulsa 'up' cuando continúes la marcha del taxi.")
                print("- Pulsa 'space' para terminar la carrera y obtener el total a pagar.")
                print("------------------------------------------------------------------------")
        else:
            print("Instrucciones de uso: ")
            print("- Pulsa 'enter' para iniciar una nueva carrera.")
            print("- Pulsa 'escape' para salir del programa.")
            print("------------------------------------------------------------------------")

# Definimos la función principal del programa que llamará a la clase y los métodos de taxi.
def main():

    taxi = Taxi()

    def presionando_enter(event):
        if not taxi.taximetro_iniciado:
            taxi.iniciar_taximetro()
        else:
            print("Comando no válido")
        taxi.mostrar_opciones()


    def presionando_up(event):
        if taxi.taximetro_iniciado:
            taxi.continuar_carrera()
        else:
            print("Comando no válido")
        taxi.mostrar_opciones()


    def presionando_down(event):
        if taxi.taximetro_iniciado:
            taxi.pausar_carrera()
        else:
            print("Comando no válido")
        taxi.mostrar_opciones()


    def presionando_space(event):
        if taxi.taximetro_iniciado:
            taxi.calcular_total()
        else:
            print("Comando no válido")
        taxi.mostrar_opciones()

    print("Bienvenido a DigiTaxi")
    print("El programa para calcular las tarifas de tus carreras")
    print(f"La tarifa en parado es de {taxi.tarifa_parado} céntimos por segundo.")
    print(f"La tarifa en movimiento es de {taxi.tarifa_movimiento} céntimos por segundo.")

    taxi.mostrar_opciones()

    keyboard.on_press_key('enter', presionando_enter)
    keyboard.on_press_key('up', presionando_up)
    keyboard.on_press_key('down', presionando_down)
    keyboard.on_press_key('space', presionando_space)

    keyboard.wait('esc')
    keyboard.unhook_all()

if __name__ == "__main__":
    main()    # Esto hace que si queremos importar el código en otro programa omita la función main






