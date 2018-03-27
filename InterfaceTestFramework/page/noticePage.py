# coding:utf-8
import requests
from page.loginPage import Login
host = 'http://dev.opa.netcat.com.cn'


class Notice():
    def __init__(self, s):  # 初始化先登录
        self.s = s
        login = Login(self.s)
        login.login()

    def noticeList(self, url):
        # url = host + "/api/v1/notice"
        result = self.s.get(url)
        # print(result.text)
        return result

    def noticeAdd(self, url, title, content):
        # url = host + "/api/v1/notice/actAdd"

        body = {
               "title": title,
               "content": content
               }
        result = self.s.post(url, data=body)
        return result

    def get_notice_id(self, list_result):
        # 获取公告id
        notice_id = list_result.json()["data"][0]["id"]  # 获取排在第一个的id值
        return notice_id

    def noticeDel(self, url, no_id):
        # no_id是公告的id
        # url = host + "/api/v1/notice/delete"
        body = {
                "id": no_id
                }
        result = self.s.delete(url, data=body)
        return result

    def noticePut(self, url, no_id, title, content):
        # url = host + "/api/v1/notice/actUp"
        par = {
            "id": no_id,
            "title": title,
            "content": content
        }
        result = self.s.put(url, data=par)
        return result


# if __name__ == "__main__":
#     ses = requests.session()
#     url_put = host + "/api/v1/notice/actUp"
#     n = Notice(ses)
#     result = n.noticePut(url_put, no_id="99", title="aaa", content="bbb")  # 获取公告列表页
#     print(result.text)
    # j = result.json()['data'][0]['id']
    # print(j)
    # print(result.text)
    #
    # get_id = n.get_notice_id(result)
    # print(get_id)

    # print(d.text)
    # l = Notice(s).noticeList().json()
    # j = l["total"]
    # print(j)

    # r = Notice(s).noticeAdd("yyo1", "yyo1")
    # print(r.text)
