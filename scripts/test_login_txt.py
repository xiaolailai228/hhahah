import os
import sys
sys.path.append(os.getcwd())

import pytest

from read_data.read_txt import read_txt


def get_data():
    arrs = []
    for data in read_txt():
        arrs.append(tuple(data.strip().split(",")))
    return arrs


class TestLoginTxt:
    @pytest.mark.parametrize("username,pwd", get_data())
    def test_txt(self,username,pwd):
        print("username:", username)
        print("pwd:", pwd)