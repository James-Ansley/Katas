from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime
from typing import Final, Self


class BankAccount:
    def __init__(self):
        self._transactions: Final[list[Transaction]] = []
        self._table = Table(
            separator=" || ",
            header=("Date", "Amount", "Balance"),
            formats=("{:%Y-%m-%d}", "{:<8}", "{:<8}"),
            header_formats=("{:<10}", "{:<8}", "{:<8}"),
        )

    def deposit(self, amount: int) -> None:
        transaction = Transaction.new_deposit(amount)
        self._transactions.append(transaction)

    def withdraw(self, amount: int) -> None:
        transaction = Transaction.new_withdrawal(amount)
        self._transactions.append(transaction)

    def print_statement(self) -> None:
        print(self._table.header())
        for date, amount, balance in self._transaction_history():
            row = self._table.row(date, amount, balance)
            print(row)

    def _transaction_history(self) -> Iterator[tuple[datetime, int, int]]:
        result = []
        running_total = 0
        for transaction in sorted(self._transactions, key=lambda t: t.date):
            running_total += transaction.amount
            trans_info = (transaction.date, transaction.amount, running_total)
            result.append(trans_info)
        return reversed(result)


@dataclass
class Transaction:
    date: datetime
    amount: int

    @classmethod
    def new_deposit(cls, amount) -> Self:
        if amount <= 0:
            raise ValueError("Transactions cannot be non-positive")
        return Transaction(datetime.now(), amount)

    @classmethod
    def new_withdrawal(cls, amount) -> Self:
        if amount <= 0:
            raise ValueError("Transactions cannot be non-positive")
        return Transaction(datetime.now(), -amount)


class Table:
    def __init__(
          self,
          *,
          separator: str,
          header: Iterable[str],
          formats: Iterable[str],
          header_formats: Iterable[str] = None,
    ):
        self.separator = separator
        self.column_headers = header
        self.formats = [fmt.format for fmt in formats]

        if header_formats is not None:
            self.header_formats = [fmt.format for fmt in header_formats]
        else:
            self.header_formats = self.formats

    def header(self):
        zipped_headers_and_fmt = zip(self.column_headers, self.header_formats)
        return self.separator.join(
            fmt(cell) for cell, fmt in zipped_headers_and_fmt
        )

    def row(self, *values):
        return self.separator.join(
            fmt(cell) for cell, fmt in zip(values, self.formats)
        )
