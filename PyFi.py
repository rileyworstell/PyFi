from PyFi_prompt import prompt
import matplotlib.pyplot as plt
import numpy as np


class PyFi:

    def __init__(self):
        self.net_worth = 0
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.goal = 0
        self.years_to_goal = 0

    def calculate_cash_flow(self):
        self.monthly_cash_flow = self.monthly_income - self.monthly_expenses
        return self.monthly_cash_flow

    def calculate_yearly_savings(self):
        return self.monthly_cash_flow * 12

    def calculate_ten_year_savings(self):
        return self.monthly_cash_flow * 12 * 10

    def visualize_ten_year_savings(self):
        ycf = self.monthly_cash_flow * 12
        _, x_arr, y_arr = self.calculate_compounding(10, 0, ycf)
        print(x_arr)
        print(y_arr)
        plt.plot(x_arr, y_arr)
        plt.title('Savings over 10 years')
        plt.xlabel('Years')
        plt.ylabel('$ Ammount')
        plt.show()

    def calculate_compounding(self, years, interest_rate, yearly_savings):
        y_arr = []
        x_arr = range(years + 1)
        y = 0
        for i in range(years + 1):
            y = yearly_savings + (y * (1+interest_rate))
            y_arr.append(y)
        return y, x_arr, y_arr

    def calculate_years_invested(self, years):
        x = self.calculate_yearly_savings()
        y, _, _ = self.calculate_compounding(years, 0.07, x)
        return round(y, 2)

    def visualize_years_invested(self, years):
        x = self.calculate_yearly_savings()
        y, x_arr, y_arr = self.calculate_compounding(years, 0.07, x)
        plt.plot(x_arr, y_arr)
        plt.title('Savings over ' + str(years) +
                  ' years if invested at 7 percent compounded yearly')
        plt.xlabel('Years')
        plt.ylabel('$ Ammount')
        plt.show()

    def calculate_years_to_goal(self, goal):
        self.goal = goal
        x = self.calculate_yearly_savings()
        i = 0
        y = 0
        while i < goal:
            y += 1
            i = x + (i * 1.07)
            print("Year " + str(y), "$" + str(round(i, 2)), "is saved.")
        self.years_to_goal = y
        return y

    def income_and_expenses(self):
        self.monthly_income = input("Enter your monthly income after taxes\n")
        self.monthly_expenses = input("Enter your monthly expenses\n")
        if self.monthly_income.isdigit() and self.monthly_expenses.isdigit():
            self.monthly_income = int(self.monthly_income)
            self.monthly_expenses = int(self.monthly_expenses)
            print("Your monthly cashflow is ", "$" +
                  str(self.calculate_cash_flow()))
        else:
            print("You must enter numbers as your income.\n")

    def command_line(self):
        self.income_and_expenses()
        todo = ""
        while todo != "exit":
            todo = input(prompt)
            if todo == "1":
                print("\n$" + str(self.calculate_yearly_savings()),
                      "is your yearly savings")
            elif todo == "2":
                self.income_and_expenses()
            elif todo == "3":
                print("$" + str(self.calculate_ten_year_savings()),
                      " is your savings over 10 years!")
            elif (todo == "3v") or (todo == "3V"):
                self.visualize_ten_year_savings()
            elif todo == "4":
                y = input("How many years do you wish to invest over?\n")
                if y.isdigit:
                    y = int(y)
                    print("$" + str(self.calculate_years_invested(y)),
                          " is your invested savings over " + str(y) + " years!\n")
                else:
                    print("Number of years invested needs to be a number!\n")
            elif (todo == "4v") or (todo == "4V"):
                y = input("How many years do you wish to invest over?\n")
                if y.isdigit:
                    y = int(y)
                    self.visualize_years_invested(y)
                else:
                    print("Number of years invested needs to be a number!\n")
            elif todo == "5":
                y = input("What is your portfolio goal?\n")
                if y.isdigit:
                    y = int(y)
                    print(str(self.calculate_years_to_goal(y)),
                          " year(s) to reach your goal of $" + str(y) + "\n")
                else:
                    print("Portfolio goal needs to be a number!\n")
            elif todo == "00":
                print("Your monthly income is $" +
                      str(self.monthly_income))
                print("Your monthly expenses are $" +
                      str(self.monthly_expenses) + "\n")
            elif todo == "01":
                print("Your portfolio goal is $" +
                      str(self.goal))
                print("The number of years to reach this goal is " +
                      str(self.monthly_expenses) + "\n")
            else:
                if todo != "exit":
                    print("That was not a valid choice: \n")
