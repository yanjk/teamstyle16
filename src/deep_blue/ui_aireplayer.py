# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIReplayer.ui'
#
# Created: Thu Dec 11 15:33:43 2014
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

class Ui_AIReplayer(object):
    def setupUi(self, AIReplayer):
        AIReplayer.setObjectName(_fromUtf8("AIReplayer"))
        AIReplayer.resize(1347, 771)
        self.formLayoutWidget = QtGui.QWidget(AIReplayer)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 0, 801, 761))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.CenterLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.CenterLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.CenterLayout.setMargin(0)
        self.CenterLayout.setObjectName(_fromUtf8("CenterLayout"))
        self.AILabel1 = QtGui.QLabel(AIReplayer)
        self.AILabel1.setGeometry(QtCore.QRect(10, 60, 54, 12))
        self.AILabel1.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.AILabel1.setObjectName(_fromUtf8("AILabel1"))
        self.ExitButton = QtGui.QPushButton(AIReplayer)
        self.ExitButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.ExitButton.setStyleSheet(_fromUtf8("font: 10pt \"微软简魏碑\";"))
        self.ExitButton.setObjectName(_fromUtf8("ExitButton"))
        self.HelpButton = QtGui.QPushButton(AIReplayer)
        self.HelpButton.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.HelpButton.setStyleSheet(_fromUtf8("font: 10pt \"微软简魏碑\";"))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        self.AILabel2 = QtGui.QLabel(AIReplayer)
        self.AILabel2.setGeometry(QtCore.QRect(1100, 60, 54, 12))
        self.AILabel2.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.AILabel2.setObjectName(_fromUtf8("AILabel2"))
        self.OpenFileComboBox1 = QtGui.QComboBox(AIReplayer)
        self.OpenFileComboBox1.setGeometry(QtCore.QRect(10, 80, 131, 22))
        self.OpenFileComboBox1.setStyleSheet(_fromUtf8("font: 8pt \"微软简魏碑\";"))
        self.OpenFileComboBox1.setObjectName(_fromUtf8("OpenFileComboBox1"))
        self.OpenFileComboBox2 = QtGui.QComboBox(AIReplayer)
        self.OpenFileComboBox2.setGeometry(QtCore.QRect(1100, 80, 131, 22))
        self.OpenFileComboBox2.setStyleSheet(_fromUtf8("font: 8pt \"微软简魏碑\";"))
        self.OpenFileComboBox2.setObjectName(_fromUtf8("OpenFileComboBox2"))
        self.layoutWidget_2 = QtGui.QWidget(AIReplayer)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1240, 80, 99, 25))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.OpenFileButton2 = QtGui.QPushButton(self.layoutWidget_2)
        self.OpenFileButton2.setText(_fromUtf8(""))
        self.OpenFileButton2.setObjectName(_fromUtf8("OpenFileButton2"))
        self.horizontalLayout_4.addWidget(self.OpenFileButton2)
        self.HumanCheckBox2 = QtGui.QCheckBox(self.layoutWidget_2)
        self.HumanCheckBox2.setStyleSheet(_fromUtf8("font: 75 9pt \"Tekton Pro\";"))
        self.HumanCheckBox2.setObjectName(_fromUtf8("HumanCheckBox2"))
        self.horizontalLayout_4.addWidget(self.HumanCheckBox2)
        self.layoutWidget = QtGui.QWidget(AIReplayer)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 80, 107, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.OpenFileButton1 = QtGui.QPushButton(self.layoutWidget)
        self.OpenFileButton1.setText(_fromUtf8(""))
        self.OpenFileButton1.setObjectName(_fromUtf8("OpenFileButton1"))
        self.horizontalLayout_2.addWidget(self.OpenFileButton1)
        self.HumanCheckBox1 = QtGui.QCheckBox(self.layoutWidget)
        self.HumanCheckBox1.setStyleSheet(_fromUtf8("font: 75 9pt \"Tekton Pro\";"))
        self.HumanCheckBox1.setObjectName(_fromUtf8("HumanCheckBox1"))
        self.horizontalLayout_2.addWidget(self.HumanCheckBox1)
        self.LoadFilePushButton = QtGui.QPushButton(AIReplayer)
        self.LoadFilePushButton.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.LoadFilePushButton.setStyleSheet(_fromUtf8("font: 9pt \"微软简魏碑\";"))
        self.LoadFilePushButton.setObjectName(_fromUtf8("LoadFilePushButton"))
        self.LoadMapPushButton = QtGui.QPushButton(AIReplayer)
        self.LoadMapPushButton.setGeometry(QtCore.QRect(210, 40, 75, 23))
        self.LoadMapPushButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.LoadMapPushButton.setObjectName(_fromUtf8("LoadMapPushButton"))
        self.layoutWidget_3 = QtGui.QWidget(AIReplayer)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 400, 91, 74))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Frog1RadioButton = QtGui.QRadioButton(self.layoutWidget_3)
        self.Frog1RadioButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.Frog1RadioButton.setObjectName(_fromUtf8("Frog1RadioButton"))
        self.verticalLayout.addWidget(self.Frog1RadioButton)
        self.Frog2RadioButton = QtGui.QRadioButton(self.layoutWidget_3)
        self.Frog2RadioButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.Frog2RadioButton.setObjectName(_fromUtf8("Frog2RadioButton"))
        self.verticalLayout.addWidget(self.Frog2RadioButton)
        self.GodVisionRadioButton = QtGui.QRadioButton(self.layoutWidget_3)
        self.GodVisionRadioButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.GodVisionRadioButton.setChecked(True)
        self.GodVisionRadioButton.setObjectName(_fromUtf8("GodVisionRadioButton"))
        self.verticalLayout.addWidget(self.GodVisionRadioButton)
        self.PlayPushButton = QtGui.QPushButton(AIReplayer)
        self.PlayPushButton.setGeometry(QtCore.QRect(118, 420, 60, 23))
        self.PlayPushButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.PlayPushButton.setCheckable(False)
        self.PlayPushButton.setObjectName(_fromUtf8("PlayPushButton"))
        self.StopPushButton = QtGui.QPushButton(AIReplayer)
        self.StopPushButton.setGeometry(QtCore.QRect(190, 420, 60, 23))
        self.StopPushButton.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.StopPushButton.setObjectName(_fromUtf8("StopPushButton"))
        self.RoundSlider = QtGui.QSlider(AIReplayer)
        self.RoundSlider.setGeometry(QtCore.QRect(10, 510, 261, 22))
        self.RoundSlider.setMaximum(300)
        self.RoundSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RoundSlider.setObjectName(_fromUtf8("RoundSlider"))
        self.RoundNumberLabel = QtGui.QLabel(AIReplayer)
        self.RoundNumberLabel.setGeometry(QtCore.QRect(20, 480, 140, 40))
        self.RoundNumberLabel.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.RoundNumberLabel.setObjectName(_fromUtf8("RoundNumberLabel"))
        self.SpeedSliderLabel = QtGui.QLabel(AIReplayer)
        self.SpeedSliderLabel.setGeometry(QtCore.QRect(20, 540, 84, 12))
        self.SpeedSliderLabel.setStyleSheet(_fromUtf8("font: 11pt \"微软简魏碑\";"))
        self.SpeedSliderLabel.setObjectName(_fromUtf8("SpeedSliderLabel"))
        self.SpeedSlider = QtGui.QSlider(AIReplayer)
        self.SpeedSlider.setGeometry(QtCore.QRect(10, 560, 261, 22))
        self.SpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedSlider.setObjectName(_fromUtf8("SpeedSlider"))
        self.RoundLcdNumber = QtGui.QLCDNumber(AIReplayer)
        self.RoundLcdNumber.setGeometry(QtCore.QRect(70, 490, 41, 21))
        self.RoundLcdNumber.setStyleSheet(_fromUtf8(""))
        self.RoundLcdNumber.setObjectName(_fromUtf8("RoundLcdNumber"))
        self.verticalLayoutWidget = QtGui.QWidget(AIReplayer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1110, 110, 221, 441))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.RightLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.RightLayout.setMargin(0)
        self.RightLayout.setObjectName(_fromUtf8("RightLayout"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(AIReplayer)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1120, 560, 211, 201))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.SmallMapLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.SmallMapLayout.setMargin(0)
        self.SmallMapLayout.setObjectName(_fromUtf8("SmallMapLayout"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(AIReplayer)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 110, 251, 281))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.LeftLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.LeftLayout.setMargin(0)
        self.LeftLayout.setObjectName(_fromUtf8("LeftLayout"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(AIReplayer)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 590, 251, 171))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.CreateLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.CreateLayout.setMargin(0)
        self.CreateLayout.setObjectName(_fromUtf8("CreateLayout"))
        self.ReplayComboBox = QtGui.QComboBox(AIReplayer)
        self.ReplayComboBox.setGeometry(QtCore.QRect(90, 10, 111, 22))
        self.ReplayComboBox.setStyleSheet(_fromUtf8("font: 8pt \"微软简魏碑\";"))
        self.ReplayComboBox.setObjectName(_fromUtf8("ReplayComboBox"))
        self.MapComboBox = QtGui.QComboBox(AIReplayer)
        self.MapComboBox.setGeometry(QtCore.QRect(90, 40, 111, 22))
        self.MapComboBox.setStyleSheet(_fromUtf8("font: 8pt \"微软简魏碑\";"))
        self.MapComboBox.setObjectName(_fromUtf8("MapComboBox"))

        self.retranslateUi(AIReplayer)
        QtCore.QMetaObject.connectSlotsByName(AIReplayer)

    def retranslateUi(self, AIReplayer):
        AIReplayer.setWindowTitle(_translate("AIReplayer", "AIReplayer", None))
        self.AILabel1.setText(_translate("AIReplayer", "1号AI：", None))
        self.ExitButton.setText(_translate("AIReplayer", "后退", None))
        self.HelpButton.setText(_translate("AIReplayer", "帮助", None))
        self.AILabel2.setText(_translate("AIReplayer", "2号AI：", None))
        self.HumanCheckBox2.setText(_translate("AIReplayer", "Human", None))
        self.HumanCheckBox1.setText(_translate("AIReplayer", "Human", None))
        self.LoadFilePushButton.setText(_translate("AIReplayer", "加载回放文件", None))
        self.LoadMapPushButton.setText(_translate("AIReplayer", "加载地图", None))
        self.Frog1RadioButton.setText(_translate("AIReplayer", "1号迷雾", None))
        self.Frog2RadioButton.setText(_translate("AIReplayer", "2号迷雾", None))
        self.GodVisionRadioButton.setText(_translate("AIReplayer", "上帝视角", None))
        self.PlayPushButton.setText(_translate("AIReplayer", "播放", None))
        self.StopPushButton.setText(_translate("AIReplayer", "停止", None))
        self.RoundNumberLabel.setText(_translate("AIReplayer", "回合数", None))
        self.SpeedSliderLabel.setText(_translate("AIReplayer", "播放速度", None))

