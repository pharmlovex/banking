import pytest
from main import BankOperation

def test_deposit():
    access = BankOperation("Access Bank", 123456)
    access.deposit(1000)
    assert access.balance == 1000

def test_withdraw_sufficient_funds():
    access = BankOperation("Access Bank", 123456)
    access.deposit(1000)
    access.withdraw(500)
    assert access.balance == 500

def test_withdraw_insufficient_funds():
    access = BankOperation("Access Bank", 123456)
    access.deposit(1000)
    access.withdraw(1500)
    assert access.balance == 1000

if __name__ == "__main__":
    pytest.main()