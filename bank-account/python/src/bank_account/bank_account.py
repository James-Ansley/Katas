from datetime import datetime


class BankAccount:
    def __init__(self):
        self._transactions = {}

    def deposit(self, amount: int) -> None:
        today = datetime.today()
        self._transactions[today] = amount

    def withdraw(self, amount: int) -> None:
        today = datetime.today()
        self._transactions[today] = -amount

    def print_statement(self) -> None:
        balance = 0
        result = []
        for date, amount in sorted(self._transactions.items()):
            balance += amount
            result.append(_format_transaction(date, amount, balance))
        result.append("Date       || Amount || Balance")
        print("\n".join(reversed(result)))


def _format_transaction(date, amount, balance):
    return " || ".join((
        f"{date.strftime('%Y-%m-%d'):>10}",
        f"{amount:<6}",
        f"{balance:<7}",
    ))
