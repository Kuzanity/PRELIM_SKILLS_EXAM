from test_unit import Temperature
import unittest

class Test_kelvin(unittest.TestCase):
    def celsius_testing(self):#celsius testing
        self.assertEqual(Temperature(celsius=21).kelvin,294.15)
    def faren_testing(self):#farenheit testing
        self.assertEqual(Temperature(farenheit=14).kelvin,263.15)
    def kelvin_testing(self):#kelvin testing
         self.assertEqual(Temperature(kelvin=40).kelvin,40)
    # def neg_args(self):#negative kelvin testing
    #     self.assertEqual(Temperature(kelvin=-40).kelvin,-40)
if __name__ == '__main__':
    unittest.main()