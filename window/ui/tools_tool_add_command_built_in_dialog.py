# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_tool_add_command_built_in_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_tool_add_command_built_in_dialog(object):
    def setupUi(self, tools_tool_add_command_built_in_dialog):
        tools_tool_add_command_built_in_dialog.setObjectName("tools_tool_add_command_built_in_dialog")
        tools_tool_add_command_built_in_dialog.resize(393, 196)
        self.gridLayout_2 = QtWidgets.QGridLayout(tools_tool_add_command_built_in_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(tools_tool_add_command_built_in_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_command_built_in = QtWidgets.QLabel(self.widget)
        self.label_command_built_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_built_in.setObjectName("label_command_built_in")
        self.gridLayout.addWidget(self.label_command_built_in, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.button_yes = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.gridLayout.addWidget(self.button_yes, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.button_no = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.gridLayout.addWidget(self.button_no, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.lineEdit_command_built_in = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_built_in.setText("")
        self.lineEdit_command_built_in.setFrame(False)
        self.lineEdit_command_built_in.setReadOnly(False)
        self.lineEdit_command_built_in.setObjectName("lineEdit_command_built_in")
        self.gridLayout.addWidget(self.lineEdit_command_built_in, 0, 1, 1, 4)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(tools_tool_add_command_built_in_dialog)
        QtCore.QMetaObject.connectSlotsByName(tools_tool_add_command_built_in_dialog)

    def retranslateUi(self, tools_tool_add_command_built_in_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_tool_add_command_built_in_dialog.setWindowTitle(_translate("tools_tool_add_command_built_in_dialog", "添加固定命令"))
        self.label_command_built_in.setText(_translate("tools_tool_add_command_built_in_dialog", "固定命令"))
        self.button_yes.setText(_translate("tools_tool_add_command_built_in_dialog", "确定"))
        self.button_no.setText(_translate("tools_tool_add_command_built_in_dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_tool_add_command_built_in_dialog = QtWidgets.QDialog()
    ui = Ui_tools_tool_add_command_built_in_dialog()
    ui.setupUi(tools_tool_add_command_built_in_dialog)
    tools_tool_add_command_built_in_dialog.show()
    sys.exit(app.exec_())