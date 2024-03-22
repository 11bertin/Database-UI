# -*- coding: utf-8 -*-


import json
import sys
import threading
import time

import pymysql
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

re_list = []


def judge_none(n):
    if n in ['none', 'None']:
        return ' is null'
    else:
        return ' = \'{}\''.format(n)



def get_json_data():
    with open('frist_set.json', 'rb') as f:
        params = json.load(f)
        host = params['host']
        port = params["port"]
        user = params["user"]
        password = params["password"]
    f.close()
    return host, port, user, password





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


login_info = get_json_data()


class Ui_ReviseWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 156)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 591, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 591, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 100, 256, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modify interface"))
        self.label.setText(_translate("MainWindow", "id"))
        self.label_2.setText(_translate("MainWindow", "name"))
        self.label_3.setText(_translate("MainWindow", "age"))
        self.label_4.setText(_translate("MainWindow", "major"))
        self.pushButton.setText(_translate("MainWindow", "Discard Modify"))
        self.pushButton_2.setText(_translate("MainWindow", "Relly Modify"))


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 347)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(69, 282, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(216, 282, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(363, 282, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 282, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 44, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 50, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(382, 10, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(382, 44, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 16, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 50, 181, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 16, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralWidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(660, 80, 16, 190))
        self.verticalScrollBar.setMaximum(190)
        self.verticalScrollBar.setSingleStep(19)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 630, 190))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 630, 531))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(True)
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.verticalScrollBar.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database interface"))
        self.pushButton.setText(_translate("MainWindow", "Query"))
        self.pushButton_2.setText(_translate("MainWindow", "Insert"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.pushButton_4.setText(_translate("MainWindow", "Modify"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "AGE"))
        self.label_3.setText(_translate("MainWindow", "NAME"))
        self.label_4.setText(_translate("MainWindow", "MAJOR"))


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        self.sql_sys = py_use_sql(host=login_info[0],
                                  port=login_info[1],
                                  user=login_info[2],
                                  password=login_info[3])
        super(MainWindow, self).__init__(parent)
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

    @pyqtSlot()  # Query
    def on_pushButton_clicked(self):
        res, return_msg = self.sql_sys.select(self.info)
        self.verticalScrollBar.setMaximum(self.sql_sys.length * 15)
        self.verticalScrollBar.setSingleStep(self.sql_sys.length * 15)
        self.textEdit.setText(res)
        return return_msg

    @pyqtSlot()  # Insert
    def on_pushButton_2_clicked(self):
        if self.lineEdit.text():
            self.on_pushButton_clicked()
            res = self.sql_sys.insert(self.info)
            self.textEdit.setText(res)
            self.on_pushButton_clicked()
            self.textEdit.append('   ' + res)
        else:
            self.textEdit.setText('At least enter ID when inserting')

    @pyqtSlot()  # Delete
    def on_pushButton_3_clicked(self):
        res = self.on_pushButton_clicked()
        if res != ():
            if self.delete_event() == QMessageBox.Yes:
                res = self.sql_sys.delete(self.info)
                self.textEdit.setText(res)

    @pyqtSlot()  # Modify
    def on_pushButton_4_clicked(self):
        res = self.on_pushButton_clicked()
        if not res:
            self.textEdit.append('Please enter the ID again to modify it (if it has been entered, please ignore it)')
        if self.student_id and res:
            self.lineEdit.clear()
            self.sub(list(res[0]))
        else:
            self.textEdit.setText('Please enter the ID correctly')

    @pyqtSlot(int)
    def on_verticalScrollBar_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        self.textEdit.move(0, self.y - value)

    def sub(self, data):
        global re_list
        re_list = data
        self.b = sub()
        self.b.show()

    def delete_event(self):
        return QMessageBox.question(self, 'Delete', 'Relly Delete？', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def update_info(self):
        try:
            while True:
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
                else:
                    self.pushButton_3.setEnabled(False)
                if self.student_id:
                    self.pushButton_4.setEnabled(True)
                else:
                    self.pushButton_4.setEnabled(False)
        except RuntimeError:
            pass




class sub(QMainWindow, Ui_ReviseWindow):
    def __init__(self, parent=None):
        super(sub, self).__init__(parent)
        self.setupUi(self)
        self.sql_sys = py_use_sql(host=login_info[0],
                                  port=login_info[1],
                                  user=login_info[2],
                                  password=login_info[3])
        self.pushButton.clicked.connect(self.hide)
        global re_list
        self.re_list = re_list
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
        if self.revise_event() == QMessageBox.Yes:
            global re_list
            re_list = self.list
            self.sql_sys.revise(self.re_list)
            self.hide()

    def revise_event(self):
        return QMessageBox.question(self, 'Modify', 'Relly Modify？',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


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
            return 'No data found'
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
            return 'Please enter ID'
        try:
            self.cursor.execute(self.insert_order(infolist))
            self.conn.commit()
            return 'Insert Successful'
        except pymysql.err.IntegrityError:
            return 'ID duplicate'

    def delete(self, infolist):
        list_find = self.delete_order(infolist)
        if not list_find:
            return 'No data found'
        for i in list_find:
            self.cursor.execute(i)
            self.conn.commit()
        return 'Delete Successful'

    def revise_order(self, old_list):
        msg = []
        old_list = [str(i) for i in old_list]
        global re_list
        info_list = re_list
        test_list = []
        if info_list[0] != old_list[0]:
            msg.append('update stu set id = {} WHERE id = {};'.format(info_list[0], old_list[0]))
        for i in range(1, 4):
            if info_list[i] and info_list[i] != old_list[i]:
                if i != 2:
                    test_list.append(self.index_list[i] + ' = \'' + info_list[i] + '\'')
                else:
                    test_list.append(self.index_list[i] + ' = ' + info_list[i])
        test = ''
        if test_list:
            test = 'update stu set {} WHERE id = {};'.format(' and '.join(test_list), info_list[0])
        if test:
            msg.append(test)
        return msg

    def revise(self, old_list):
        msg = self.revise_order(old_list)
        for i in msg:
            self.cursor.execute(i)
            self.conn.commit()
        self.cursor.execute('select * from stu;')
        self.conn.commit()


def run():
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    t = threading.Thread(target=ui.update_info)
    t.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
