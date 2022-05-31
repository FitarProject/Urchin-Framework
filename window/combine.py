from PyQt5.Qt import *
import json

from window.ui.combine_window import Ui_combine_window
from window.dialog.combine_openvariable import Combine_openvariable_event
from window.func.mylist_combine import Mylist_combine
from window.func.mylist_combine_selected import Mylist_selected
from window.dialog.combine_func_detatil import Combine_func_detatil_event
from window.dialog.combine_func_introduction import Combine_func_introduction_event


class Combine(QWidget, Ui_combine_window):
    signal_add_task = pyqtSignal(dict)
    signal_add_func = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.childwindow_flag_variable = False
        self.childwindow_flag_func_detatil = False
        self.childwindow_flag_func_introduction = False
        # self.setupUi(self)
        self.set_qss()

    def setupUi(self, combine_window):
        super().setupUi(combine_window)
        # with open('qss/widget_label.qss', 'r', encoding='UTF-8') as f:
        #     my_qss = f.read()
        #     self.combine_frame.setStyleSheet(my_qss)
        with open('qss/combine_window.qss', 'r', encoding='UTF-8') as f:
            my_qss = f.read()
            self.combine_frame.setStyleSheet(my_qss)
            self.selected_func.setStyleSheet(my_qss)
            self.combine_font.setStyleSheet(my_qss)
        # 绘制合成栏
        self.listWidget = Mylist_combine(self.combine_frame)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setGeometry(QRect(0, 40, 411, 341))
        self.listWidget.setMinimumSize(QSize(411, 341))
        # self.listWidget.setFrameShape(QFrame.Box)
        # self.listWidget.setFrameShadow(QFrame.Plain)
        # 绘制预置栏
        self.selected_tools = Mylist_selected(self.selected_widget, 'mytool', 'selected_tool')
        self.selected_tools.setGeometry(QRect(0, 0, 193, 111))
        self.selected_tools.setObjectName('selected_tools')
        self.selected_tunnels = Mylist_selected(self.selected_widget, 'mytunnel', 'selected_tunnel')
        self.selected_tunnels.setGeometry(QRect(194, 0, 193, 111))
        self.selected_tunnels.setObjectName('selected_tunnels')
        self.selected_components = Mylist_selected(self.selected_widget, 'mycomponent', 'selected_component')
        self.selected_components.setGeometry(QRect(388, 0, 193, 111))
        self.selected_components.setObjectName('selected_components')
        # 连接信号与槽函数
        self.listWidget.config_change.connect(self.combine_change_event)
        self.button_openvariable.clicked.connect(self.button_openvariable_event)

        self.result_func.clicked.connect(self.result_func_event)
        self.result_func_introduction.clicked.connect(self.result_func_introduction_event)

        self.combine_button_addtool.clicked.connect(self.addtool_event)
        self.combine_button_addtunnel.clicked.connect(self.addtunnel_event)
        self.combine_button_resetlayout.clicked.connect(self.resetlayout_event)

        self.selected_clear_tool.clicked.connect(self.clear_tool_event)
        self.selected_clear_tunnel.clicked.connect(self.clear_tunnel_event)
        self.selected_clear_component.clicked.connect(self.clear_component_event)

    def set_qss(self):
        pass

    # 自定义槽函数
    # 打开变量和结果集窗口
    def button_openvariable_event(self):
        self.childwindow_flag_variable = True
        # 将model绑定到变量列表和结果列表
        self.variable_and_result = Combine_openvariable_event()
        self.variable_and_result.dialog_close.connect(self.variable_close_event)
        self.variable_and_result.show()

    def variable_close_event(self):
        self.childwindow_flag_variable = False

    # 绑定结果窗口与功能详情窗口的配置刷新
    def combine_change_event(self):
        if self.childwindow_flag_variable:
            self.variable_and_result.refresh_list()
        if self.childwindow_flag_func_detatil:
            self.func_detatil.refresh_list()

    # 预置栏工具删除
    def delete_selected_tool(self, object_name):
        with open('config/selected_tool.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        value_list = []
        for selected_tool in config['selected_tool']:
            if selected_tool['button_num'] == object_name:
                value_list.append(selected_tool)
        if value_list:
            for i in value_list:
                config['selected_tool'].remove(i)
            with open('config/selected_tool.json', 'w', encoding='utf-8') as f:
                json.dump(config, f)
            self.selected_tools.refresh()

    # 预置栏通道删除
    def delete_selected_tunnel(self, object_name):
        with open('config/selected_tunnel.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        value_list = []
        for selected_tunnel in config['selected_tunnel']:
            if selected_tunnel['button_num'] == object_name:
                value_list.append(selected_tunnel)
        if value_list:
            for i in value_list:
                config['selected_tunnel'].remove(i)
            with open('config/selected_tunnel.json', '2', encoding='utf-8') as f:
                json.dump(config, f)
            self.selected_tunnels.refresh()

    # 预置栏刷新按钮
    def refresh_selected_tool(self):
        self.selected_tools = Mylist_selected(self.selected_widget, 'mytool', 'selected_tool')
        self.selected_tools.setGeometry(QRect(0, 0, 193, 111))
        self.selected_tools.setObjectName('selected_tools')

    def refresh_selected_tunnel(self):
        self.selected_tunnels = Mylist_selected(self.selected_widget, 'mytunnel', 'selected_tunnel')
        self.selected_tunnels.setGeometry(QRect(194, 0, 193, 111))
        self.selected_tunnels.setObjectName('selected_tunnels')

    def refresh_selected_component(self):
        self.selected_components = Mylist_selected(self.selected_widget, 'mycomponent', 'selected_component')
        self.selected_components.setGeometry(QRect(388, 0, 193, 111))
        self.selected_components.setObjectName('selected_components')

    # 部件添加按钮
    def addtool_event(self):
        try:
            data = {"type": 0, "button_num": "空工具", "command_num": 0, "variable": [], "variable_value": [], "result_name": [], "component": []}
            self.listWidget.button_list.append(data)
            self.listWidget.makeItem(QSize(57, 57), data)
        except Exception as e:
            print(e, 'Combine', 'addtool_event')

    def addtunnel_event(self):
        try:
            data = {"type": 1, "tunnel": [], "input_value": [], "result_name": []}
            self.listWidget.button_list.append(data)
            self.listWidget.makeItem(QSize(57, 57), data)
        except Exception as e:
            print(e, 'Combine', 'addtunnel_event')

    # 重设布局按钮
    def resetlayout_event(self):
        if self.combine_button_resetlayout.text() == '重设布局':
            self.combine_button_resetlayout.setText('完成')
            self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
            self.listWidget.setDragEnabled(True)
        else:
            self.combine_button_resetlayout.setText('重设布局')
            self.listWidget.setDragEnabled(False)
            self.listWidget.setDragDropMode(QAbstractItemView.DropOnly)
            self.listWidget.save_config()

    # 预置栏清空按钮
    def clear_tool_event(self):
        try:
            self.selected_tools.clear()
            self.selected_tools.config[self.selected_tools.config_file].clear()
            self.selected_tools.save_config()
        except Exception as e:
            print(e, 'Combine', 'clear_tool_event')

    def clear_tunnel_event(self):
        self.selected_tunnels.clear()
        self.selected_tunnels.config[self.selected_tunnels.config_file].clear()
        self.selected_tunnels.save_config()

    def clear_component_event(self):
        self.selected_components.clear()
        self.selected_components.config[self.selected_components.config_file].clear()
        self.selected_components.save_config()

    # 打开合成窗口
    def result_func_event(self):
        try:
            self.childwindow_flag_func_detatil = True
            self.func_detatil = Combine_func_detatil_event()
            self.func_detatil.dialog_close.connect(self.func_detatil_close_event)
            self.func_detatil.signal_add_task.connect(self.func_detatil_add_task_event)
            self.func_detatil.signal_add_func.connect(self.func_detatil_add_func_event)
            self.func_detatil.show()
        except Exception as e:
            print(e, 'Combine', 'result_func_event')

    def func_detatil_close_event(self):
        self.childwindow_flag_func_detatil = False

    # 执行测试任务
    def func_detatil_add_task_event(self, config):
        self.signal_add_task.emit(config)

    # 添加功能
    def func_detatil_add_func_event(self, config):
        self.signal_add_func.emit(config)
        # with open('config/combine.txt', 'w', encoding='utf-8') as f:
        #     f.write('')
        # self.listWidget.refresh()

    # 设置功能介绍窗口
    def result_func_introduction_event(self):
        try:
            self.childwindow_flag_func_introduction = True
            self.func_introduction = Combine_func_introduction_event()
            self.func_introduction.dialog_close.connect(self.func_introduction_close_event)
            self.func_introduction.signal_yes.connect(self.func_introduction_event)
            self.func_introduction.show()
        except Exception as e:
            print(e, 'Combine', 'result_func_introduction_event')

    def func_introduction_close_event(self):
        self.childwindow_flag_func_introduction = False

    # 刷新功能介绍
    def func_introduction_event(self):
        self.combine_change_event()