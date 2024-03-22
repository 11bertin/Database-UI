# -*- coding: utf-8 -*-

import json
import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from UI.Ui_revise import Ui_MainWindow

sys.path.append(os.getcwd())
from src.function import process_json, get_json_list, process_exit_json, get_json_data
from src.sql_order import py_use_sql

login_info = get_json_data()


class sub(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(sub, self).__init__(parent)
        self.setupUi(self)
        self.sql_sys = py_use_sql(host=login_info[0],
                                  port=login_info[1],
                                  user=login_info[2],
                                  password=login_info[3])
        self.pushButton.clicked.connect(self.hide)
        self.re_list = get_json_list()
        # print(self.re_list, '这是sub')
        self.lineEdit.setText(str(self.re_list[0]))
        self.lineEdit_2.setText(self.re_list[1])
        self.lineEdit_3.setText('' if self.re_list[2] is None else str(self.re_list[2]))
        self.lineEdit_4.setText(self.re_list[3])
        self.list = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                     self.lineEdit_4.text()]
        self.enter = 0

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        # TODO: not implemented yet
        self.list = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                     self.lineEdit_4.text()]
        # res = self.revise_event
        if self.revise_event() == QMessageBox.Yes:
            process_json(self.list)
            self.sql_sys.revise(self.re_list)
            self.hide()

    def revise_event(self):
        return QMessageBox.question(self, '修改', '确认修改？',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = sub()
    ui.show()
    sys.exit(app.exec_())
