import parse_money_tracker_data
from category import *

def process_data():
    lines = parse_money_tracker_data.read_file()
    print(lines)
    expenses = []
    incomes = []
    for line in lines:
        if line[0] == '=':
            current_date = line[4:14]
            print(current_date)
        else:
            current_line = line.strip().split(', ')
            print(current_line)
            amount = float(current_line[0])
            form = current_line[1]
            if current_line[2] == 'New Expense':
                expense = Expense(amount, form, current_date)
                expenses.append(expense)
            else:
                income = Income(amount, form, current_date)
                incomes.append(income)
    print(incomes)
    print(expenses)


process_data()