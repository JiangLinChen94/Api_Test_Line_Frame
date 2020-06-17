import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, '..', 'config', 'config.ini')


class ConfigUtils(object):
    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path, encoding='utf-8')

    @property
    def host(self):
        url_value = self.cfg.get('default', 'hosts')
        return url_value

    @property
    def case_path(self):
        url_value = self.cfg.get('default', 'case_path')
        return url_value
    # 测试用例存放路径

    @property
    def report_path(self):
        report_path_value = self.cfg.get('default', 'report_path')
        return report_path_value

    @property
    def smtp_server(self):
        smtp_server_value = self.cfg.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.cfg.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):
        smtp_password_value = self.cfg.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.cfg.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.cfg.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.cfg.get('email', 'smtp_subject')
        return smtp_subject_value


local_config = ConfigUtils()


if __name__ == '__main__':
    current_path = os.path.abspath(os.path.dirname(__file__))
    print(local_config.host)
    print(local_config.case_path)