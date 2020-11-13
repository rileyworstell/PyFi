import unittest
from PyFi import PyFi


class TestPyFi(unittest.TestCase):

    def test_cash_flow(self):
        myPyFi = PyFi()
        myPyFi.monthly_income = 8000
        myPyFi.monthly_expenses = 5000
        myPyFi.calculate_cash_flow()
        self.assertEqual(myPyFi.calculate_cash_flow(),
                         myPyFi.monthly_income - myPyFi.monthly_expenses)


if __name__ == '__main__':
    unittest.main()
