import sys
import json
import sys
import threading
from PyQt5.QtWidgets import QApplication

sys.path.append(' .')


def judge_none(n):
    if n in ['none', 'None']:
        return ' is null'
    else:
        return ' = \'{}\''.format(n)


def get_json_list():
    with open('frist_set.json', 'rb') as f:
        params = json.load(f)
        x = params["re_list"]
    f.close()
    return x


def get_json_data():
    with open('frist_set.json', 'rb') as f:
        params = json.load(f)
        host = params['host']
        port = params["port"]
        user = params["user"]
        password = params["password"]
    f.close()
    return host, port, user, password


def process_json(data):
    with open('frist_set.json', 'rb') as f1:
        json_data = json.load(f1)
        f1.close()
    json_data["re_list"] = data
    with open('frist_set.json', "w") as f2:
        f2.write(json.dumps(json_data))
        f2.close()


def get_exit_data():
    with open('frist_set.json', 'rb') as f:  # 使用只读模型，并定义名称为f
        params = json.load(f)
        exit = params["exit"]
    f.close()
    return exit


def process_exit_json(int_exit):
    with open('frist_set.json', 'rb') as f1:
        json_data = json.load(f1)
        # print(json_data)
        f1.close()
    json_data["exit"] = int_exit
    with open('frist_set.json', "w") as f2:
        f2.write(json.dumps(json_data))
        f2.close()


def alignment(str1, space, align='center'):
    length = len(str1.encode('gb2312'))
    space = space - length if space >= length else 0
    if align == 'left':
        str1 = str1 + ' ' * space
    elif align == 'right':
        str1 = ' ' * space + str1
    elif align == 'center':
        str1 = ' ' * (space // 2) + str1 + ' ' * (space - space // 2)
    return str1


if __name__ == '__main__':
    print(get_json_list())
