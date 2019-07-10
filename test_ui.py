# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1638, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1641, 761))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1639, 759))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.first_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.first_widget.setEnabled(True)
        self.first_widget.setGeometry(QtCore.QRect(0, 0, 181, 761))
        self.first_widget.setStyleSheet("QWidget{\n"
"    background:#3C3F41;\n"
"    border-top:1px solid white;\n"
"    border-bottom:1px solid white;\n"
"    border-left:1px solid white;\n"
"    color: #A9B7C6;\n"
"}\n"
"    QLabel{border:none;\n"
"        font-size:23px;\n"
"        font-weight:700;\n"
"        border-bottom:1px solid white;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"    }   \n"
"QPushButton{\n"
"        border:none;\n"
"        font-size:17px;\n"
"        font-weight:700;\n"
"           border-top-left-radius:None;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"}\n"
"\n"
"QCalendarWidget QTableView \n"
"{\n"
"    background-color: #3C3F41;\n"
"    alternate-background-color: rgb(128, 128, 128);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton,#qt_calendar_yearbutton{\n"
"color: black; \n"
"font: 11pt Ariali; \n"
"\n"
"}\n"
"   QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"background-color:     #3C3F41;\n"
"}\n"
"QToolButton#qt_calendar_monthbutton {\n"
"padding-right: 20px;}\n"
"")
        self.first_widget.setObjectName("first_widget")
        self.left_label_2 = QtWidgets.QLabel(self.first_widget)
        self.left_label_2.setGeometry(QtCore.QRect(30, 170, 131, 31))
        self.left_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_2.setObjectName("left_label_2")
        self.left_label_4 = QtWidgets.QLabel(self.first_widget)
        self.left_label_4.setGeometry(QtCore.QRect(30, 290, 131, 31))
        self.left_label_4.setObjectName("left_label_4")
        self.btn_pic = QtWidgets.QPushButton(self.first_widget)
        self.btn_pic.setGeometry(QtCore.QRect(40, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.btn_pic.setFont(font)
        self.btn_pic.setStyleSheet("")
        self.btn_pic.setObjectName("btn_pic")
        self.btn_pic_2 = QtWidgets.QPushButton(self.first_widget)
        self.btn_pic_2.setGeometry(QtCore.QRect(40, 400, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,Helvetica,Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.btn_pic_2.setFont(font)
        self.btn_pic_2.setStyleSheet("")
        self.btn_pic_2.setObjectName("btn_pic_2")
        self.second_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.second_widget.setGeometry(QtCore.QRect(180, 0, 1461, 761))
        self.second_widget.setStyleSheet("    QWidget{\n"
"        color: #A9B7C6;\n"
"        background:    #2B2B2B;\n"
"        border:none;\n"
"    }\n"
"    QPushButton{\n"
"           border-top-right-radius:None;\n"
"        border:none;\n"
"        font-size:21px;\n"
"        font-weight:700;\n"
"        font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"    }\n"
"QLabel{border:none;}\n"
"QScrollArea{border:none;}")
        self.second_widget.setObjectName("second_widget")
        self.left_label_3 = QtWidgets.QLabel(self.second_widget)
        self.left_label_3.setGeometry(QtCore.QRect(130, 140, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left_label_3.setFont(font)
        self.left_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_3.setObjectName("left_label_3")
        self.left_label_5 = QtWidgets.QLabel(self.second_widget)
        self.left_label_5.setGeometry(QtCore.QRect(130, 210, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left_label_5.setFont(font)
        self.left_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_5.setObjectName("left_label_5")
        self.left_label_6 = QtWidgets.QLabel(self.second_widget)
        self.left_label_6.setGeometry(QtCore.QRect(130, 280, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left_label_6.setFont(font)
        self.left_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_6.setObjectName("left_label_6")
        self.left_label_7 = QtWidgets.QLabel(self.second_widget)
        self.left_label_7.setGeometry(QtCore.QRect(130, 350, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left_label_7.setFont(font)
        self.left_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_7.setObjectName("left_label_7")
        self.left_label_8 = QtWidgets.QLabel(self.second_widget)
        self.left_label_8.setGeometry(QtCore.QRect(130, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.left_label_8.setFont(font)
        self.left_label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.left_label_8.setObjectName("left_label_8")
        self.textEditNum = QtWidgets.QTextEdit(self.second_widget)
        self.textEditNum.setGeometry(QtCore.QRect(360, 140, 211, 61))
        self.textEditNum.setStyleSheet("    QTextEdit{\n"
"        color: #2B2B2B;\n"
"        background:    #A9B7C6;\n"
"        border:none;\n"
"    }")
        self.textEditNum.setObjectName("textEditNum")
        self.textEditLength = QtWidgets.QTextEdit(self.second_widget)
        self.textEditLength.setGeometry(QtCore.QRect(360, 210, 211, 61))
        self.textEditLength.setStyleSheet("    QTextEdit{\n"
"        color: #2B2B2B;\n"
"        background:    #A9B7C6;\n"
"        border:none;\n"
"    }")
        self.textEditLength.setObjectName("textEditLength")
        self.textEditCoeficient = QtWidgets.QTextEdit(self.second_widget)
        self.textEditCoeficient.setGeometry(QtCore.QRect(360, 280, 211, 61))
        self.textEditCoeficient.setStyleSheet("    QTextEdit{\n"
"        color: #2B2B2B;\n"
"        background:    #A9B7C6;\n"
"        border:none;\n"
"    }")
        self.textEditCoeficient.setObjectName("textEditCoeficient")
        self.textEditOffset = QtWidgets.QTextEdit(self.second_widget)
        self.textEditOffset.setGeometry(QtCore.QRect(360, 350, 211, 61))
        self.textEditOffset.setStyleSheet("    QTextEdit{\n"
"        color: #2B2B2B;\n"
"        background:    #A9B7C6;\n"
"        border:none;\n"
"    }")
        self.textEditOffset.setObjectName("textEditOffset")
        self.textEditSymbol = QtWidgets.QTextEdit(self.second_widget)
        self.textEditSymbol.setGeometry(QtCore.QRect(360, 420, 211, 61))
        self.textEditSymbol.setStyleSheet("    QTextEdit{\n"
"        color: #2B2B2B;\n"
"        background:    #A9B7C6;\n"
"        border:none;\n"
"    }")
        self.textEditSymbol.setObjectName("textEditSymbol")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.left_label_2.setText(_translate("MainWindow", "便捷计算器"))
        self.left_label_4.setText(_translate("MainWindow", " 其他功能"))
        self.btn_pic.setText(_translate("MainWindow", "暂未开发哦"))
        self.btn_pic_2.setText(_translate("MainWindow", "做个样子哦"))
        self.left_label_3.setText(_translate("MainWindow", "请输入运算字符："))
        self.left_label_5.setText(_translate("MainWindow", "请输入字符长度："))
        self.left_label_6.setText(_translate("MainWindow", "请输入运算系数："))
        self.left_label_7.setText(_translate("MainWindow", "请输入运算偏移量："))
        self.left_label_8.setText(_translate("MainWindow", "请输入有无符号："))

