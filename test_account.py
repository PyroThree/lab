from account import *


class Test:

    def setup_method(self):
        self.account = Account('John')

    def teardown_method(self):
        del self.account

    def test_init(self):
        assert self.account.get_name() == 'John'
        assert self.account.get_balance() == 0.00

    def test_deposit(self):
        assert self.account.deposit(100.00) == True
        assert self.account.deposit(-100.00) == False
        assert self.account.deposit(0.00) == False

    def test_withdraw(self):
        assert self.account.withdraw(0) == False
        assert self.account.withdraw(-100) == False
        assert self.account.withdraw(1.00) == False
