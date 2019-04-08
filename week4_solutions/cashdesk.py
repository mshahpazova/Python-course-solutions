class Bill:
    def __init__(self, amount):
        self.validate(amount)
        self.amount = amount
    def __int__(self):
      return int(self.amount)

    def __str__(self):
        return "A {0}$!".format(self.amount)
      
    def validate(self, amount):
        if not (type(amount) == int):
            raise TypeError("Invalid amount value")
        if (amount < 0):
            raise ValueError("Amount should be positive")

    def __repr__(self):
      return self.__str__(self)

      class BillBatch:
    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def total(self):
        my_sum = 0
        for bill in bills:
            my_sum += int(bill)
        return my_sum


values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

print(BillBatch.total(batch))


