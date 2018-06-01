class InsufficientAmount(Exception):
        pass

class InvalidAmount(Exception):
    pass


class Wallet(object):
    def __init__(self,inital_amount=0):
        self.balance = inital_amount

    def spend_cash(self,amount):
        if self.balance < amount:
            raise InsufficientAmount('not enough funds available')
        self.balance -= amount

    def add_cash(self,amount):
        if amount<0:
            raise InvalidAmount('please check the transaction')
        self.balance += amount 