from dataclasses import dataclass

@dataclass
class Account:
    owner: str
    balance: float = 0.0
    overdraft_limit: float = 0.0  # how far below zero you can go

    def deposit(self, amount: float) -> None:
        _validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        _validate_amount(amount)
        new_balance = self.balance - amount
        if new_balance < -self.overdraft_limit:
            raise ValueError("Insufficient funds (overdraft limit reached)")
        self.balance = new_balance

    def transfer(self, to: "Account", amount: float) -> None:
        if not isinstance(to, Account):
            raise TypeError("to must be an Account")
        self.withdraw(amount)
        to.deposit(amount)


def _validate_amount(amount: float) -> None:
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if amount <= 0:
        raise ValueError("amount must be > 0")
