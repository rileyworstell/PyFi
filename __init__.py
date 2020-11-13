from PyFi import PyFi


if __name__ == '__main__':
    # This is just a basic example of the PyFi application
    myPyFi = PyFi()
    myPyFi.net_worth = 10000
    myPyFi.monthly_income = 8000
    myPyFi.monthly_expenses = 5000
    print(myPyFi.calculate_cash_flow())
