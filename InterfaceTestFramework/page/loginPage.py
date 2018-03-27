# coding:utf-8
import requests
host = 'http://dev.opa.netcat.com.cn'


class Login():
    def __init__(self, s):
        self.s = s

    def login(self, username="admin1305", password="netcat1305"):

        url_login = host + '/admin/Auth/login'

        headers = {
                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                  }

        body = {
                "username": username,
                "password": password
               }

        r = self.s.post(url_login, data=body, headers=headers)
        # print(r.text)
        return r

# if __name__ == "__main__":
#     s = requests.session()
#     l = Login(s)
#     l.login("admin1305", "netcat1305")

