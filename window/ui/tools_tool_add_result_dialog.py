# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_tool_add_result_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_tool_add_result_dialog(object):
    def setupUi(self, tools_tool_add_result_dialog):
        tools_tool_add_result_dialog.setObjectName("tools_tool_add_result_dialog")
        tools_tool_add_result_dialog.resize(392, 196)
        self.gridLayout_2 = QtWidgets.QGridLayout(tools_tool_add_result_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(tools_tool_add_result_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_result = QtWidgets.QLabel(self.widget)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.button_yes = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.gridLayout.addWidget(self.button_yes, 1, 1, 1, 1)
        self.button_no = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.gridLayout.addWidget(self.button_no, 1, 3, 1, 1)
        self.lineEdit_result = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_result.setText("")
        self.lineEdit_result.setFrame(False)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.gridLayout.addWidget(self.lineEdit_result, 0, 1, 1, 4)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(tools_tool_add_result_dialog)
        QtCore.QMetaObject.connectSlotsByName(tools_tool_add_result_dialog)

    def retranslateUi(self, tools_tool_add_result_dialog):
        _translate = QtCore.QCoreApplication.translate
        tools_tool_add_result_dialog.setWindowTitle(_translate("tools_tool_add_result_dialog", "添加有效结果"))
        self.label_result.setText(_translate("tools_tool_add_result_dialog", "有效结果"))
        self.button_yes.setText(_translate("tools_tool_add_result_dialog", "确定"))
        self.button_no.setText(_translate("tools_tool_add_result_dialog", "取消"))
        self.lineEdit_result.setPlaceholderText(_translate("tools_tool_add_result_dialog", "请输入结果文件的位置及名称"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_tool_add_result_dialog = QtWidgets.QDialog()
    ui = Ui_tools_tool_add_result_dialog()
    ui.setupUi(tools_tool_add_result_dialog)
    tools_tool_add_result_dialog.show()
    sys.exit(app.exec_())
