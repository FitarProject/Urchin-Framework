# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combine_func_introduction_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_combine_func_introduction_dialog(object):
    def setupUi(self, combine_func_introduction_dialog):
        combine_func_introduction_dialog.setObjectName("combine_func_introduction_dialog")
        combine_func_introduction_dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(combine_func_introduction_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(combine_func_introduction_dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(combine_func_introduction_dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_command_built_in = QtWidgets.QLabel(combine_func_introduction_dialog)
        self.label_command_built_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_command_built_in.setObjectName("label_command_built_in")
        self.horizontalLayout_2.addWidget(self.label_command_built_in)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(combine_func_introduction_dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget = QtWidgets.QWidget(combine_func_introduction_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_yes = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yes.sizePolicy().hasHeightForWidth())
        self.button_yes.setSizePolicy(sizePolicy)
        self.button_yes.setObjectName("button_yes")
        self.horizontalLayout.addWidget(self.button_yes)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_no = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_no.sizePolicy().hasHeightForWidth())
        self.button_no.setSizePolicy(sizePolicy)
        self.button_no.setObjectName("button_no")
        self.horizontalLayout.addWidget(self.button_no)
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(combine_func_introduction_dialog)
        QtCore.QMetaObject.connectSlotsByName(combine_func_introduction_dialog)

    def retranslateUi(self, combine_func_introduction_dialog):
        _translate = QtCore.QCoreApplication.translate
        combine_func_introduction_dialog.setWindowTitle(_translate("combine_func_introduction_dialog", "功能名称及介绍"))
        self.label.setText(_translate("combine_func_introduction_dialog", "功能名称"))
        self.label_command_built_in.setText(_translate("combine_func_introduction_dialog", "功能介绍"))
        self.button_yes.setText(_translate("combine_func_introduction_dialog", "确定"))
        self.button_no.setText(_translate("combine_func_introduction_dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    combine_func_introduction_dialog = QtWidgets.QDialog()
    ui = Ui_combine_func_introduction_dialog()
    ui.setupUi(combine_func_introduction_dialog)
    combine_func_introduction_dialog.show()
    sys.exit(app.exec_())