import unittest
from calculadora3 import validar_formato_hora, calcular_horas_trabalhadas
from datetime import datetime, timedelta

class TestCalculadora3(unittest.TestCase):

    def test_validar_formato_hora(self):
        self.assertTrue(validar_formato_hora("08:30"))
        self.assertTrue(validar_formato_hora("15:45"))
        self.assertFalse(validar_formato_hora("0830"))
        self.assertFalse(validar_formato_hora("8:30"))
        self.assertFalse(validar_formato_hora("25:30"))
        self.assertFalse(validar_formato_hora("08:75"))

    def test_calcular_horas_trabalhadas_inversao(self):
       
        hora_inicio = datetime.strptime("22:00", "%H:%M")
        hora_termino = datetime.strptime("06:00", "%H:%M")
        intervalo = timedelta(hours=1, minutes=0)  
        resultado = calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo)
        self.assertEqual(resultado, "7 horas e 0 minutos")

    def test_calcular_horas_trabalhadas_normal(self):
      
        hora_inicio = datetime.strptime("08:00", "%H:%M")
        hora_termino = datetime.strptime("17:00", "%H:%M")
        intervalo = timedelta(hours=1, minutes=0) 
        resultado = calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo)
        self.assertEqual(resultado, "8 horas e 0 minutos")

if __name__ == '__main__':
    unittest.main()
