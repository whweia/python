# coding:utf-8
import requests
from page.loginPage import Login
host = 'http://dev.opa.netcat.com.cn'


class Document():
    def __init__(self, s):
        self.s = s

    def document_list(self):
        url_doclist = host + '/api/v1/document'  # 接口指南列表的url
        login = Login(self.s)  # 上面导入了Login类,进行实例化
        login.login()  # 先进行登录，有默认的用户名密码了
        result = self.s.get(url_doclist)  # 发送接口指南列表的接口
        # print(result.text)
        return result.text


# if __name__ == "__main__":
    # s = requests.session()
    # r = Document(s)
    # r.document_list()
