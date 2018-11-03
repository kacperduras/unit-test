import unittest

import example


class ExampleTest(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.example = example.Example(5, 5)

    def test_plus(self):
        result = self.example.plus()

        self.assertTrue(result, 10)
        pass

    def test_minus(self):
        result = self.example.minus()

        self.assertTrue(result, 0)
        pass

    def test_multiplication(self):
        result = self.example.multiplication()

        self.assertTrue(result, 25)
        pass

    def test_division(self):
        result = self.example.division()

        self.assertTrue(result, 1)
        pass


if __name__ == '__main__':
    unittest.main()
