import unittest
import time
import taxi as tx

MARGEN_ERROR = 0.1

class TestBasicos(unittest.TestCase):

    def test_empieza_en_cero(self):
        mitaxi = tx.Taxi()
        mitaxi.iniciar_taximetro()
        self.assertAlmostEqual(0, mitaxi.total, delta=MARGEN_ERROR)

    def test_cobra_bien_en_parado(self):
        TIEMPO_ESPERA = 4
        mitaxi = tx.Taxi()
        mitaxi.iniciar_taximetro()
        time.sleep(TIEMPO_ESPERA)
        mitaxi.continuar_carrera()
        self.assertAlmostEqual(TIEMPO_ESPERA * mitaxi.tarifa_parado, mitaxi.total, delta=MARGEN_ERROR)

    def test_cobra_bien_en_movimiento(self):
        TIEMPO_ESPERA = 4
        mitaxi = tx.Taxi()
        mitaxi.iniciar_taximetro()
        mitaxi.continuar_carrera()
        coste_inicio = mitaxi.total
        time.sleep(TIEMPO_ESPERA)
        mitaxi.pausar_carrera()
        self.assertAlmostEqual(TIEMPO_ESPERA * mitaxi.tarifa_movimiento, mitaxi.total - coste_inicio, delta=MARGEN_ERROR)

    def test_empieza_en_cero2(self):
        mitaxi = tx.Taxi()
        mitaxi.iniciar_taximetro()
        mitaxi.calcular_total()
        mitaxi.iniciar_taximetro()
        self.assertAlmostEqual(0, mitaxi.total, delta=MARGEN_ERROR)


if __name__ == '__main__':
    unittest.main()
