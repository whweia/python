# coding:utf-8
from common.base import BasePage
opa_url = "http://dev.opa.netcat.com.cn/Admin/Auth/login"


class LoginPage(BasePage):
    """
    定位器，先把页面上的元素定位出来
    """
    # 密码登录模块
    username_loc = ("id", "username")  # 输入手机号
    password_loc = ("id", "password")  # 输入密码
    login_loc = ("id", "pulg")  # 点击登录
    # 点击忘记密码
    forget_password_loc = ("xpath", "//div[@id='#app']/div/div/section[3]/div/ul[2]/li/div[2]/span[2]/span")

    def input_username(self, username):
        """输入账号"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        self.click(self.login_loc)

    def click_forget_password(self):
        self.click(self.forget_password_loc)


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    my = LoginPage(driver)
    driver.get(opa_url)

    my.click_forget_password()

'''
    user = "admin1305"
    my.input_username(user)

    pws = "netcat1305"
    my.input_password(pws)

    login_loc = ("id", "pulg")
    my.click(login_loc)
'''

