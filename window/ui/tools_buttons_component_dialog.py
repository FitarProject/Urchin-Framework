# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_buttons_component_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_buttons_component_dialog(object):
    def setupUi(self, tools_buttons_component_dialog):
        tools_buttons_component_dialog.setObjectName("tools_buttons_component_dialog")
        tools_buttons_component_dialog.resize(503, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(tools_buttons_component_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_position = QtWidgets.QLabel(tools_buttons_component_dialog)
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 2, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(tools_buttons_component_dialog)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(tools_buttons_component_dialog)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(tools_buttons_component_dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 2)
        self.button_name = QtWidgets.QToolButton(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_name.sizePolicy().hasHeightForWidth())
        self.button_name.setSizePolicy(sizePolicy)
        self.button_name.setText("")
        self.button_name.setAutoRaise(True)
        self.button_name.setObjectName("button_name")
        self.gridLayout.addWidget(self.button_name, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(tools_buttons_component_dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(tools_buttons_component_dialog)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setText("")
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setTabStopWidth(24)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setTabStopWidth(24)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.textEdit_3 = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_3.setTabStopWidth(24)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_4.addWidget(self.textEdit_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.textEdit_4 = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_4.setTabStopWidth(24)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_5.addWidget(self.textEdit_4)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_introduction = QtWidgets.QLabel(tools_buttons_component_dialog)
        self.label_introduction.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_introduction.setObjectName("label_introduction")
        self.horizontalLayout_2.addWidget(self.label_introduction)
        self.plainTextEdit_introduction = QtWidgets.QPlainTextEdit(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_introduction.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_introduction.setSizePolicy(sizePolicy)
        self.plainTextEdit_introduction.setMinimumSize(QtCore.QSize(0, 20))
        self.plainTextEdit_introduction.setMaximumSize(QtCore.QSize(600, 100))
        self.plainTextEdit_introduction.setReadOnly(True)
        self.plainTextEdit_introduction.setObjectName("plainTextEdit_introduction")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_introduction)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 3, 1, 1)
        self.button_editall = QtWidgets.QPushButton(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_editall.sizePolicy().hasHeightForWidth())
        self.button_editall.setSizePolicy(sizePolicy)
        self.button_editall.setObjectName("button_editall")
        self.gridLayout_3.addWidget(self.button_editall, 1, 4, 2, 1)
        self.button_add_to_selected = QtWidgets.QPushButton(tools_buttons_component_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_to_selected.sizePolicy().hasHeightForWidth())
        self.button_add_to_selected.setSizePolicy(sizePolicy)
        self.button_add_to_selected.setObjectName("button_add_to_selected")
        self.gridLayout_3.addWidget(self.button_add_to_selected, 1, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(tools_buttons_component_dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(tools_buttons_component_dialog)

    def retranslateUi(self, tools_buttons_component_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_buttons_component_dialog.setWindowTitle(_translate("tools_buttons_component_dialog", "配件详情"))
        self.label_position.setText(_translate("tools_buttons_component_dialog", " 配件类型"))
        self.label_name.setText(_translate("tools_buttons_component_dialog", "名称"))
        self.comboBox.setItemText(0, _translate("tools_buttons_component_dialog", "工具执行脚本"))
        self.comboBox.setItemText(1, _translate("tools_buttons_component_dialog", "数据预处理脚本"))
        self.comboBox.setItemText(2, _translate("tools_buttons_component_dialog", "前置命令"))
        self.comboBox.setItemText(3, _translate("tools_buttons_component_dialog", "后置命令"))
        self.label.setText(_translate("tools_buttons_component_dialog", " 脚本位置"))
        self.label_2.setText(_translate("tools_buttons_component_dialog", "工具执行脚本"))
        self.textEdit.setHtml(_translate("tools_buttons_component_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">一般为调用工具执行脚本的方式，可为脚本设置代理，保存文件等。</p></body></html>"))
        self.label_3.setText(_translate("tools_buttons_component_dialog", "数据预处理脚本"))
        self.textEdit_2.setHtml(_translate("tools_buttons_component_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">一般为数据处理脚本，用于将获取到的数据进行格式统一，然后传递给特定工具。</p></body></html>"))
        self.label_4.setText(_translate("tools_buttons_component_dialog", "前置命令"))
        self.textEdit_3.setHtml(_translate("tools_buttons_component_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">接在工具执行的命令前，一般以‘&amp;’、‘&amp;&amp;’、‘|’、‘||’结尾。</p></body></html>"))
        self.label_5.setText(_translate("tools_buttons_component_dialog", "后置命令"))
        self.textEdit_4.setHtml(_translate("tools_buttons_component_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">接在工具执行的命令后，一般以‘&amp;’、‘&amp;&amp;’、‘|’、‘||’开头。</p></body></html>"))
        self.label_introduction.setText(_translate("tools_buttons_component_dialog", " 配件说明"))
        self.button_editall.setText(_translate("tools_buttons_component_dialog", "编辑"))
        self.button_add_to_selected.setText(_translate("tools_buttons_component_dialog", "添加至炼金"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_buttons_component_dialog = QtWidgets.QDialog()
    ui = Ui_tools_buttons_component_dialog()
    ui.setupUi(tools_buttons_component_dialog)
    tools_buttons_component_dialog.show()
    sys.exit(app.exec_())