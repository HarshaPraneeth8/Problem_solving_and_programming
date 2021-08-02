import unittest
import calc

#Creatinng testcases, in order to create test cases, first, we
#need to create a class

class Testcalc(unittest.TestCase):
    #Inherit test case from unittest
    def test_add(self):
        #The method should start with test+underscore(test_)
        self.assertEqual(calc.add(2,6),8)
        self.assertEqual(calc.add(3, 4), 7)
        self.assertEqual(calc.add(9,3),12)

    def test_mult(self):
        self.assertEqual(calc.multiply(2, 6), 12)
        self.assertEqual(calc.multiply(3, 4), 12)
        self.assertEqual(calc.multiply(9, 3), 27)

    def test_sub(self):
        self.assertEqual(calc.subtract(2, 6), -4)
        self.assertEqual(calc.subtract(3, 4), -1)
        self.assertEqual(calc.subtract(9, 3), 6)

    def test_exp(self):
        self.assertEqual(calc.exp(2,3), 8)
        self.assertEqual(calc.exp(3,4), 81)
        self.assertEqual(calc.exp(9,0), 1)

    def test_div(self):
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(1, 1), 1)
        self.assertEqual(calc.divide(1, 2), 0.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
#This basically means if we run the module directly
#then, run the code within the condition and the code here is unittest.main()
#Unittest.main() runs all of the tests
