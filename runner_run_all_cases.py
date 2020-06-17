#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/6/13 13:38

import os
import time
import unittest
import HTMLTestRunner
from utils.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join(current_path, local_config.case_path)
report_path = os.path.join(current_path, local_config.report_path)


class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = 'VX_Api_Test'
        self.description = '测试微信公众号'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_testcase.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        html_report = os.path.join(local_config.report_path, 'result_%s.html' % now_time)
        file = open(html_report, 'wb')
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                                    title=self.title,
                                                    description=self.description,
                                                    )
        html_runner.run(all_suite)
        file.close()


if __name__ == '__main__':
    RunAllCases().run()
    # EmailUtils('python自动化测试报告', dir_path).zip_send_mail()
