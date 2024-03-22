# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys
import threading
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
sys.path.append(' .')
from UI.Ui_data_interface import Ui_MainWindow


import src.sql_order
import src.revise
from src.function import get_json_data, process_json, get_json_list, get_exit_data

login_info = get_json_data()


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        self.sql_sys = src.sql_order.py_use_sql(host=login_info[0],
                                                port=login_info[1],
                                                user=login_info[2],
                                                password=login_info[3])
        super(MainWindow, self).__init__(parent)
        threading.Thread.__init__(self)
        self.setupUi(self)
        self.index_list = ['id', 'name', 'age', 'major']
        self.student_id = ''
        self.student_name = ''
        self.student_age = ''
        self.student_major = ''
        self.msg = 'select * from stu where id!=0'
        self.info = [self.student_id,
                     self.student_name,
                     self.student_age,
                     self.student_major]
        self.y = self.textEdit.pos().y()
        self.b = ''
        # self.b = src.revise.sub(self.info)

    @pyqtSlot()  # 查询
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        res, return_msg = self.sql_sys.select(self.info)
#         # print(self.sql_sys.select(self.info))
        self.verticalScrollBar.setMaximum(self.sql_sys.length * 15)
        self.verticalScrollBar.setSingleStep(self.sql_sys.length * 1.5)
        self.textEdit.setText(res)
#         # print(511)
        return return_msg

    @pyqtSlot()  # 插入
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.lineEdit.text():
            self.on_pushButton_clicked()
            res = self.sql_sys.insert(self.info)
            self.textEdit.setText(res)
            self.on_pushButton_clicked()
            self.textEdit.append('   ' + res)
        else:
            self.textEdit.setText('插入数据至少要输入id')

    @pyqtSlot()  # 删除
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO
        res = self.on_pushButton_clicked()
        if res != '查不到学生':
            if self.delete_event() == QMessageBox.Yes:
                res = self.sql_sys.delete(self.info)
                self.textEdit.setText(res)

    @pyqtSlot()  # 修改
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO
        res = self.on_pushButton_clicked()
#         # print(res)
        if not res:
            self.textEdit.append('请再次输入id进行修改(如果已输入请忽略)')
        if self.student_id:
            self.sub(list(res[0]))
            # # print(self.sub())
            # print('sub完毕')
            # self.on_pushButton_clicked()
            # self.textEdit.append('修改成功')
            # self.lineEdit.clear()
        # print('ii')

    @pyqtSlot(int)
    def on_verticalScrollBar_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.textEdit.move(0, self.y - value)

    def sub(self, data):
        process_json(data)
        # print('process执行完毕')
        self.b = src.revise.sub()
        self.b.show()
        # time.sleep(5)
#         # print(list(res[0]), get_json_list())

    def delete_event(self):
        return QMessageBox.question(self, '删除', '确定删除？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if reply == QMessageBox.Yes:
#         #     print(11)

    def update_info(self):
        try:
            while True:
                # todo
                time.sleep(0.3)
                self.student_id = self.lineEdit.text()
                self.student_name = self.lineEdit_3.text()
                self.student_age = self.lineEdit_2.text()
                self.student_major = self.lineEdit_4.text()
                self.info = [self.student_id,
                             self.student_name,
                             self.student_age,
                             self.student_major]
                if self.student_id or self.student_name or self.student_age or self.student_major:
                    self.pushButton_3.setEnabled(True)
                    # self.pushButton_4.setEnabled(True)
                else:
                    self.pushButton_3.setEnabled(False)
                if self.student_id:
                    self.pushButton_4.setEnabled(True)
                else:
                    self.pushButton_4.setEnabled(False)
        except RuntimeError:
            pass
            # print("关闭成功")


def run():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    t = threading.Thread(target=ui.update_info)
    t.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
    # data=((423, '423', 34, '2314'),)
#     # print(list(data[0]))
    # process_json(list(data[0]))
