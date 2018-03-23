# coding:utf-8

import unittest
import requests
from page.loginPage import login, is_login_success


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def test_login01_success(self):
        a = login(self.s, "admin1305", "netcat1305")
        result = is_login_success(a)
        print(result)

        self.assertTrue(result)

    def test_login02_error_username(self):
        e = login(self.s, "admin13051", "netcat1305")
        result = is_login_success(e)
        print(result)

        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()