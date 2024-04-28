from contextlib import redirect_stdout
from io import StringIO

from approvaltests import verify
from freezegun import freeze_time

from bank_account import BankAccount
from utils import test


@test
def a_new_bank_account_will_display_a_blank_statement():
    bank_account = BankAccount()
    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())


@test
def a_bank_account_will_display_a_single_deposit_in_its_statement():
    bank_account = BankAccount()

    with freeze_time("2012-01-10"):
        bank_account.deposit(123)

    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())


@test
def a_bank_account_will_display_a_single_withdrawal_in_its_statement():
    bank_account = BankAccount()

    with freeze_time("2012-01-14"):
        bank_account.withdraw(123)

    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())


@test
def a_bank_account_will_display_multiple_deposits_in_its_statement():
    bank_account = BankAccount()

    with freeze_time("2012-01-10"):
        bank_account.deposit(1000)
    with freeze_time("2012-01-13"):
        bank_account.deposit(2000)

    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())


@test
def a_bank_account_will_display_multiple_withdrawals_in_its_statement():
    bank_account = BankAccount()

    with freeze_time("2012-01-10"):
        bank_account.withdraw(1000)
    with freeze_time("2012-01-13"):
        bank_account.withdraw(2000)

    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())


@test
def a_bank_account_will_display_multiple_transactions_in_its_statement():
    bank_account = BankAccount()

    with freeze_time("2012-01-10"):
        bank_account.deposit(1000)
    with freeze_time("2012-01-13"):
        bank_account.deposit(2000)
    with freeze_time("2012-01-14"):
        bank_account.withdraw(500)

    with redirect_stdout(StringIO()) as f:
        bank_account.print_statement()
    verify(f.getvalue())
