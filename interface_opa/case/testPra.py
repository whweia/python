# coding:utf-8

import requests
import unittest


class TestPra(unittest.TestCase):
    u''' 错误码页面的接口测试888'''
    def setUp(self):
        # setUp初始化，先登录
        self.url_login = 'http://dev.opa.netcat.com.cn/admin/Auth/login'  # 登录的接口(post)
        # 加self，就表示这个url可以全局使用，其他方法 也可以调用这个url
        self.headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
                        }
        self.s = requests.session()  # 用session保持会话

        body = {
                "username": "admin1305",
                "password": "netcat1305"
                }
        self.result = self.s.post(self.url_login, headers=self.headers, data=body)  # 发送登录请求

    def tearDown(self):
        pass

    def test_error(self):
        u'''获取错误码的接口测试'''
        self.url_error = 'http://dev.opa.netcat.com.cn/api/v1/errorcode'  # 获取错误码的列表(get)
        r_error = self.s.get(self.url_error, headers=self.headers)
        # print(r_error.text)

        result_error = r_error.json()
        id_error = result_error['data'][1]["id"]  # 获取第二个id的值
        print(id_error)
        self.assertEqual(id_error, 55)

if __name__ == "__main__":
    unittest.main()

