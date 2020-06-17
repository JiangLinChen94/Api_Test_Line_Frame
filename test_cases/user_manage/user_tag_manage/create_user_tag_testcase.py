#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/6/13 11:27

import unittest
from utils import common_api
from utils.config_utils import local_config


class CreateUserTagTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.host

    def tearDown(self):
        pass

    def test_creat_tag(self):
        tokenid = common_api.get_access_token_value()
        res_obj = common_api.create_user_tag_api(tokenid, "alin104")
        self.assertEqual(res_obj.json()['tag']['name'], 'alin104', msg='验证添加标签成功')

    def test_tag_name_repetition(self):
        tokenid = common_api.get_access_token_value()
        res_obj = common_api.create_user_tag_api(tokenid, "alin100")
        self.assertEqual(res_obj.json()['errcode'], 45157, msg='验证标签名重复')

    def test_tag_name_overproof(self):
        tokenid = common_api.get_access_token_value()
        res_obj = common_api.create_user_tag_api(tokenid, "alin100阿斯蒂芬静安寺两地分居路撒地方sad发送京东方氨基酸的法律家数量的房间爱上大附件as两地分居撒来得及发牢骚地方阿萨德发送大")
        self.assertEqual(res_obj.json()['errcode'], 45158, msg='验证标签名超过30个字符')


if __name__ == "__main__":
    unittest.main()
