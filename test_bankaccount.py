import unittest
from bankaccount import BankAccount
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()
        self.account.deposit(100)
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)
    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
if __name__ == '__main__':
    unittest.main()