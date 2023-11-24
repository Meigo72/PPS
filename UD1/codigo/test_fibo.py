# test_fibo.py
import unittest
from fibo import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_quinto_numero(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado[-1], 3, "El quinto número de la secuencia de Fibonacci debería ser 3")

if __name__ == "__main__":
    unittest.main()
