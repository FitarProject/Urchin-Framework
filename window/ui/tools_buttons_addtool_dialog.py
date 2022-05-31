# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_buttons_addtool_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_buttons_addtool_dialog(object):
    def setupUi(self, tools_buttons_addtool_dialog):
        tools_buttons_addtool_dialog.setObjectName("tools_buttons_addtool_dialog")
        tools_buttons_addtool_dialog.resize(502, 465)
        self.gridLayout_2 = QtWidgets.QGridLayout(tools_buttons_addtool_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(tools_buttons_addtool_dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_command_built_in = QtWidgets.QToolButton(self.widget)
        self.toolButton_command_built_in.setToolTip("")
        self.toolButton_command_built_in.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_command_built_in.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_command_built_in.setAutoRaise(True)
        self.toolButton_command_built_in.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_command_built_in.setObjectName("toolButton_command_built_in")
        self.gridLayout.addWidget(self.toolButton_command_built_in, 9, 4, 1, 1)
        self.label_command_template = QtWidgets.QLabel(self.widget)
        self.label_command_template.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_template.setObjectName("label_command_template")
        self.gridLayout.addWidget(self.label_command_template, 4, 1, 1, 1)
        self.label_simple_name = QtWidgets.QLabel(self.widget)
        self.label_simple_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_simple_name.setObjectName("label_simple_name")
        self.gridLayout.addWidget(self.label_simple_name, 1, 1, 1, 1)
        self.toolButton_command_introduction = QtWidgets.QToolButton(self.widget)
        self.toolButton_command_introduction.setToolTip("")
        self.toolButton_command_introduction.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_command_introduction.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_command_introduction.setAutoRaise(True)
        self.toolButton_command_introduction.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_command_introduction.setObjectName("toolButton_command_introduction")
        self.gridLayout.addWidget(self.toolButton_command_introduction, 6, 4, 1, 1)
        self.button_no = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.gridLayout.addWidget(self.button_no, 12, 3, 2, 1)
        self.lineEdit_simple_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_simple_name.setText("")
        self.lineEdit_simple_name.setMaxLength(100)
        self.lineEdit_simple_name.setFrame(False)
        self.lineEdit_simple_name.setReadOnly(False)
        self.lineEdit_simple_name.setObjectName("lineEdit_simple_name")
        self.gridLayout.addWidget(self.lineEdit_simple_name, 1, 2, 1, 2)
        self.label_command_example = QtWidgets.QLabel(self.widget)
        self.label_command_example.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_example.setObjectName("label_command_example")
        self.gridLayout.addWidget(self.label_command_example, 8, 1, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setMaxLength(100)
        self.lineEdit_name.setFrame(False)
        self.lineEdit_name.setReadOnly(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 2)
        self.toolButton_position = QtWidgets.QToolButton(self.widget)
        self.toolButton_position.setToolTip("")
        self.toolButton_position.setStyleSheet("")
        self.toolButton_position.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_position.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_position.setAutoRaise(True)
        self.toolButton_position.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_position.setObjectName("toolButton_position")
        self.gridLayout.addWidget(self.toolButton_position, 3, 4, 1, 1)
        self.label_command_built_in = QtWidgets.QLabel(self.widget)
        self.label_command_built_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_built_in.setObjectName("label_command_built_in")
        self.gridLayout.addWidget(self.label_command_built_in, 9, 1, 1, 1)
        self.lineEdit_position = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_position.setText("")
        self.lineEdit_position.setFrame(False)
        self.lineEdit_position.setReadOnly(False)
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.gridLayout.addWidget(self.lineEdit_position, 3, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 2, 1, 1)
        self.label_position = QtWidgets.QLabel(self.widget)
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 3, 1, 1, 1)
        self.toolButton_command_example = QtWidgets.QToolButton(self.widget)
        self.toolButton_command_example.setToolTip("")
        self.toolButton_command_example.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_command_example.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_command_example.setAutoRaise(True)
        self.toolButton_command_example.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_command_example.setObjectName("toolButton_command_example")
        self.gridLayout.addWidget(self.toolButton_command_example, 8, 4, 1, 1)
        self.label_command_introduction = QtWidgets.QLabel(self.widget)
        self.label_command_introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_introduction.setObjectName("label_command_introduction")
        self.gridLayout.addWidget(self.label_command_introduction, 6, 1, 1, 1)
        self.toolButton_command_template = QtWidgets.QToolButton(self.widget)
        self.toolButton_command_template.setToolTip("")
        self.toolButton_command_template.setStyleSheet("")
        self.toolButton_command_template.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_command_template.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_command_template.setAutoRaise(True)
        self.toolButton_command_template.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_command_template.setObjectName("toolButton_command_template")
        self.gridLayout.addWidget(self.toolButton_command_template, 4, 4, 1, 1)
        self.toolButton_result = QtWidgets.QToolButton(self.widget)
        self.toolButton_result.setToolTip("")
        self.toolButton_result.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_result.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_result.setAutoRaise(True)
        self.toolButton_result.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_result.setObjectName("toolButton_result")
        self.gridLayout.addWidget(self.toolButton_result, 10, 4, 1, 1)
        self.plainTextEdit_introduction = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_introduction.setReadOnly(False)
        self.plainTextEdit_introduction.setPlainText("")
        self.plainTextEdit_introduction.setObjectName("plainTextEdit_introduction")
        self.gridLayout.addWidget(self.plainTextEdit_introduction, 11, 2, 1, 3)
        self.comboBox_result = QtWidgets.QComboBox(self.widget)
        self.comboBox_result.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_result.setEditable(True)
        self.comboBox_result.setFrame(False)
        self.comboBox_result.setObjectName("comboBox_result")
        self.gridLayout.addWidget(self.comboBox_result, 10, 2, 1, 2)
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 1, 1, 1)
        self.lineEdit_command_introduction = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_introduction.setText("")
        self.lineEdit_command_introduction.setFrame(False)
        self.lineEdit_command_introduction.setReadOnly(False)
        self.lineEdit_command_introduction.setObjectName("lineEdit_command_introduction")
        self.gridLayout.addWidget(self.lineEdit_command_introduction, 6, 2, 1, 2)
        self.label_result = QtWidgets.QLabel(self.widget)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 10, 1, 1, 1)
        self.label_introduction = QtWidgets.QLabel(self.widget)
        self.label_introduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_introduction.setObjectName("label_introduction")
        self.gridLayout.addWidget(self.label_introduction, 11, 1, 1, 1)
        self.comboBox_command_template = QtWidgets.QComboBox(self.widget)
        self.comboBox_command_template.setEditable(True)
        self.comboBox_command_template.setFrame(False)
        self.comboBox_command_template.setObjectName("comboBox_command_template")
        self.gridLayout.addWidget(self.comboBox_command_template, 4, 2, 1, 2)
        self.button_yes = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.gridLayout.addWidget(self.button_yes, 12, 1, 2, 1)
        self.lineEdit_command_example = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_command_example.setText("")
        self.lineEdit_command_example.setFrame(False)
        self.lineEdit_command_example.setReadOnly(False)
        self.lineEdit_command_example.setObjectName("lineEdit_command_example")
        self.gridLayout.addWidget(self.lineEdit_command_example, 8, 2, 1, 2)
        self.toolButton_simple_rename = QtWidgets.QToolButton(self.widget)
        self.toolButton_simple_rename.setToolTip("")
        self.toolButton_simple_rename.setStyleSheet("")
        self.toolButton_simple_rename.setText("")
        self.toolButton_simple_rename.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_simple_rename.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_simple_rename.setAutoRaise(True)
        self.toolButton_simple_rename.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_simple_rename.setObjectName("toolButton_simple_rename")
        self.gridLayout.addWidget(self.toolButton_simple_rename, 1, 4, 1, 1)
        self.toolButton_rename = QtWidgets.QToolButton(self.widget)
        self.toolButton_rename.setToolTip("")
        self.toolButton_rename.setStyleSheet("")
        self.toolButton_rename.setText("")
        self.toolButton_rename.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_rename.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_rename.setAutoRaise(True)
        self.toolButton_rename.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_rename.setObjectName("toolButton_rename")
        self.gridLayout.addWidget(self.toolButton_rename, 0, 4, 1, 1)
        self.comboBox_command_built_in = QtWidgets.QComboBox(self.widget)
        self.comboBox_command_built_in.setEditable(True)
        self.comboBox_command_built_in.setFrame(False)
        self.comboBox_command_built_in.setObjectName("comboBox_command_built_in")
        self.gridLayout.addWidget(self.comboBox_command_built_in, 9, 2, 1, 2)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(tools_buttons_addtool_dialog)
        QtCore.QMetaObject.connectSlotsByName(tools_buttons_addtool_dialog)

    def retranslateUi(self, tools_buttons_addtool_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_buttons_addtool_dialog.setWindowTitle(_translate("tools_buttons_addtool_dialog", "添加新工具"))
        self.label_command_template.setText(_translate("tools_buttons_addtool_dialog", "命令模板"))
        self.label_simple_name.setText(_translate("tools_buttons_addtool_dialog", "简称"))
        self.button_no.setText(_translate("tools_buttons_addtool_dialog", "取消"))
        self.label_command_example.setText(_translate("tools_buttons_addtool_dialog", "命令示例"))
        self.label_command_built_in.setText(_translate("tools_buttons_addtool_dialog", "固定命令"))
        self.label_position.setText(_translate("tools_buttons_addtool_dialog", "工具位置"))
        self.label_command_introduction.setText(_translate("tools_buttons_addtool_dialog", "命令介绍"))
        self.label_name.setText(_translate("tools_buttons_addtool_dialog", "名称"))
        self.label_result.setText(_translate("tools_buttons_addtool_dialog", "有效结果"))
        self.label_introduction.setText(_translate("tools_buttons_addtool_dialog", "工具说明"))
        self.button_yes.setText(_translate("tools_buttons_addtool_dialog", "添加"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_buttons_addtool_dialog = QtWidgets.QDialog()
    ui = Ui_tools_buttons_addtool_dialog()
    ui.setupUi(tools_buttons_addtool_dialog)
    tools_buttons_addtool_dialog.show()
    sys.exit(app.exec_())