# coding:utf-8
import requests
host = 'http://dev.opa.netcat.com.cn'


def login(s, username, password):
    login_url = host + '/admin/Auth/login'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
    body = {
        "username": username,
        "password": password
           }
    # s = requests.session()
    r = s.post(login_url, data=body, headers=headers)
    return r.text


def is_login_success(result):
    if "ok" in result:
        return True
    else:
        return False

# if __name__ == "__main__":
#     s = requests.session()
#     a = login(s,"admin1305", "netcat1305")
#     print(is_login_success(a))