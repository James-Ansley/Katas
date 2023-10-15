import re
from contextlib import redirect_stdout
from datetime import date
from io import StringIO

import pytest
from approvaltests import verify
from freezegun import freeze_time

from bank_account import BankAccount


class Case:
    def __init__(self, feature: str):
        self.feature = f"Feature: {feature}"
        self._arrange_description = None
        self._act_description = None
        self._asserts_description = None

    def arrange(self, description: str, value: object | None = None):
        if value is not None:
            self._arrange_description = "\n\n".join((description, str(value)))
        else:
            self._arrange_description = description

    def act(self, description: str, value: object | None = None):
        if value is not None:
            self._act_description = "\n\n".join((description, str(value)))
        else:
            self._act_description = description

    def asserts(self, description: str, value):
        self._asserts_description = "\n\n".join((description, str(value)))

    def __str__(self):
        output = "\n\n".join(
            feature for feature in (
                self.feature,
                self._arrange_description,
                self._act_description,
                self._asserts_description,
            )
            if feature is not None
        )
        # IDEs usually strip trailing spaces causing tests that include them
        # to always fail
        return re.sub(r" +\n", "\n", output)


def statement_of(account) -> str:
    stdout = StringIO()
    with redirect_stdout(stdout):
        account.print_statement()
    return stdout.getvalue()


def do_on(day, action):
    with freeze_time(date.fromisoformat(day)):
        action()


def test_empty_bank_account():
    case = Case("An empty bank account displays an empty table")
    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.asserts("An empty statement will be produced", statement_of(account))
    verify(case)


def test_bank_account_can_deposit():
    case = Case("An empty bank account can be deposited into")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act(f"Depositing 500 units on 2012-01-14")
    do_on("2012-01-14", lambda: account.deposit(500))

    case.asserts(
        "Will record the deposit in the statement",
        statement_of(account)
    )
    verify(case)


def test_bank_account_can_withdraw():
    case = Case("An empty bank account can be withdrawn from")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act("Withdrawing 500 units on 2012-01-14")
    do_on("2012-01-14", lambda: account.withdraw(500))

    case.asserts(
        "Will record the withdrawal in the statement",
        statement_of(account)
    )
    verify(case)


def test_multiple_deposits_are_recorded():
    case = Case("Multiple deposits are recorded")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act("Depositing 100 units on 2012-01-14 and 200 units on 2012-01-15")
    do_on("2012-01-14", lambda: account.deposit(100))
    do_on("2012-01-15", lambda: account.deposit(200))

    case.asserts(
        "Will record the transactions and display in reverse order",
        statement_of(account)
    )
    verify(case)


def test_multiple_withdrawals_are_recorded():
    case = Case("Multiple withdrawals are recorded")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act("Withdrawing 100 units on 2012-01-14 and 200 units on 2012-01-15")
    do_on("2012-01-14", lambda: account.withdraw(100))
    do_on("2012-01-15", lambda: account.withdraw(200))

    case.asserts(
        "Will record the transactions and display in reverse order",
        statement_of(account)
    )
    verify(case)


def test_multiple_withdrawals_and_deposits_are_recorded():
    case = Case("Multiple withdrawals and deposits are recorded")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act(
        "Depositing 1000 units on 2012-01-10, \n"
        "Depositing 2000 units on 2012-01-13, \n"
        "and Withdrawing 500 units on 2012-01-14"
    )
    do_on("2012-01-10", lambda: account.deposit(1000))
    do_on("2012-01-13", lambda: account.deposit(2000))
    do_on("2012-01-14", lambda: account.withdraw(500))

    case.asserts(
        "Will record the transactions and display in reverse order",
        statement_of(account)
    )
    verify(case)


def test_multiple_withdrawals_and_deposits_are_recorded_even_when_received_out_of_order():
    case = Case("Multiple withdrawals and deposits are recorded "
                "even when received out of order")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act(
        "Withdrawing 500 units on 2012-01-14, \n"
        "Depositing 1000 units on 2012-01-10, \n"
        "Depositing 2000 units on 2012-01-13, \n"
        "Depositing 3000 units on 2011-01-01, \n"
        "Withdrawing 500 units on 2011-01-02, \n"
    )
    do_on("2012-01-14", lambda: account.withdraw(500))
    do_on("2012-01-10", lambda: account.deposit(1000))
    do_on("2012-01-13", lambda: account.deposit(2000))
    do_on("2011-01-01", lambda: account.deposit(3000))
    do_on("2011-01-02", lambda: account.withdraw(500))

    case.asserts(
        "Will record the transactions and display in reverse order",
        statement_of(account)
    )
    verify(case)


def test_negative_amounts_cannot_be_deposited():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError):
        account.deposit(-1)


def test_negative_amounts_cannot_be_withdrawn():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError):
        account.withdraw(-1)


def test_zero_unit_amounts_cannot_be_deposited():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError):
        account.deposit(0)


def test_zero_unit_amounts_cannot_be_withdrawn():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError):
        account.withdraw(0)


def test_a_traction_error_will_not_affect_future_transactions():
    case = Case("Transactions that fail are ignored")

    case.arrange("Starting with an empty bank account")
    account = BankAccount()

    case.act(
        "Withdrawing 500 units on 2012-01-14, \n"
        "Depositing 1000 units on 2012-01-10, \n"
        "Depositing -5 units on 2012-01-13, \n"
        "Depositing 3000 units on 2011-01-01, \n"
        "Withdrawing 500 units on 2011-01-02, \n"
    )
    do_on("2012-01-14", lambda: account.withdraw(500))
    do_on("2012-01-10", lambda: account.deposit(1000))

    with pytest.raises(ValueError):
        do_on("2012-01-13", lambda: account.deposit(-5))
        
    do_on("2011-01-01", lambda: account.deposit(3000))
    do_on("2011-01-02", lambda: account.withdraw(500))

    case.asserts(
        "Will record the transactions and display in reverse order "
        "ignoring the erroneous transaction",
        statement_of(account)
    )
    verify(case)
