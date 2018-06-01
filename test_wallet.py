import pytest
from wallet import Wallet

def init_account():
    wallet = Wallet()
    assert wallet.balance == 0

def set_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def add_cash():
    wallet = Wallet(100)
    wallet.add_cash(100)
    assert wallet.balance == 200

def spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

