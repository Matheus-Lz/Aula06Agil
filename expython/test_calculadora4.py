import unittest
from io import StringIO
from unittest.mock import patch
import sys

from calculadora4 import inserir_horarios_e_intervalo

class TestCalculadora(unittest.TestCase):
    @patch('builtins.input', side_effect=["8:30", "15:45", "01:00"])
    def test_calculadora_com_horas_e_minutos(self, mock_input):
        sys.stdout = StringIO()
        inserir_horarios_e_intervalo()
        output = sys.stdout.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, "Horas trabalhadas: 06 horas e 15 minutos")

if __name__ == '__main__':
    unittest.main()
