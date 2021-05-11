from django.db import models


class Deposit(models.Model):

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    interest = models.DecimalField(max_digits=12, decimal_places=4)


    def __str__(self):
        return f'Deposit {self.deposit} to term {self.term} years with rate {self.rate}; interest: {self.interest}'
