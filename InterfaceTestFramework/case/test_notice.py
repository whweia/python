# coding:utf-8
import unittest
import requests
import random
import string
from page.loginPage import Login
from page.noticePage import Notice
host = 'http://dev.opa.netcat.com.cn'


class Test_notice(unittest.TestCase):
    '''公告模块测试'''
    @classmethod
    def setUpClass(cls):
        # 先登录，可以加个修饰符
        cls.s = requests.session()
        cls.login = Login(cls.s).login()
        cls.notice = Notice(cls.s)  # 先实例化Notice类，因为下面都要用到
        cls.title = cls.rand_string(cls, 5)  # 生成随机的五位字符串

    def rand_string(self, length):
        # 生成随机字符串，length自定义字符串长度
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_notice_list(self):
        '''获取公告列表'''
        url = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url)
        j = result.json()["status"]  # json解析，获取状态的值，成功的话返回的status=ok
        print(j)
        self.assertEqual(j, "ok")  # 断言，判断两个值相等

    def test_notice_delete(self):
        '''输入一个存在的id，进行删除，删除成功'''
        url_del = host + '/api/v1/notice/delete'  # 删除公告的url
        url_list = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url_list)  # 先获取列表
        no_id = self.notice.get_notice_id(result)  # 然后获取id值
        delete_result = self.notice.noticeDel(url_del, no_id).json()["result"]  # 执行删除
        # print(delete_result.text)
        self.assertEqual(delete_result, "true")

    def test_notice_add_success(self):
        url = host + '/api/v1/notice/actAdd'
        result = self.notice.noticeAdd(url, self.title, self.title).json()["result"]
        self.assertEqual(result, "true")

    def test_notice_add_no_title(self):
        url = host + '/api/v1/notice/actAdd'
        result = self.notice.noticeAdd(url, "", self.title).json()["msg"]
        self.assertEqual(result, "标题不能为空")

    def test_notice_add_no_comment(self):
        url = host + '/api/v1/notice/actAdd'
        result = self.notice.noticeAdd(url, self.title, "").json()["msg"]
        self.assertEqual(result, "内容不能为空")

    def test_notice_add_no_title_no_comment(self):
        url = host + '/api/v1/notice/actAdd'
        result = self.notice.noticeAdd(url, "", "").json()["msg"]
        self.assertEqual(result, "标题不能为空")

    def test_notice_put_success(self):
        url = host + "/api/v1/notice/actUp"
        url_list = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url_list)  # 先获取列表
        no_id = self.notice.get_notice_id(result)  # 然后获取第一个id值
        result = self.notice.noticePut(url, no_id, self.title, self.title).json()["msg"]
        self.assertEqual(result, "修改成功！")

    def test_notice_put_no_title(self):
        url = host + "/api/v1/notice/actUp"
        url_list = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url_list)  # 先获取列表
        no_id = self.notice.get_notice_id(result)  # 然后获取第一个id值
        result = self.notice.noticePut(url, no_id, "", self.title).json()["msg"]
        self.assertEqual(result, "标题不能为空")

    def test_notice_put_no_title_no_content(self):
        url = host + "/api/v1/notice/actUp"
        url_list = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url_list)  # 先获取列表
        no_id = self.notice.get_notice_id(result)  # 然后获取第一个id值
        result = self.notice.noticePut(url, no_id, "", "").json()["msg"]
        self.assertEqual(result, "标题不能为空")

    def test_notice_put_no_content(self):
        url = host + "/api/v1/notice/actUp"
        url_list = host + "/api/v1/notice"  # 公告列表的url
        result = self.notice.noticeList(url_list)  # 先获取列表
        no_id = self.notice.get_notice_id(result)  # 然后获取第一个id值
        result = self.notice.noticePut(url, no_id, "self.title", "").json()["msg"]
        self.assertEqual(result, "内容不能为空")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()









