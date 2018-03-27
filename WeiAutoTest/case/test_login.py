# coding:utf-8

from selenium import webdriver
import unittest
from opa_page.loginpage import LoginPage, opa_url


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.logindriver = LoginPage(self.driver)
        self.driver.get(opa_url)

    def test_login_success(self):

        self.logindriver.input_username("admin1305")

        self.logindriver.input_password("netcat1305")

        self.logindriver.click_submit()

if __name__ == "__main__":
    unittest.main()
