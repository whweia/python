# coding:utf-8
import requests
host = 'http://dev.opa.netcat.com.cn'
s = requests.session()


def document_list(s):
    dl_url = host + '/api/v1/document'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    r_dl = s.get(dl_url, headers=headers)
    return r_dl.json()

'''
if __name__ == "__main__":
    # 先登录
    login_url = host + '/admin/Auth/login'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

    body = {
        "username": "admin1305",
        "password": "netcat1305"
           }
    r_login = s.post(login_url, data=body, headers=headers)

    # 访问document_list接口
    doc = document_list()
    print(doc)
    print(type(doc))
    print(doc['status'])
'''
