class Category:
    def __init__(self, amount, form, date):
        self.amount = amount
        self.form = form
        self.date = date

class Income(Category):
    def __init__(self, amount, form, date):
        super().__init__(amount, form, date)

class Expense(Category):
    def __init__(self, amount, form, date):
        super().__init__(amount, form, date)
