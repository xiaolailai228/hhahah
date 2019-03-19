import yaml


def read_yaml(filename):
    filename = "./data/" + filename
    with open(filename, "r", encoding="utf-8") as f:
        return yaml.load(f)


if __name__ == '__main__':
    """期望格式：
    [("1111","333"),("aaa","bbbb"),("","")]

    问题：
        1. 读取出来的数据格式为字典，要的格式为列表
        2. 数据有3组数据，3个字典
        3. 读取指定的键名，获取值

    解决：
        1. 新建1个空列表，将读取来的数据添加到空内
        2. 使用字典中的values()方法获取所有的值
        3. 添加到列表中

    """
    # 新建 空列表 -->添加字典读取出来的数据
    arrs = []
    datas = read_yaml("data_login.yaml")
    for data in datas.values():
        arrs.append((data.get("username"), data.get("pwd")))
    print(arrs)
