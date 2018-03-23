# coding:utf-8

import unittest
from commen import HTMLTestRunner_jpg
import os

filePath = os.path.dirname(__file__)  # 先找到当前文件所在的文件夹

casePath = os.path.join(filePath, "case")  # 拼接出case所在的路径

reportPath = os.path.join(filePath, "report")  # 拼接出report所在的路径

# 生成的测试报告路径
resultPath = os.path.join(reportPath, "result.html")  # result.html放在report文件夹中

# discover去CasePath中找以test开头的用例
discover = unittest.defaultTestLoader.discover(casePath, "test*.py")

# print(discover)

fb = open(resultPath, "wb")  # wb 写，就是每次先清空了，然后再写进去
runner = HTMLTestRunner_jpg.HTMLTestRunner(fb, verbosity=2,
                                           title="测试报告",
                                           description="测试报告描述")

runner.run(discover)
