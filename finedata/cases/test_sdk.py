from class_method.finedata import finedata
import unittest
import requests
from log.log import Log
log = Log()

class Test(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.finedata = finedata(s)
    def test_login(self):
        d = {'userName': 'lihaiying', 'sign': '98C13D43E71B2E659F960F2C01BE6879ADB863EB4E28C293',
             'publicKey': '533d1a84-40ab-4e03-9183-05350f4af6e6',
             'type': 'DES', 'time': 1525938446167}
        result = self.finedata.login(d)
        self.assertEqual(result,True)
    def test_sdk(self):
        log.info('测试乐视视频提测条数')

        sdk_d = {'daterange': '', 'one_level_code': '0', 'two_level_code': '00', 'three_level_code': '001',
              'country_code': '', 'status': '', 'product_version': '', 'principal': ''}
        result = self.finedata.sdk(sdk_d)
        log.info('提测总条数是 %s' %result)
        self.assertGreater(result, 19)
        self.assertNotEqual(result,0)

if __name__ == '__main__':
    unittest.main()