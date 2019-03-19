import os
import sys
sys.path.append(os.getcwd())

import pytest
from base.get_driver import get_driver
from page.page_login import PageLogin

# 获取数据
from read_data.read_yaml import read_yaml


def get_data():
    arrs = []
    datas = read_yaml("data_login.yaml")
    for data in datas.values():
        arrs.append((data.get("username"), data.get("pwd")))
    return arrs


class TestLogin:
    def setup_class(self):
        # 实例化 PageLogin
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        # 关闭driver
        self.login.driver.quit()

    @pytest.mark.parametrize("username,pwd", get_data())
    def test_login(self, username, pwd):
        # 调用登录方法
        self.login.page_login(username, pwd)
