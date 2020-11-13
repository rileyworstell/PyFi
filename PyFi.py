class PyFi:

    def __init__(self):
        self.net_worth = 0
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0

    def calculate_cash_flow(self):
        self.monthly_cash_flow = self.monthly_income - self.monthly_expenses
        return self.monthly_cash_flow

    def calculate_yearly_savings(self):
        return self.monthly_expenses * 12

    def income_and_expenses(self):
        self.monthly_income = input("Enter your monthly income after taxes\n")
        self.monthly_expenses = input("Enter your monthly expenses\n")
        if self.monthly_income.isdigit() and self.monthly_expenses.isdigit():
            self.monthly_income = int(self.monthly_income)
            self.monthly_expenses = int(self.monthly_expenses)
            print("Your monthly cashflow is ", self.calculate_cash_flow())
        else:
            print("You must enter numbers as your income.\n")

    def command_line(self):
        self.income_and_expenses()
        todo = ""
        while todo != "exit":
            todo = input(
                "What would you like to do now? ('1' for yearly savings, '2' to reenter income and expenses, 'exit' to end program) \n")
            if todo == "1":
                print("$", self.calculate_yearly_savings(),
                      "is your yearly savings")
            elif todo == "2":
                self.income_and_expenses()
            else:
                if todo != "exit":
                    print("That was not a valid choice: \n")


if __name__ == '__main__':
    # This will be different for different functionalities of the application.
    # as of now the main portion of this application are to be fun through PyFi_cli.py
    myPyFi = PyFi()
    myPyFi.net_worth = 10000
    myPyFi.monthly_income = 8000
    myPyFi.monthly_expenses = 5000
    print(myPyFi.calculate_cash_flow())
