# coding:utf-8
import requests
import unittest
import json
import time
from log.log import Log

log = Log()
class finedata():
    def __init__(self,s):
        s = requests.session()
        self.s = s
    def login(self, d):
        url = 'http://lebi.letv.cn/session/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        '''
        d = {'userName': 'lihaiying', 'sign': '98C13D43E71B2E659F960F2C01BE6879ADB863EB4E28C293',
             'publicKey': '533d1a84-40ab-4e03-9183-05350f4af6e6',
             'type': 'DES', 'time': 1525938446167}
        '''
        try:
            r = self.s.post(url, data=d, headers=headers)
        except:
            print('不通')
            log.error('--登陆请求发送失败--')
            return
        log.info('--登陆请求发送成功！--')
        result = r.json()['success']
        log.info('--登陆结果是: %s' %result)
        print(result)
        return result
    def sdk(self,sdk_d):
        url = 'http://lebi.letv.cn/dq/testIde/data_request_info'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        '''
        sdk_d = {'daterange': '', 'one_level_code': '0', 'two_level_code': '00', 'three_level_code': '001',
              'country_code': '', 'status': '', 'product_version': '', 'principal': ''}
        '''
        try:
            r = self.s.post(url, data=sdk_d, headers=headers)
        except:
            log.error('查询请求失败！')
            return
        log.info('查询请求成功！')
        result = r.json()['total']
        log.info('数据总条数是： %s' %result)
        print(result)
        #log.info('总条数是 %s' %result)
        return  result

