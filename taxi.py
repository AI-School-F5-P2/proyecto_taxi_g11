import time
import logging

# Configuramos el sistema de logs
logging.basicConfig(level=logging.DEBUG, filename='registro.log', encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Designamos la clase Taxi
class Taxi:

    # Definimos el constructor.
    def __init__(self):
        self.en_movimiento = False
        self.tiempo_inicio = None
        self.tiempo_ultimo_cambio = None
        self.tarifa_parado = 2
        self.tarifa_movimiento = 5
        self.total = 0.0
        self.taximetro_iniciado = False
        self.logger = logging.getLogger(__name__)


    # Definimos el método que arranca el taximetro.
    def iniciar_taximetro(self):
        self.taximetro_iniciado = True
        self.total = 0.0
        self.tiempo_inicio = time.time()
        self.tiempo_ultimo_cambio = self.tiempo_inicio
        self.logger.info('La carrera ha comenzado')


    # Definimos el método que calcula la tarifa acumulada cuando nos ponemos en movimiento.
    def continuar_carrera(self):
        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.en_movimiento = True
            self.total += tiempo_transcurrido * self.tarifa_parado
            self.logger.info('El taxi continúa su recorrido')
            self.logger.debug(f"Se han añadido {(tiempo_transcurrido * self.tarifa_parado):.0f} céntimos al total")



    # Definimos el método que calcula la tarifa acumulada cuando nos detenemos.
    def pausar_carrera(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.en_movimiento = False
            self.total += tiempo_transcurrido * self.tarifa_movimiento
            self.logger.info('El taxi se ha detenido temporalmente')
            self.logger.debug(f"Se han añadido {(tiempo_transcurrido * self.tarifa_movimiento):.0f} céntimos al total")


    # Definimos el método que calcula el total de la tarifa al final de la carrera.
    def calcular_total(self):
        if self.en_movimiento:
            tiempo_pausa = time.time()
            tiempo_transcurrido = tiempo_pausa - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_pausa
            self.total += tiempo_transcurrido * self.tarifa_movimiento
            self.logger.info('La carrera ha terminado')
            self.logger.debug(f"Se han añadido {(tiempo_transcurrido * self.tarifa_movimiento):.0f} céntimos al total")
            self.logger.debug("La carrera ha durado {minutos:.0f} minutos y {segundos:.0f} segundos.".format(
                minutos = (tiempo_pausa - self.tiempo_inicio) // 60,
                segundos = (tiempo_pausa - self.tiempo_inicio) % 60))


        if not self.en_movimiento:
            tiempo_arrancar = time.time()
            tiempo_transcurrido = tiempo_arrancar - self.tiempo_ultimo_cambio
            self.tiempo_ultimo_cambio = tiempo_arrancar
            self.total += tiempo_transcurrido * self.tarifa_parado
            self.logger.info('La carrera ha terminado')
            self.logger.debug(f"Se han añadido {(tiempo_transcurrido * self.tarifa_parado):.0f} centimos al total")
            self.logger.debug("La carrera ha durado {minutos:.0f} minutos y {segundos:.0f} segundos.".format(
                minutos = (tiempo_arrancar- self.tiempo_inicio) // 60,
                segundos = (tiempo_arrancar- self.tiempo_inicio) % 60))


        euros =self.total/ 100
        self.en_movimiento = False
        self.taximetro_iniciado = False