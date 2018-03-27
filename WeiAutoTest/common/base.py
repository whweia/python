# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage(object):
    """
    对原生selenium框架进行二次封装
    """
    def __init__(self, driver):
        """
        启动浏览器参数化
        """
        # self.driver = webdriver.Firefox()
        self.driver = driver

    def open(self, url):
        """
        封装打开浏览器的方法，
        浏览器最大化
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator):
        """
        封装查找元素的方法，找不到元素给出提示，然后返回False；
        参数locator是元祖类型
        """
        try:
            element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
            return element
        except:
            print("NoSuchElement,Please find again!")
            return False

    def send_keys(self, locator, text):
        """
        send_keys方法，test为输入内容
        """
        self.find_element(locator).send_keys(text)

    def clear(self, locator):
        """
        清空输入框
        """
        self.find_element(locator).clear()

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def is_title_exit(self, locator):
        """
        判断页面title是否完全等于
        """
        try:
            title = WebDriverWait(self.driver, 15).until(EC.title_is(locator))
            return title
        except:
            print("不存在此title")
            return False

# 测试代码，封装完后要先进行测试，测试通过后其他模块调用
"""
if __name__ == "__main__":
    driver = webdriver.Firefox()
    my = BasePage(driver)  # 实例化
    # 测试 open 方法
    opa_url = "http://dev.opa_page.netcat.com.cn/Admin/Auth/login"
    my.open(opa_url)

    # 测试 find_element 方法
    # ele = ("id", "username")
    # my.find_element(ele)
    # print(my.find_element(ele))

    # 测试 send_keys 方法
    user_loc = ("id", "username")
    user = "admin1305"
    my.send_keys(user_loc, user)

    pws_loc = ("id", "password")
    pws = "netcat1305"
    my.send_keys(pws_loc, pws)

    # 测试 clear 方法
    # sleep(3)
    # clear_loc = ("id", "username")
    # my.clear(clear_loc)

    # 测试 click 方法
    click_loc = ("id", "pulg")
    my.click(click_loc)

"""






