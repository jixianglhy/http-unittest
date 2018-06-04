# coding:utf-8
import unittest
import HTMLTestRunner
import os
import time

def all_case():
    case_dir = r'D:\pycharm\finedata\cases'
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
    testcase.addTest(discover)
    print(testcase)
    return testcase

if __name__ == '__main__':
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = 'D:\\pycharm\\finedata\\report\\'
    fp = open(report_path + now + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='finedata测试结果', description='两条测试用例')
    #runner = unittest.TextTestRunner()
    runner.run(all_case())
    fp.close()