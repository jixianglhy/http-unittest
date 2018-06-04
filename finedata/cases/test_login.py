from class_method.finedata import finedata
import unittest
import requests
from log.log import Log
log = Log()
class Test(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.finedata = finedata(s)
    def test_login1(self):
        log.info('--测试正确的用户名，密码--')
        d = {'userName': 'lihaiying', 'sign': '98C13D43E71B2E659F960F2C01BE6879ADB863EB4E28C293',
             'publicKey': '533d1a84-40ab-4e03-9183-05350f4af6e6',
             'type': 'DES', 'time': 1525938446167}
        log.info('--输入的用户名，密码是：%s' %d)
        result = self.finedata.login(d)
        log.info('--登陆的结果是：%s' %result)
        self.assertEqual(result,True)

        log.info('---Pass----')

    def test_login2(self):
        log.info('--测试错误的用户名，密码--')
        d = {'userName': 'lihaiyin', 'sign': '98C13D43E71B2E659F960F2C01BE6879ADB863EB4E28C293',
             'publicKey': '533d1a84-40ab-4e03-9183-05350f4af6e6',
             'type': 'DES', 'time': 1525938446167}
        log.info('--输入的用户名，密码是：%s' %d)
        result = self.finedata.login(d)
        log.info('--登陆的结果是：%s' %result)
        self.assertEqual(result,False)
        log.info('---Pass----')


if __name__ == '__main__':
    unittest.main()

