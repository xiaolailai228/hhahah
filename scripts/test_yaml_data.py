import pytest


def get_data():
    return [("111", "222")]

class TestReadYaml:
    @pytest.mark.parametrize("username,pwd", get_data())
    def test_read_yaml(self,username, pwd):
        print("username:", username)
        print("pwd:", pwd)