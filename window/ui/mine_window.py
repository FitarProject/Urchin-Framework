# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mine_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mine_window(object):
    def setupUi(self, mine_window):
        mine_window.setObjectName("mine_window")
        mine_window.resize(590, 553)
        self.widget = QtWidgets.QWidget(mine_window)
        self.widget.setGeometry(QtCore.QRect(0, 0, 580, 540))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 484, 381, 61))
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(180, 10, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 361, 21))
        self.label_7.setObjectName("label_7")
        self.scrollArea_custom = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_custom.setGeometry(QtCore.QRect(0, 100, 580, 381))
        self.scrollArea_custom.setWidgetResizable(True)
        self.scrollArea_custom.setObjectName("scrollArea_custom")
        self.scrollAreaWidgetContents_custom = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_custom.setGeometry(QtCore.QRect(0, 0, 578, 379))
        self.scrollAreaWidgetContents_custom.setObjectName("scrollAreaWidgetContents_custom")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_custom)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 70, 15))
        self.label_4.setObjectName("label_4")
        self.button_manage = QtWidgets.QPushButton(self.scrollAreaWidgetContents_custom)
        self.button_manage.setGeometry(QtCore.QRect(500, 0, 75, 23))
        self.button_manage.setObjectName("button_manage")
        self.scrollArea_custom.setWidget(self.scrollAreaWidgetContents_custom)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 580, 81))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 578, 79))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 50, 15))
        self.label_3.setObjectName("label_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.button_export = QtWidgets.QPushButton(self.widget)
        self.button_export.setGeometry(QtCore.QRect(490, 490, 71, 41))
        self.button_export.setObjectName("button_export")
        self.button_import = QtWidgets.QPushButton(self.widget)
        self.button_import.setGeometry(QtCore.QRect(400, 490, 71, 41))
        self.button_import.setObjectName("button_import")

        self.retranslateUi(mine_window)
        QtCore.QMetaObject.connectSlotsByName(mine_window)

    def retranslateUi(self, mine_window):
        _translate = QtCore.QCoreApplication.translate
        mine_window.setWindowTitle(_translate("mine_window", "我的百宝箱"))
        self.label_5.setText(_translate("mine_window", "作者博客：fitar.top"))
        self.label_6.setText(_translate("mine_window", "联系方式：admin@fitarmail.top"))
        self.label_7.setText(_translate("mine_window", "项目地址：https://github.com/FitarProject/Urchin-Framework"))
        self.label_4.setText(_translate("mine_window", "自定义功能"))
        self.button_manage.setText(_translate("mine_window", "管理"))
        self.label_2.setText(_translate("mine_window", " 我的功能库"))
        self.label_3.setText(_translate("mine_window", "内置功能"))
        self.button_export.setText(_translate("mine_window", "导出配置"))
        self.button_import.setText(_translate("mine_window", "导入配置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mine_window = QtWidgets.QWidget()
    ui = Ui_mine_window()
    ui.setupUi(mine_window)
    mine_window.show()
    sys.exit(app.exec_())
