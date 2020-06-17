import os
import unittest
from utils import HTMLTestReportCN
from utils.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join(current_path, local_config.case_path)
report_path = os.path.join(current_path, local_config.report_path)


class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = 'VX_Api_Test'
        self.description = 'newdream—test'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_testcase.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='alin')
        runner.run(all_suite)
        fp.close()
        return dir_path


if __name__ == '__main__':
    dir_path = RunAllCases().run()
    # EmailUtils('python自动化测试报告', dir_path).zip_send_mail()
