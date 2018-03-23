# coding:utf-8

import unittest
import requests
from page.loginPage import login
from page.documentPage import document_list


class TestDocument(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def test_doc_list(self):
        login(self.s, "admin1305", "netcat1305")  # 登录
        # print(l)
        doc = document_list(self.s)
        print(doc['status'])

if __name__ == "__main__":
    unittest.main()

