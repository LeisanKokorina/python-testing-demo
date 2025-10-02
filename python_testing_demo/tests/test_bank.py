import pytest
from app.bank import Account

def test_deposit_increases_balance():
    acc = Account("Alice", balance=100)
    acc.deposit(50)
    assert acc.balance == 150

@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_rejects_non_positive(amount):
    acc = Account("Bob")
    with pytest.raises(ValueError):
        acc.deposit(amount)

def test_withdraw_within_limit():
    acc = Account("Alice", balance=100, overdraft_limit=50)
    acc.withdraw(120)
    assert acc.balance == -20

def test_withdraw_exceeds_overdraft():
    acc = Account("Alice", balance=10, overdraft_limit=5)
    with pytest.raises(ValueError):
        acc.withdraw(20)

def test_transfer_type_guard():
    a = Account("Alice", balance=100)
    with pytest.raises(TypeError):
        a.transfer("not-an-account", 10)  # type: ignore[arg-type]

def test_deposit_rejects_non_number():
    acc = Account("Alice")
    with pytest.raises(TypeError):
        acc.deposit("not-a-number")

def test_withdraw_rejects_non_number():
    acc = Account("Alice", balance=50)
    with pytest.raises(TypeError):
        acc.withdraw("ten")

def test_withdraw_exactly_at_overdraft_limit():
    acc = Account("Alice", balance=0, overdraft_limit=10)
    acc.withdraw(10)   # allowed
    assert acc.balance == -10
