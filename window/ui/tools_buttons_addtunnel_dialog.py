# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_buttons_addtunnel_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_buttons_addtunnel_dialog(object):
    def setupUi(self, tools_buttons_addtunnel_dialog):
        tools_buttons_addtunnel_dialog.setObjectName("tools_buttons_addtunnel_dialog")
        tools_buttons_addtunnel_dialog.resize(502, 488)
        self.verticalLayout = QtWidgets.QVBoxLayout(tools_buttons_addtunnel_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(tools_buttons_addtunnel_dialog)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(tools_buttons_addtunnel_dialog)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setReadOnly(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.button_name = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_name.sizePolicy().hasHeightForWidth())
        self.button_name.setSizePolicy(sizePolicy)
        self.button_name.setText("")
        self.button_name.setAutoRaise(True)
        self.button_name.setObjectName("button_name")
        self.gridLayout.addWidget(self.button_name, 0, 2, 1, 1)
        self.label_position = QtWidgets.QLabel(tools_buttons_addtunnel_dialog)
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 1, 0, 1, 1)
        self.lineEdit_position = QtWidgets.QLineEdit(tools_buttons_addtunnel_dialog)
        self.lineEdit_position.setText("")
        self.lineEdit_position.setFrame(False)
        self.lineEdit_position.setReadOnly(False)
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.gridLayout.addWidget(self.lineEdit_position, 1, 1, 1, 1)
        self.button_position = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_position.sizePolicy().hasHeightForWidth())
        self.button_position.setSizePolicy(sizePolicy)
        self.button_position.setText("")
        self.button_position.setAutoRaise(True)
        self.button_position.setObjectName("button_position")
        self.gridLayout.addWidget(self.button_position, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_deloutput = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_deloutput.sizePolicy().hasHeightForWidth())
        self.button_deloutput.setSizePolicy(sizePolicy)
        self.button_deloutput.setText("")
        self.button_deloutput.setAutoRaise(True)
        self.button_deloutput.setObjectName("button_deloutput")
        self.gridLayout_2.addWidget(self.button_deloutput, 4, 3, 1, 1)
        self.button_addoutput = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_addoutput.sizePolicy().hasHeightForWidth())
        self.button_addoutput.setSizePolicy(sizePolicy)
        self.button_addoutput.setText("")
        self.button_addoutput.setAutoRaise(True)
        self.button_addoutput.setObjectName("button_addoutput")
        self.gridLayout_2.addWidget(self.button_addoutput, 3, 3, 1, 1)
        self.label_output = QtWidgets.QLabel(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_output.sizePolicy().hasHeightForWidth())
        self.label_output.setSizePolicy(sizePolicy)
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.gridLayout_2.addWidget(self.label_output, 3, 0, 2, 1)
        self.list_input = QtWidgets.QListWidget(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_input.sizePolicy().hasHeightForWidth())
        self.list_input.setSizePolicy(sizePolicy)
        self.list_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.list_input.setObjectName("list_input")
        self.gridLayout_2.addWidget(self.list_input, 0, 1, 2, 1)
        self.list_output = QtWidgets.QListWidget(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_output.sizePolicy().hasHeightForWidth())
        self.list_output.setSizePolicy(sizePolicy)
        self.list_output.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.list_output.setObjectName("list_output")
        self.gridLayout_2.addWidget(self.list_output, 3, 1, 2, 1)
        self.label_input = QtWidgets.QLabel(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_input.sizePolicy().hasHeightForWidth())
        self.label_input.setSizePolicy(sizePolicy)
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label_input")
        self.gridLayout_2.addWidget(self.label_input, 0, 0, 2, 1)
        self.button_delinput = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delinput.sizePolicy().hasHeightForWidth())
        self.button_delinput.setSizePolicy(sizePolicy)
        self.button_delinput.setText("")
        self.button_delinput.setAutoRaise(True)
        self.button_delinput.setObjectName("button_delinput")
        self.gridLayout_2.addWidget(self.button_delinput, 1, 3, 1, 1)
        self.button_addinput = QtWidgets.QToolButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_addinput.sizePolicy().hasHeightForWidth())
        self.button_addinput.setSizePolicy(sizePolicy)
        self.button_addinput.setText("")
        self.button_addinput.setAutoRaise(True)
        self.button_addinput.setObjectName("button_addinput")
        self.gridLayout_2.addWidget(self.button_addinput, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_introduction = QtWidgets.QLabel(tools_buttons_addtunnel_dialog)
        self.label_introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_introduction.setObjectName("label_introduction")
        self.horizontalLayout.addWidget(self.label_introduction)
        self.plainTextEdit_introduction = QtWidgets.QPlainTextEdit(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_introduction.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_introduction.setSizePolicy(sizePolicy)
        self.plainTextEdit_introduction.setReadOnly(False)
        self.plainTextEdit_introduction.setObjectName("plainTextEdit_introduction")
        self.horizontalLayout.addWidget(self.plainTextEdit_introduction)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 3, 1, 1)
        self.button_no = QtWidgets.QPushButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.gridLayout_3.addWidget(self.button_no, 1, 4, 2, 1)
        self.button_yes = QtWidgets.QPushButton(tools_buttons_addtunnel_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.gridLayout_3.addWidget(self.button_yes, 1, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(tools_buttons_addtunnel_dialog)
        QtCore.QMetaObject.connectSlotsByName(tools_buttons_addtunnel_dialog)

    def retranslateUi(self, tools_buttons_addtunnel_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_buttons_addtunnel_dialog.setWindowTitle(_translate("tools_buttons_addtunnel_dialog", "添加新通道"))
        self.label_name.setText(_translate("tools_buttons_addtunnel_dialog", "名称"))
        self.label_position.setText(_translate("tools_buttons_addtunnel_dialog", " 脚本位置"))
        self.label_output.setText(_translate("tools_buttons_addtunnel_dialog", " 输出变量"))
        self.list_input.setSortingEnabled(False)
        self.list_output.setSortingEnabled(False)
        self.label_input.setText(_translate("tools_buttons_addtunnel_dialog", " 输入变量"))
        self.label_introduction.setText(_translate("tools_buttons_addtunnel_dialog", " 通道说明"))
        self.button_no.setText(_translate("tools_buttons_addtunnel_dialog", "取消"))
        self.button_yes.setText(_translate("tools_buttons_addtunnel_dialog", "添加"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_buttons_addtunnel_dialog = QtWidgets.QDialog()
    ui = Ui_tools_buttons_addtunnel_dialog()
    ui.setupUi(tools_buttons_addtunnel_dialog)
    tools_buttons_addtunnel_dialog.show()
    sys.exit(app.exec_())
