class Deposit:

    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate


    def interest(self):
        money = self.deposit
        for term in range(self.term):
            money = money * (self.rate + 1)
        interest = money - self.deposit

        return interest


deposit = Deposit(
    deposit=1000,
    term=2,
    rate=0.05,
)

interest = deposit.interest()
print(interest)
