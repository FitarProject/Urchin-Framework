# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mine_func_detatil_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mine_func_detatil_dialog(object):
    def setupUi(self, mine_func_detatil_dialog):
        mine_func_detatil_dialog.setObjectName("mine_func_detatil_dialog")
        mine_func_detatil_dialog.resize(513, 479)
        self.verticalLayout = QtWidgets.QVBoxLayout(mine_func_detatil_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(mine_func_detatil_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(mine_func_detatil_dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(mine_func_detatil_dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(mine_func_detatil_dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(mine_func_detatil_dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.button_edit = QtWidgets.QToolButton(mine_func_detatil_dialog)
        self.button_edit.setText("")
        self.button_edit.setAutoRaise(True)
        self.button_edit.setObjectName("button_edit")
        self.gridLayout.addWidget(self.button_edit, 0, 2, 1, 1)
        self.treeWidget_variable = QtWidgets.QTreeWidget(mine_func_detatil_dialog)
        self.treeWidget_variable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget_variable.setObjectName("treeWidget_variable")
        self.treeWidget_variable.header().setDefaultSectionSize(100)
        self.gridLayout.addWidget(self.treeWidget_variable, 1, 1, 1, 2)
        self.listWidget_result = QtWidgets.QListWidget(mine_func_detatil_dialog)
        self.listWidget_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_result.setObjectName("listWidget_result")
        self.gridLayout.addWidget(self.listWidget_result, 2, 1, 1, 2)
        self.plainTextEdit_introduction = QtWidgets.QPlainTextEdit(mine_func_detatil_dialog)
        self.plainTextEdit_introduction.setReadOnly(True)
        self.plainTextEdit_introduction.setObjectName("plainTextEdit_introduction")
        self.gridLayout.addWidget(self.plainTextEdit_introduction, 3, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_yes = QtWidgets.QPushButton(mine_func_detatil_dialog)
        self.button_yes.setObjectName("button_yes")
        self.horizontalLayout.addWidget(self.button_yes)
        self.button_no = QtWidgets.QPushButton(mine_func_detatil_dialog)
        self.button_no.setObjectName("button_no")
        self.horizontalLayout.addWidget(self.button_no)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(mine_func_detatil_dialog)
        QtCore.QMetaObject.connectSlotsByName(mine_func_detatil_dialog)

    def retranslateUi(self, mine_func_detatil_dialog):
        _translate = QtCore.QCoreApplication.translate
        mine_func_detatil_dialog.setWindowTitle(_translate("mine_func_detatil_dialog", "功能详情"))
        self.label.setText(_translate("mine_func_detatil_dialog", "功能名称"))
        self.label_3.setText(_translate("mine_func_detatil_dialog", "输入参数"))
        self.label_4.setText(_translate("mine_func_detatil_dialog", "输出结果"))
        self.label_2.setText(_translate("mine_func_detatil_dialog", "功能介绍"))
        self.treeWidget_variable.setSortingEnabled(True)
        self.treeWidget_variable.headerItem().setText(0, _translate("mine_func_detatil_dialog", "部件号"))
        self.treeWidget_variable.headerItem().setText(1, _translate("mine_func_detatil_dialog", "控件名称"))
        self.treeWidget_variable.headerItem().setText(2, _translate("mine_func_detatil_dialog", "变量名"))
        self.treeWidget_variable.headerItem().setText(3, _translate("mine_func_detatil_dialog", "值"))
        self.button_yes.setText(_translate("mine_func_detatil_dialog", "执行"))
        self.button_no.setText(_translate("mine_func_detatil_dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mine_func_detatil_dialog = QtWidgets.QDialog()
    ui = Ui_mine_func_detatil_dialog()
    ui.setupUi(mine_func_detatil_dialog)
    mine_func_detatil_dialog.show()
    sys.exit(app.exec_())
