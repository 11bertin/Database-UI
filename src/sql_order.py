import os
import sys

import pymysql

sys.path.append(os.getcwd())
from src.function import judge_none, alignment, get_json_list


class py_use_sql:
    def __init__(self, host, port, user, password):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=password, charset="utf8")
        self.cursor = self.conn.cursor()
        self.cursor.execute('use student;')
        self.index_list = ['id', 'name', 'age', 'major']
        self.length = 0

    @staticmethod
    def insert_order(infolist):
        msg = 'insert into stu values('
        new_list = []
        for i in range(4):
            if not infolist[i]:
                new_list.append('null')
            else:
                if i % 2 == 0:
                    new_list.append(infolist[i])
                else:
                    new_list.append('\'{}\''.format(infolist[i]))
        msg += ','.join(new_list)
        msg += ');'
        return msg

    def select_order(self, infolist):
        msg = 'select * from stu'
        msg_list = []
        if not infolist:
            return msg
        for i in range(4):
            if infolist[i]:
                if infolist[i].isdigit():
                    msg_list.append(self.index_list[i] + ' = ' + infolist[i])
                else:
                    msg_list.append(self.index_list[i] + judge_none(infolist[i]))
        if msg_list:
            msg += ' where {}'.format(' and '.join(msg_list))
        return msg

    def transform_text(self, tuple_msg):
        if not tuple_msg:
            return '查不到学生'
        self.length = len(tuple_msg) + 1
        text = ''
        for i in self.index_list:
            text += alignment(i, 10)
        text += '\n'
        for i in tuple_msg:
            text += '\n'
            for j in i:
                if j is None:
                    j = 'None'
                text += alignment(str(j), 10)
        return text

    def delete_order(self, infolist):
        self.cursor.execute(self.select_order(infolist))
        self.conn.commit()
        item = self.cursor.fetchall()
        msg_list = []
        for i in item:
            msg = 'delete from stu where id = {};'.format(i[0])
            msg_list.append(msg)
        return msg_list

    def select(self, infolist):

        self.cursor.execute(self.select_order(infolist))
        self.conn.commit()
        res = self.cursor.fetchall()
        return self.transform_text(res), res

    def insert(self, infolist):
        if not infolist[0]:
            return '请输入学生id'
        try:
            self.cursor.execute(self.insert_order(infolist))
            self.conn.commit()
            return '插入成功'
        except pymysql.err.IntegrityError:
            return 'id重复'

    def delete(self, infolist):
        list_find = self.delete_order(infolist)
        if not list_find:
            return '没有查找到此学生'
        for i in list_find:
            self.cursor.execute(i)
            self.conn.commit()
        return '删除成功'

    def revise_order(self, old_list):
        # print('这是revise')
        msg = []
        old_list = [str(i) for i in old_list]
        info_list = get_json_list()
        test_list = []
        if info_list[0] != old_list[0]:
            msg.append('update stu set id = {} WHERE id = {};'.format(info_list[0], old_list[0]))
            # self.cursor.execute(msg)
            # self.conn.commit()
        for i in range(1, 4):
            if info_list[i] and info_list[i] != old_list[i]:
                if i != 2:
                    test_list.append(self.index_list[i] + ' = \'' + info_list[i] + '\'')
                else:
                    test_list.append(self.index_list[i] + ' = ' + info_list[i])
        if test_list:
            test = 'update stu set {} WHERE id = {};'.format(' and '.join(test_list), info_list[0])
        msg.append(test)

        return msg

    def revise(self, old_list):
        msg = self.revise_order(old_list)
        for i in msg:
            self.cursor.execute(i)
            self.conn.commit()
        self.cursor.execute('select * from stu;')
        self.conn.commit()


if __name__ == '__main__':
    sql_sys = py_use_sql(host='127.0.0.1', port=3306, user='root', password='Biao0511')
