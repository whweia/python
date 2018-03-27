# coding:utf-8
import unittest
import requests
from page.loginPage import Login


class Test_login(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.login = Login(self.s)

    def test_login_success(self):
        result = self.login.login("admin1305", "netcat1305")
        print(result.text)
        self.assertEqual(result.text, "ok")

    def test_login_error_username(self):
        result = self.login.login("13265000000", "netcat1305")
        print(result.text)
        self.assertTrue("账户未注册" in result.text)

    def test_login_error_password(self):
        result = self.login.login("admin1305", "netcat130")
        print(result.text)
        self.assertTrue("密码有误" in result.text)

if __name__ == "__main__":
    unittest.main()


