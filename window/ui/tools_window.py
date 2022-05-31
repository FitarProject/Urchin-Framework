# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tools_window(object):
    def setupUi(self, tools_window):
        tools_window.setObjectName("tools_window")
        tools_window.resize(586, 543)
        self.tools_font = QtWidgets.QWidget(tools_window)
        self.tools_font.setGeometry(QtCore.QRect(0, 0, 580, 540))
        self.tools_font.setStyleSheet("")
        self.tools_font.setObjectName("tools_font")
        self.tabWidget = QtWidgets.QTabWidget(self.tools_font)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 580, 491))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tools_tab_tool = QtWidgets.QWidget()
        self.tools_tab_tool.setObjectName("tools_tab_tool")
        self.tool_window = QtWidgets.QWidget(self.tools_tab_tool)
        self.tool_window.setGeometry(QtCore.QRect(0, 0, 580, 471))
        self.tool_window.setStyleSheet("")
        self.tool_window.setObjectName("tool_window")
        self.tool_label = QtWidgets.QLabel(self.tool_window)
        self.tool_label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.tool_label.setObjectName("tool_label")
        self.tool_scrollArea = QtWidgets.QScrollArea(self.tool_window)
        self.tool_scrollArea.setGeometry(QtCore.QRect(0, 30, 580, 440))
        self.tool_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tool_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tool_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tool_scrollArea.setWidgetResizable(False)
        self.tool_scrollArea.setObjectName("tool_scrollArea")
        self.scrollAreaWidgetContents_tool = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_tool.setGeometry(QtCore.QRect(0, 0, 570, 439))
        self.scrollAreaWidgetContents_tool.setObjectName("scrollAreaWidgetContents_tool")
        self.tool_scrollArea.setWidget(self.scrollAreaWidgetContents_tool)
        self.pushButton = QtWidgets.QPushButton(self.tool_window)
        self.pushButton.setGeometry(QtCore.QRect(490, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tools_tab_tool, "")
        self.tools_tab_tunnel = QtWidgets.QWidget()
        self.tools_tab_tunnel.setObjectName("tools_tab_tunnel")
        self.tunnel_window = QtWidgets.QWidget(self.tools_tab_tunnel)
        self.tunnel_window.setGeometry(QtCore.QRect(0, 0, 580, 471))
        self.tunnel_window.setStyleSheet("")
        self.tunnel_window.setObjectName("tunnel_window")
        self.tunnel_label = QtWidgets.QLabel(self.tunnel_window)
        self.tunnel_label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.tunnel_label.setObjectName("tunnel_label")
        self.tunnel_scrollArea = QtWidgets.QScrollArea(self.tunnel_window)
        self.tunnel_scrollArea.setGeometry(QtCore.QRect(0, 30, 580, 440))
        self.tunnel_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tunnel_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tunnel_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tunnel_scrollArea.setWidgetResizable(False)
        self.tunnel_scrollArea.setObjectName("tunnel_scrollArea")
        self.scrollAreaWidgetContents_tunnel = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_tunnel.setGeometry(QtCore.QRect(0, 0, 570, 439))
        self.scrollAreaWidgetContents_tunnel.setObjectName("scrollAreaWidgetContents_tunnel")
        self.tunnel_scrollArea.setWidget(self.scrollAreaWidgetContents_tunnel)
        self.tabWidget.addTab(self.tools_tab_tunnel, "")
        self.tools_tab_command = QtWidgets.QWidget()
        self.tools_tab_command.setObjectName("tools_tab_command")
        self.command_window = QtWidgets.QWidget(self.tools_tab_command)
        self.command_window.setGeometry(QtCore.QRect(0, 0, 580, 471))
        self.command_window.setStyleSheet("")
        self.command_window.setObjectName("command_window")
        self.command_label = QtWidgets.QLabel(self.command_window)
        self.command_label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.command_label.setObjectName("command_label")
        self.command_scrollArea = QtWidgets.QScrollArea(self.command_window)
        self.command_scrollArea.setGeometry(QtCore.QRect(0, 30, 580, 440))
        self.command_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.command_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.command_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.command_scrollArea.setWidgetResizable(False)
        self.command_scrollArea.setObjectName("command_scrollArea")
        self.scrollAreaWidgetContents_command = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_command.setGeometry(QtCore.QRect(0, 0, 570, 439))
        self.scrollAreaWidgetContents_command.setObjectName("scrollAreaWidgetContents_command")
        self.command_scrollArea.setWidget(self.scrollAreaWidgetContents_command)
        self.tabWidget.addTab(self.tools_tab_command, "")
        self.tools_tab_component = QtWidgets.QWidget()
        self.tools_tab_component.setObjectName("tools_tab_component")
        self.component_window = QtWidgets.QWidget(self.tools_tab_component)
        self.component_window.setGeometry(QtCore.QRect(0, 0, 580, 470))
        self.component_window.setStyleSheet("")
        self.component_window.setObjectName("component_window")
        self.component_label = QtWidgets.QLabel(self.component_window)
        self.component_label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.component_label.setObjectName("component_label")
        self.component_scrollArea = QtWidgets.QScrollArea(self.component_window)
        self.component_scrollArea.setGeometry(QtCore.QRect(0, 30, 580, 440))
        self.component_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.component_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.component_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.component_scrollArea.setWidgetResizable(False)
        self.component_scrollArea.setObjectName("component_scrollArea")
        self.scrollAreaWidgetContents_component = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_component.setGeometry(QtCore.QRect(0, 0, 570, 439))
        self.scrollAreaWidgetContents_component.setObjectName("scrollAreaWidgetContents_component")
        self.component_scrollArea.setWidget(self.scrollAreaWidgetContents_component)
        self.tabWidget.addTab(self.tools_tab_component, "")
        self.tools_menu_list = QtWidgets.QWidget(self.tools_font)
        self.tools_menu_list.setGeometry(QtCore.QRect(0, 470, 580, 71))
        self.tools_menu_list.setObjectName("tools_menu_list")
        self.tools_button_tool = QtWidgets.QPushButton(self.tools_menu_list)
        self.tools_button_tool.setGeometry(QtCore.QRect(1, 0, 145, 70))
        self.tools_button_tool.setObjectName("tools_button_tool")
        self.tools_button_tunnel = QtWidgets.QPushButton(self.tools_menu_list)
        self.tools_button_tunnel.setGeometry(QtCore.QRect(146, 0, 145, 70))
        self.tools_button_tunnel.setObjectName("tools_button_tunnel")
        self.tools_button_command = QtWidgets.QPushButton(self.tools_menu_list)
        self.tools_button_command.setGeometry(QtCore.QRect(291, 0, 145, 70))
        self.tools_button_command.setObjectName("tools_button_command")
        self.tools_button_component = QtWidgets.QPushButton(self.tools_menu_list)
        self.tools_button_component.setGeometry(QtCore.QRect(436, 0, 145, 70))
        self.tools_button_component.setObjectName("tools_button_component")

        self.retranslateUi(tools_window)
        self.tabWidget.setCurrentIndex(0)
        self.tools_button_tool.clicked.connect(self.tool_scrollArea.show)
        self.tools_button_tunnel.clicked.connect(self.tunnel_scrollArea.show)
        self.tools_button_command.clicked.connect(self.command_scrollArea.show)
        self.tools_button_component.clicked.connect(self.component_scrollArea.show)
        QtCore.QMetaObject.connectSlotsByName(tools_window)

    def retranslateUi(self, tools_window):
        _translate = QtCore.QCoreApplication.translate
        tools_window.setWindowTitle(_translate("tools_window", "工具库"))
        self.tool_label.setText(_translate("tools_window", "工具集"))
        self.pushButton.setText(_translate("tools_window", "刷新工具状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab_tool), _translate("tools_window", "1"))
        self.tunnel_label.setText(_translate("tools_window", "通道集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab_tunnel), _translate("tools_window", "Tab 2"))
        self.command_label.setText(_translate("tools_window", "命令集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab_command), _translate("tools_window", "页"))
        self.component_label.setText(_translate("tools_window", "配件集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tools_tab_component), _translate("tools_window", "页"))
        self.tools_button_tool.setText(_translate("tools_window", "工具"))
        self.tools_button_tunnel.setText(_translate("tools_window", "通道"))
        self.tools_button_command.setText(_translate("tools_window", "命令"))
        self.tools_button_component.setText(_translate("tools_window", "配件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tools_window = QtWidgets.QWidget()
    ui = Ui_tools_window()
    ui.setupUi(tools_window)
    tools_window.show()
    sys.exit(app.exec_())