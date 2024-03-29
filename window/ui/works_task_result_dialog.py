# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'works_task_result_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_works_task_result_dialog(object):
    def setupUi(self, works_task_result_dialog):
        works_task_result_dialog.setObjectName("works_task_result_dialog")
        works_task_result_dialog.resize(615, 562)
        self.gridLayout = QtWidgets.QGridLayout(works_task_result_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(works_task_result_dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.button_collect_result = QtWidgets.QPushButton(self.widget)
        self.button_collect_result.setObjectName("button_collect_result")
        self.gridLayout_2.addWidget(self.button_collect_result, 0, 3, 1, 1)
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.button_download_result = QtWidgets.QPushButton(self.widget)
        self.button_download_result.setObjectName("button_download_result")
        self.gridLayout_2.addWidget(self.button_download_result, 0, 2, 1, 1)
        self.button_refresh = QtWidgets.QPushButton(self.widget)
        self.button_refresh.setObjectName("button_refresh")
        self.gridLayout_2.addWidget(self.button_refresh, 0, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_task_information = QtWidgets.QWidget()
        self.tab_task_information.setObjectName("tab_task_information")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_task_information)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.log_browser_task_information = QtWidgets.QTextBrowser(self.tab_task_information)
        self.log_browser_task_information.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.log_browser_task_information.setObjectName("log_browser_task_information")
        self.gridLayout_3.addWidget(self.log_browser_task_information, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_task_information, "")
        self.tab_cmd_output = QtWidgets.QWidget()
        self.tab_cmd_output.setObjectName("tab_cmd_output")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_cmd_output)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.log_browser_task_cmd_out = QtWidgets.QTextBrowser(self.tab_cmd_output)
        self.log_browser_task_cmd_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.log_browser_task_cmd_out.setObjectName("log_browser_task_cmd_out")
        self.gridLayout_4.addWidget(self.log_browser_task_cmd_out, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_cmd_output, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 5)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(works_task_result_dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(works_task_result_dialog)

    def retranslateUi(self, works_task_result_dialog):
        _translate = QtCore.QCoreApplication.translate
        works_task_result_dialog.setWindowTitle(_translate("works_task_result_dialog", "任务执行结果"))
        self.button_collect_result.setText(_translate("works_task_result_dialog", "收藏结果"))
        self.label_name.setText(_translate("works_task_result_dialog", "任务名称"))
        self.button_download_result.setText(_translate("works_task_result_dialog", "导出结果"))
        self.button_refresh.setText(_translate("works_task_result_dialog", "刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_task_information), _translate("works_task_result_dialog", "任务详情"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cmd_output), _translate("works_task_result_dialog", "命令行输出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    works_task_result_dialog = QtWidgets.QDialog()
    ui = Ui_works_task_result_dialog()
    ui.setupUi(works_task_result_dialog)
    works_task_result_dialog.show()
    sys.exit(app.exec_())
