# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_tool_add_command_template_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_tool_add_command_template_dialog(object):
    def setupUi(self, tools_tool_add_command_template_dialog):
        tools_tool_add_command_template_dialog.setObjectName("tools_tool_add_command_template_dialog")
        tools_tool_add_command_template_dialog.resize(384, 295)
        self.gridLayout_2 = QtWidgets.QGridLayout(tools_tool_add_command_template_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(tools_tool_add_command_template_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_command_introduction = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_introduction.setText("")
        self.lineEdit_command_introduction.setFrame(False)
        self.lineEdit_command_introduction.setReadOnly(False)
        self.lineEdit_command_introduction.setObjectName("lineEdit_command_introduction")
        self.gridLayout.addWidget(self.lineEdit_command_introduction, 1, 1, 1, 1)
        self.label_command_example = QtWidgets.QLabel(self.widget)
        self.label_command_example.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_example.setObjectName("label_command_example")
        self.gridLayout.addWidget(self.label_command_example, 2, 0, 1, 1)
        self.label_command_introduction = QtWidgets.QLabel(self.widget)
        self.label_command_introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_introduction.setObjectName("label_command_introduction")
        self.gridLayout.addWidget(self.label_command_introduction, 1, 0, 1, 1)
        self.lineEdit_command_example = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_example.setText("")
        self.lineEdit_command_example.setFrame(False)
        self.lineEdit_command_example.setReadOnly(False)
        self.lineEdit_command_example.setObjectName("lineEdit_command_example")
        self.gridLayout.addWidget(self.lineEdit_command_example, 2, 1, 1, 1)
        self.lineEdit_command_template = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_template.setFrame(False)
        self.lineEdit_command_template.setReadOnly(False)
        self.lineEdit_command_template.setObjectName("lineEdit_command_template")
        self.gridLayout.addWidget(self.lineEdit_command_template, 0, 1, 1, 1)
        self.label_command_template = QtWidgets.QLabel(self.widget)
        self.label_command_template.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_template.setObjectName("label_command_template")
        self.gridLayout.addWidget(self.label_command_template, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_no = QtWidgets.QPushButton(tools_tool_add_command_template_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.gridLayout_3.addWidget(self.button_no, 1, 3, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.gridLayout_3.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 4, 1, 1)
        self.button_yes = QtWidgets.QPushButton(tools_tool_add_command_template_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.gridLayout_3.addWidget(self.button_yes, 1, 1, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(tools_tool_add_command_template_dialog)
        QtCore.QMetaObject.connectSlotsByName(tools_tool_add_command_template_dialog)

    def retranslateUi(self, tools_tool_add_command_template_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_tool_add_command_template_dialog.setWindowTitle(_translate("tools_tool_add_command_template_dialog", "添加命令模板"))
        self.lineEdit_command_introduction.setPlaceholderText(_translate("tools_tool_add_command_template_dialog", "请输入该条命令的介绍"))
        self.label_command_example.setText(_translate("tools_tool_add_command_template_dialog", "命令示例"))
        self.label_command_introduction.setText(_translate("tools_tool_add_command_template_dialog", "命令介绍"))
        self.lineEdit_command_example.setPlaceholderText(_translate("tools_tool_add_command_template_dialog", "请输入该条命令的示例"))
        self.label_command_template.setText(_translate("tools_tool_add_command_template_dialog", "命令模板"))
        self.button_no.setText(_translate("tools_tool_add_command_template_dialog", "取消"))
        self.button_yes.setText(_translate("tools_tool_add_command_template_dialog", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_tool_add_command_template_dialog = QtWidgets.QDialog()
    ui = Ui_tools_tool_add_command_template_dialog()
    ui.setupUi(tools_tool_add_command_template_dialog)
    tools_tool_add_command_template_dialog.show()
    sys.exit(app.exec_())
