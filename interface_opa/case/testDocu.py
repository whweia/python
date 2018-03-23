# coding:utf-8

import requests
import unittest

host = 'http://dev.opa.netcat.com.cn'
class TestDoc(unittest.TestCase):
    u'''接口列表页的接口测试999'''
    def setUp(self):
        # setUp初始化，先登录
        self.url_login = 'host + /admin/Auth/login'  # 登录的接口(post)
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

    def test_doc(self):
        u'''获取接口列表的接口测试'''
        self.url_doc = 'http://dev.opa.netcat.com.cn/api/v1/document'  # 获取接入指南的接口(get)
        r_doc = self.s.get(self.url_doc, headers=self.headers)  # 发送接入指南的接口(get)请求

        result_doc = r_doc.json()  # 获取返回,json解析
        id_doc = result_doc['data'][0]["id"]  # 获取第一个id的值
        print(id_doc)  # 打印id值
        self.assertEqual(id_doc, 91)  # 用获取的id值断言

if __name__ == "__main__":
    unittest.main()

