import unittest
from unittest import TestCase
from BankApp.Account import Account


class MyTestCase(unittest.TestCase):
    def Test_ThatBalance_Can_Be_Checked(self):
        frankAccount = Account(0,"franklin","1234",1)
        self.assertEqual(0, frankAccount.CheckBalance("1234"))




