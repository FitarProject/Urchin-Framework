# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'works_addbutton_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_works_addbutton_dialog(object):
    def setupUi(self, works_addbutton_dialog):
        works_addbutton_dialog.setObjectName("works_addbutton_dialog")
        works_addbutton_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        works_addbutton_dialog.resize(600, 500)
        works_addbutton_dialog.setMinimumSize(QtCore.QSize(600, 500))
        works_addbutton_dialog.setMaximumSize(QtCore.QSize(600, 500))
        self.gridLayout = QtWidgets.QGridLayout(works_addbutton_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(works_addbutton_dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_select_all = QtWidgets.QPushButton(self.widget)
        self.button_select_all.setObjectName("button_select_all")
        self.horizontalLayout_2.addWidget(self.button_select_all)
        self.button_yes = QtWidgets.QPushButton(self.widget)
        self.button_yes.setObjectName("button_yes")
        self.horizontalLayout_2.addWidget(self.button_yes)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 410, 4100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(works_addbutton_dialog)
        QtCore.QMetaObject.connectSlotsByName(works_addbutton_dialog)

    def retranslateUi(self, works_addbutton_dialog):
        _translate = QtCore.QCoreApplication.translate
        works_addbutton_dialog.setWindowTitle(_translate("works_addbutton_dialog", "选择功能"))
        self.label.setText(_translate("works_addbutton_dialog", "功能库"))
        self.button_select_all.setText(_translate("works_addbutton_dialog", "全选"))
        self.button_yes.setText(_translate("works_addbutton_dialog", "添加"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    works_addbutton_dialog = QtWidgets.QDialog()
    ui = Ui_works_addbutton_dialog()
    ui.setupUi(works_addbutton_dialog)
    works_addbutton_dialog.show()
    sys.exit(app.exec_())