#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/6/13 11:12

import unittest
from utils import common_api
from utils.config_utils import local_config


class GetAccessTokenTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.host

    def tearDown(self):
        pass

    def test_get_access_token(self):
        res_obj = common_api.get_access_token_api('client_credential',
                                                  'wxec83eaada223a9c8',
                                                  '1867d7f1cabb3bafae0b7304e8251a09')
        self.assertEqual(res_obj.json()['expires_in'], 7200, msg='验证是否获取access_token值')

    def test_appid_error(self):
        res_obj = common_api.get_access_token_api('client_credential',
                                                  'wxec83eaada223a9',
                                                  '1867d7f1cabb3bafae0b7304e8251a09')
        self.assertEqual(res_obj.json()['errcode'], 40013, msg='验证appid错误是否正常运行')

    def test_grant_type_error(self):
        res_obj = common_api.get_access_token_api('client_creden',
                                                  'wxec83eaada223a9c8',
                                                  '1867d7f1cabb3bafae0b7304e8251a09')
        self.assertEqual(res_obj.json()['errcode'], 40002, msg='验证grant错误是否正常运行')

    def test_secret_error(self):
        res_obj = common_api.get_access_token_api('client_credential',
                                                  'wxec83eaada223a9c8',
                                                  '1867d7f1cabb3bafa')
        self.assertEqual(res_obj.json()['errcode'], 40125, msg='验证AppSecret错误或者AppSecret不属于这个公众号')


if __name__ == "__main__":
    unittest.main()
