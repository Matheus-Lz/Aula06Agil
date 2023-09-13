import unittest
from calculadora2 import validar_formato_hora, calcular_horas_trabalhadas
from datetime import datetime, timedelta

class TestCalculadora2(unittest.TestCase):

    def test_validar_formato_hora(self):
        self.assertTrue(validar_formato_hora("08:30"))
        self.assertTrue(validar_formato_hora("15:45"))
        self.assertFalse(validar_formato_hora("0830"))
        self.assertFalse(validar_formato_hora("8:30"))
        self.assertFalse(validar_formato_hora("25:30"))
        self.assertFalse(validar_formato_hora("08:75"))

    def test_calcular_horas_trabalhadas(self):
        hora_inicio = datetime.strptime("09:00", "%H:%M")
        hora_termino = datetime.strptime("17:30", "%H:%M")
        intervalo = timedelta(hours=1, minutes=30)  # 1 hora e 30 minutos de intervalo
        resultado = calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo)
        self.assertEqual(resultado, "7 horas e 30 minutos")

if __name__ == '__main__':
    unittest.main()

