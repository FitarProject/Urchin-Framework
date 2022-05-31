# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'community_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_community_window(object):
    def setupUi(self, community_window):
        community_window.setObjectName("community_window")
        community_window.resize(590, 548)
        self.widget = QtWidgets.QWidget(community_window)
        self.widget.setGeometry(QtCore.QRect(0, 0, 580, 540))
        self.widget.setObjectName("widget")
        self.share_func = QtWidgets.QPushButton(self.widget)
        self.share_func.setGeometry(QtCore.QRect(20, 480, 100, 50))
        self.share_func.setObjectName("share_func")
        self.share_tool = QtWidgets.QPushButton(self.widget)
        self.share_tool.setGeometry(QtCore.QRect(130, 480, 100, 50))
        self.share_tool.setObjectName("share_tool")
        self.share_tunnel = QtWidgets.QPushButton(self.widget)
        self.share_tunnel.setGeometry(QtCore.QRect(240, 480, 100, 50))
        self.share_tunnel.setObjectName("share_tunnel")
        self.share_command = QtWidgets.QPushButton(self.widget)
        self.share_command.setGeometry(QtCore.QRect(350, 480, 100, 50))
        self.share_command.setObjectName("share_command")
        self.share_part = QtWidgets.QPushButton(self.widget)
        self.share_part.setGeometry(QtCore.QRect(460, 480, 100, 50))
        self.share_part.setObjectName("share_part")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(370, 480, 141, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 480, 141, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_addr = QtWidgets.QLabel(self.widget)
        self.label_addr.setGeometry(QtCore.QRect(150, 10, 211, 16))
        self.label_addr.setObjectName("label_addr")
        self.button_refresh = QtWidgets.QToolButton(self.widget)
        self.button_refresh.setGeometry(QtCore.QRect(520, 7, 51, 21))
        self.button_refresh.setObjectName("button_refresh")
        self.label_status = QtWidgets.QLabel(self.widget)
        self.label_status.setGeometry(QtCore.QRect(430, 10, 81, 16))
        self.label_status.setObjectName("label_status")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 561, 431))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.button_list_widget = QtWidgets.QWidget()
        self.button_list_widget.setGeometry(QtCore.QRect(0, 0, 557, 427))
        self.button_list_widget.setObjectName("button_list_widget")
        self.scrollArea.setWidget(self.button_list_widget)
        self.button_change_server = QtWidgets.QToolButton(self.widget)
        self.button_change_server.setGeometry(QtCore.QRect(370, 7, 51, 21))
        self.button_change_server.setObjectName("button_change_server")

        self.retranslateUi(community_window)
        QtCore.QMetaObject.connectSlotsByName(community_window)

    def retranslateUi(self, community_window):
        _translate = QtCore.QCoreApplication.translate
        community_window.setWindowTitle(_translate("community_window", "社区"))
        self.share_func.setText(_translate("community_window", "分享功能"))
        self.share_tool.setText(_translate("community_window", "分享工具"))
        self.share_tunnel.setText(_translate("community_window", "分享通道"))
        self.share_command.setText(_translate("community_window", "分享命令"))
        self.share_part.setText(_translate("community_window", "分享配件"))
        self.label.setText(_translate("community_window", "共享社区"))
        self.label_2.setText(_translate("community_window", "其他分享功能暂未开放"))
        self.label_3.setText(_translate("community_window", "其他分享功能暂未开放"))
        self.label_addr.setText(_translate("community_window", "addr:"))
        self.button_refresh.setText(_translate("community_window", "刷新"))
        self.label_status.setText(_translate("community_window", "状态："))
        self.button_change_server.setText(_translate("community_window", "更改"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    community_window = QtWidgets.QWidget()
    ui = Ui_community_window()
    ui.setupUi(community_window)
    community_window.show()
    sys.exit(app.exec_())