# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameInfo1.ui'
#
# Created: Mon Sep 15 17:10:57 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GameInfo1(object):
    def setupUi(self, GameInfo1):
        GameInfo1.setObjectName(_fromUtf8("GameInfo1"))
        GameInfo1.resize(222, 241)
        self.label_25 = QtGui.QLabel(GameInfo1)
        self.label_25.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.layoutWidget = QtGui.QWidget(GameInfo1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 22))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.layoutWidget_2 = QtGui.QWidget(GameInfo1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 60, 201, 164))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_29 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.horizontalLayout.addWidget(self.lineEdit_29)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_24 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.horizontalLayout_2.addWidget(self.lineEdit_24)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_25 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.horizontalLayout_3.addWidget(self.lineEdit_25)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.lineEdit_26 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.horizontalLayout_4.addWidget(self.lineEdit_26)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_5.addWidget(self.lineEdit_6)
        self.lineEdit_27 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.horizontalLayout_5.addWidget(self.lineEdit_27)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_6.addWidget(self.lineEdit_7)
        self.lineEdit_28 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.horizontalLayout_6.addWidget(self.lineEdit_28)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_24 = QtGui.QLabel(GameInfo1)
        self.label_24.setGeometry(QtCore.QRect(90, 40, 54, 12))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_8.setBuddy(self.lineEdit_3)
        self.label_7.setBuddy(self.lineEdit_4)
        self.label_3.setBuddy(self.lineEdit_5)
        self.label_4.setBuddy(self.lineEdit_6)
        self.label_5.setBuddy(self.lineEdit_7)

        self.retranslateUi(GameInfo1)
        QtCore.QMetaObject.connectSlotsByName(GameInfo1)

    def retranslateUi(self, GameInfo1):
        GameInfo1.setWindowTitle(_translate("GameInfo1", "游戏信息", None))
        self.label_25.setText(_translate("GameInfo1", "   2号", None))
        self.label.setText(_translate("GameInfo1", "回合数    ：", None))
        self.label_2.setText(_translate("GameInfo1", "回合用时  ：", None))
        self.label_8.setText(_translate("GameInfo1", "资源数    ：", None))
        self.label_7.setText(_translate("GameInfo1", "基地生命  ：", None))
        self.label_3.setText(_translate("GameInfo1", "空中单位数：", None))
        self.label_4.setText(_translate("GameInfo1", "水面单位数：", None))
        self.label_5.setText(_translate("GameInfo1", "水下单位数：", None))
        self.label_24.setText(_translate("GameInfo1", "   1号", None))

