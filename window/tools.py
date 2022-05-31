from PyQt5.Qt import *
from string import Template
import subprocess, json, logging

from window.ui.tools_window import Ui_tools_window
from window.dialog.tools_buttons_tool import Tools_buttons_tool_event
from window.dialog.tools_buttons_addtool import Tools_buttons_addtool_event
from window.dialog.tools_buttons_tunnel import Tools_buttons_tunnel_event
from window.dialog.tools_buttons_addtunnel import Tools_buttons_addtunnel_event
from window.dialog.tools_buttons_command import Tools_buttons_command_event
from window.dialog.tools_buttons_addcommand import Tools_buttons_addcommand_event
from window.dialog.tools_tunnel_edit_script import Tools_tunnel_edit_script_event
from window.dialog.tools_tunnel_edit_customscript import Tools_tunnel_edit_customscript_event
from window.paint.button_record import Button_list
from window.func.mybutton_command import Mybutton_command
from window.func.get_cmd_out import cmd_exec


class Tools(QWidget, Ui_tools_window):
    refresh_selected_tool = pyqtSignal()
    refresh_selected_tunnel = pyqtSignal()
    del_selected_tool = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        # 子窗口状态信号
        self.childwindow_flag_toolbutton = False
        self.childwindow_flag_addtoolbutton = False
        self.childwindow_flag_tunnelbutton = False
        self.childwindow_flag_addtunnelbutton = False
        self.childwindow_flag_tunnel_script = False
        self.childwindow_flag_commandbutton = False
        self.childwindow_flag_addcommandbutton = False
        # 右键菜单所指按钮
        self.rightmenu_curr = ''

    def setupUi(self, tools_window):
        super().setupUi(tools_window)
        self.pushButton.hide()
        with open('qss/toolsMenuList.qss', 'r', encoding='UTF-8') as f:
            self.tools_menu_list.setStyleSheet(f.read())
        with open('qss/tools_window.qss', 'r', encoding='UTF-8') as f:
            style = f.read()
            self.tool_window.setStyleSheet(style)
            self.tunnel_window.setStyleSheet(style)
            self.command_window.setStyleSheet(style)
            self.component_window.setStyleSheet(style)
        with open('qss/tools_scrollArea.qss', 'r', encoding='UTF-8') as f:
            style = f.read()
            self.tool_scrollArea.setStyleSheet(style)
            self.tunnel_scrollArea.setStyleSheet(style)
            self.command_scrollArea.setStyleSheet(style)
            self.component_scrollArea.setStyleSheet(style)
        # 初始化按钮字典
        self.tool_button = {}
        self.tunnel_button = {}
        self.command_button = {}
        self.component_button = {}
        self.dict_to_button_tool = {}
        self.dict_to_button_tunnel = {}
        self.dict_to_button_command = {}
        self.dict_to_button_component = {}
        self.button_list_tool = Button_list(10, 10, 70, 70, 50, 50, 570, 5800)
        self.button_list_tunnel = Button_list(10, 10, 70, 70, 50, 50, 570, 5800)
        self.button_list_command = Button_list(10, 10, 70, 70, 50, 50, 570, 5800)
        self.button_list_component = Button_list(10, 10, 70, 70, 50, 50, 570, 5800)
        # self.scrollAreaWidgetContents_tool.setGeometry(0, 0, 560, 440)
        # 读取所有按钮信息并绘制
        self.read_config_tool('tools_buttons_tool.json')
        self.read_config_tunnel('tools_buttons_tunnel.json')
        self.read_config_command('tools_buttons_command.json')
        self.read_config_component('tools_buttons_component.json')
        self.buttons_paint()
        # 设置右键菜单
        # self.scrollAreaWidgetContents_tool.setContextMenuPolicy(Qt.CustomContextMenu)
        # 设置最初展示界面
        self.tabWidget.setCurrentIndex(0)
        # 连接信号与槽函数
        self.tools_button_tool.clicked.connect(self.show_tab_window)
        self.tools_button_tunnel.clicked.connect(self.show_tab_window)
        self.tools_button_command.clicked.connect(self.show_tab_window)
        self.tools_button_component.clicked.connect(self.show_tab_window)

    # 点击下侧按钮切换界面信号
    def show_tab_window(self):
        dic = {
            "tools_button_tool": 0,
            "tools_button_tunnel": 1,
            "tools_button_command": 2,
            "tools_button_component": 3,
        }
        index = dic[self.sender().objectName()]
        self.tabWidget.setCurrentIndex(index)

    # 绘制按钮
    def buttons_paint(self):
        # 绘制工具栏按钮
        for button_object_name, button_config in self.dict_to_button_tool.items():
            try:
                x, y, width, height = self.button_list_tool.add_button(button_object_name)
                self.tool_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_tool)
                self.tool_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.tool_button[button_object_name].setObjectName(button_object_name)
                self.tool_button[button_object_name].setText(button_config['simple_name'])
                self.tool_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                self.tool_button[button_object_name].setVisible(True)
                if button_object_name == 'button_add':
                    self.tool_button[button_object_name].clicked.connect(self.tool_buttons_add_event)
                else:
                    self.tool_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
                    self.tool_button[button_object_name].clicked.connect(self.tool_buttons_clicked_event)
                    self.tool_button[button_object_name].customContextMenuRequested.connect(self.tool_rightmenu_event)
            except Exception as e:
                print(e, 'buttons_paint tools_tool', 'Tools')
        # 绘制通道栏按钮
        for button_object_name, button_config in self.dict_to_button_tunnel.items():
            try:
                x, y, width, height = self.button_list_tunnel.add_button(button_object_name)
                self.tunnel_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_tunnel)
                self.tunnel_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.tunnel_button[button_object_name].setObjectName(button_object_name)
                self.tunnel_button[button_object_name].setText(button_config['name'])
                self.tunnel_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                self.tunnel_button[button_object_name].setVisible(True)
                if button_object_name == 'button_add':
                    self.tunnel_button[button_object_name].clicked.connect(self.tunnel_buttons_add_event)
                else:
                    self.tunnel_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
                    self.tunnel_button[button_object_name].clicked.connect(self.tunnel_buttons_clicked_event)
                    self.tunnel_button[button_object_name].customContextMenuRequested.connect(self.tunnel_rightmenu_event)
            except Exception as e:
                print(e, 'buttons_paint tools_tunnel', 'Tools')
        # 绘制命令栏按钮
        for button_object_name, button_config in self.dict_to_button_command.items():
            try:
                x, y, width, height = self.button_list_command.add_button(button_object_name)
                self.command_button[button_object_name] = Mybutton_command(self.scrollAreaWidgetContents_command)
                self.command_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.command_button[button_object_name].setObjectName(button_object_name)
                self.command_button[button_object_name].setText(button_config['name'])
                self.command_button[button_object_name].setToolTip('名称：' + button_config['name'] + '\n' + '命令：' + button_config['command'])
                self.command_button[button_object_name].setVisible(True)
                if button_object_name == 'button_add':
                    self.command_button[button_object_name].clicked.connect(self.command_buttons_add_event)
                    self.command_button[button_object_name].setToolTip('添加')
                else:
                    self.command_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
                    self.command_button[button_object_name].double_clicked.connect(self.command_buttons_double_clicked_event)
                    self.command_button[button_object_name].clicked.connect(self.command_buttons_clicked_event)
                    self.command_button[button_object_name].customContextMenuRequested.connect(self.command_rightmenu_event)
            except Exception as e:
                print(e, 'buttons_paint tools_command', 'Tools')
        # 绘制配件栏按钮
        for button_object_name, button_config in self.dict_to_button_component.items():
            try:
                pass
                # x, y, width, height = self.button_list_component.add_button(button_object_name)
                # self.component_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_component)
                # self.component_button[button_object_name].setGeometry(QRect(x, y, width, height))
                # self.component_button[button_object_name].setObjectName(button_object_name)
                # self.component_button[button_object_name].setText(button_config['simple_name'])
                # self.component_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                # self.component_button[button_object_name].setVisible(True)
                # if button_object_name == 'button_add':
                #     self.component_button[button_object_name].clicked.connect(self.component_buttons_add_event)
                # else:
                #     self.component_button[button_object_name].clicked.connect(self.component_buttons_clicked_event)
            except Exception as e:
                print(e, 'buttons_paint tools_component', 'Tools')

    ################################################################################
    ###############################       tool       ###############################
    ################################################################################
    # 读取配置文件
    def read_config_tool(self, filename):
        with open('config/' + filename, 'r', encoding='utf-8') as f:
            self.dict_to_button_tool = json.load(f)
            self.dict_to_button_tool['button_add'] = {
                'name': '添加',
                'simple_name': '添加',
                "folder": "",
                "filename": "",
                'introduction': '',
                "command_template": [],
                "command_introduction": [],
                "command_example": [],
                "command_built_in": [],
                "result": [],
            }

    # 保存配置文件
    def save_config_tool(self, filename):
        del self.dict_to_button_tool['button_add']
        with open('config/' + filename, 'w', encoding='utf-8') as f:
            json.dump(self.dict_to_button_tool, f)
        self.dict_to_button_tool['button_add'] = {
                'name': '添加',
                'simple_name': '添加',
                "folder": "",
                "filename": "",
                'introduction': '',
                "command_template": [],
                "command_introduction": [],
                "command_example": [],
                "command_built_in": [],
                "result": [],
            }

    # 右键菜单
    def tool_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()
            self.tool_rightmenu = QMenu(self)
            self.tool_action_edit = QAction(QIcon('resource/image/edit.png'), u'编辑', self)
            self.tool_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.tool_action_task = QAction(QIcon('resource/image/task.png'), u'添加至任务', self)
            self.tool_action_selected = QAction(QIcon('resource/image/combine.png'), u'添加至炼金', self)
            self.tool_action_func = QAction(QIcon('resource/image/func.png'), u'添加至功能', self)
            # self.tool_action_save.setShortcut('Ctrl+S')  # 设置动作A的快捷键
            self.tool_rightmenu.addAction(self.tool_action_edit)
            self.tool_rightmenu.addAction(self.tool_action_delete)
            self.tool_rightmenu.addAction(self.tool_action_task)
            self.tool_rightmenu.addAction(self.tool_action_selected)
            self.tool_rightmenu.addAction(self.tool_action_func)
            self.tool_action_edit.triggered.connect(self.tool_action_edit_event)
            self.tool_action_delete.triggered.connect(self.tool_action_delete_event)
            self.tool_action_task.triggered.connect(self.tool_action_task_event)
            self.tool_action_selected.triggered.connect(self.tool_action_selected_event)
            self.tool_action_func.triggered.connect(self.tool_action_func_event)

            self.tool_rightmenu.popup(QCursor.pos())  # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以，
        except Exception as e:
            print(e, 'tool_rightmenu_event', 'Tools')

    # 工具按钮重绘制
    def tool_buttons_repaint(self):
        try:
            # 保存配置
            self.save_config_tool('tools_buttons_tool.json')
            # 工具按钮位置重置
            for button_object_name in self.dict_to_button_tool.keys():
                x, y = self.button_list_tool.get_button_position(button_object_name)
                width, height = self.button_list_tool.width, self.button_list_tool.height
                self.tool_button[button_object_name].setText(self.dict_to_button_tool[button_object_name]['simple_name'])
                self.tool_button[button_object_name].setToolTip('<html><head/><body><p>' + self.dict_to_button_tool[button_object_name]['name'] + '</p></body></html>')
                self.tool_button[button_object_name].setGeometry(QRect(x, y, width, height))
            # 刷新界面
            self.scrollAreaWidgetContents_tool.update()
        except Exception as e:
            print(e, 'tool_buttons_repaint', 'Tools')

    # 自定义槽函数
    # 有按钮配置变动，刷新配置事件
    def tool_refresh_event(self, object_name, object_dict, subitem_name):
        if subitem_name == 'all':
            self.dict_to_button_tool[object_name] = object_dict
            self.save_config_tool('tools_buttons_tool.json')
        else:
            try:
                self.dict_to_button_tool[object_name][subitem_name] = object_dict[subitem_name]
                self.save_config_tool('tools_buttons_tool.json')
            except Exception as e:
                print(e, 'subitem_name error!', 'Tools')
        self.tool_buttons_repaint()

    # 按钮添加事件
    def addtool_add_event(self, button_config):
        try:
            # 获取新按钮编号
            num = int(self.button_list_tool.get_button_list()[-2].split('_')[-1]) + 1
            button_object_name = 'button_' + str(num)
            # 添加进按钮字典并保存配置
            self.dict_to_button_tool[button_object_name] = button_config
            # 获取按钮坐标并绘制
            self.button_list_tool.remove_button('button_add')
            x, y, width, height = self.button_list_tool.add_button(button_object_name)
            self.button_list_tool.add_button('button_add')
            self.tool_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_tool)
            self.tool_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.tool_button[button_object_name].setObjectName(button_object_name)
            self.tool_button[button_object_name].setText(button_config['simple_name'])
            self.tool_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
            self.tool_button[button_object_name].setVisible(True)
            self.tool_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
            self.tool_button[button_object_name].clicked.connect(self.tool_buttons_clicked_event)
            self.tool_button[button_object_name].customContextMenuRequested.connect(self.tool_rightmenu_event)
            # 重新绘制所有按钮
            self.tool_buttons_repaint()
        except Exception as e:
            print(e, 'addtool_add_event', 'Tools')

    # 子窗口关闭
    def tool_close_event(self, close_flag):
        if close_flag:
            self.childwindow_flag_toolbutton = False

    def addtool_close_event(self):
        self.childwindow_flag_addtoolbutton = False

    # 点击工具栏的按钮
    def tool_buttons_clicked_event(self):
        try:
            self.tool_buttons = Tools_buttons_tool_event(self.sender().objectName(), self.dict_to_button_tool[self.sender().objectName()])
            self.childwindow_flag_toolbutton = True
            self.tool_buttons.tool_refresh.connect(self.tool_refresh_event)
            self.tool_buttons.tool_close.connect(self.tool_close_event)
            self.tool_buttons.refresh_selected_tool.connect(self.refresh_selected_tool_event)
            self.tool_buttons.show()
        except Exception as e:
            print(e, 'tool_buttons_clicked_event', 'Tools')

    # 工具栏的添加按钮
    def tool_buttons_add_event(self):
        try:
            self.tool_addbuttons = Tools_buttons_addtool_event()
            self.childwindow_flag_addtoolbutton = True
            self.tool_addbuttons.tool_add.connect(self.addtool_add_event)
            self.tool_addbuttons.tool_close.connect(self.addtool_close_event)
            self.tool_addbuttons.show()
        except Exception as e:
            print(e, 'tool_buttons_add_event', 'Tools')

    # 右键菜单动作函数
    def tool_action_edit_event(self):
        try:
            self.tool_buttons = Tools_buttons_tool_event(self.rightmenu_curr, self.dict_to_button_tool[self.rightmenu_curr])
            self.childwindow_flag_toolbutton = True
            self.tool_buttons.tool_refresh.connect(self.tool_refresh_event)
            self.tool_buttons.tool_close.connect(self.tool_close_event)
            self.tool_buttons.refresh_selected_tool.connect(self.refresh_selected_tool_event)
            self.tool_buttons.show()
        except Exception as e:
            print(e, 'tool_action_edit_event', 'Tools')

    def tool_action_delete_event(self):
        if QMessageBox.warning(self, "操作警告", '是否删除这个工具？\n该操作不可恢复！', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            try:
                # 在按钮配置字典中删除
                del self.dict_to_button_tool[self.rightmenu_curr]
                # 在坐标类中删除
                self.button_list_tool.remove_button(self.rightmenu_curr)
                # 在按钮绘制字典中删除
                self.tool_button[self.rightmenu_curr].deleteLater()
                del self.tool_button[self.rightmenu_curr]
                # 保存配置并重新绘制
                self.tool_buttons_repaint()
                # 预选区域删除按钮
                self.del_selected_tool.emit(self.rightmenu_curr)
            except Exception as e:
                print(e, 'tool_action_delete_event', 'Tools')

    def tool_action_task_event(self):
        print(self.rightmenu_curr)
        pass

    def tool_action_selected_event(self):
        try:
            index = 0
            if QMessageBox.warning(self, "操作确认", '是否添加工具命令\n"' + self.dict_to_button_tool[self.rightmenu_curr]['command_template'][index] + '"\n至炼金工坊预选区域？', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                config = {"name": self.dict_to_button_tool[self.rightmenu_curr]['name'], "button_num": self.rightmenu_curr, "command_num": index}
                with open('config/selected_tool.json', 'r', encoding='utf-8') as f:
                    selected_tool = json.load(f)
                selected_tool['selected_tool'].append(config)
                with open('config/selected_tool.json', 'w', encoding='utf-8') as f:
                    json.dump(selected_tool, f)
                self.refresh_selected_tool.emit()
        except Exception as e:
            print(e, 'tool_action_selected_event', 'Tools')

    def tool_action_func_event(self):
        print(self.rightmenu_curr)
        pass

    def refresh_selected_tool_event(self):
        self.refresh_selected_tool.emit()

    ################################################################################
    ###############################      tunnel      ###############################
    ################################################################################
    # 读取配置文件
    def read_config_tunnel(self, filename):
        try:
            with open('config/' + filename, 'r', encoding='utf-8') as f:
                self.dict_to_button_tunnel = json.load(f)
                self.dict_to_button_tunnel['button_add'] = {
                    "name": "添加",
                    "position": '',
                    "input": [],
                    "output": ["output_1"],
                    "introduction": "",
                }
        except Exception as e:
            print(e, 'read_config_tunnel', 'Tools')

    def save_config_tunnel(self, filename):
        try:
            del self.dict_to_button_tunnel['button_add']
            with open('config/' + filename, 'w', encoding='utf-8') as f:
                json.dump(self.dict_to_button_tunnel, f)
            self.dict_to_button_tunnel['button_add'] = {
                    "name": "添加",
                    "position": '',
                    "input": [],
                    "output": ["output_1"],
                    "introduction": "",
                }
        except Exception as e:
            print(e, 'save_config_tunnel', 'Tools')

    # 右键菜单
    def tunnel_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()
            self.tunnel_rightmenu = QMenu(self)
            self.tunnel_action_edit = QAction(QIcon('resource/image/edit.png'), u'编辑', self)
            self.tunnel_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.tunnel_action_script = QAction(QIcon('resource/image/script.png'), u'查看脚本', self)
            self.tunnel_action_selected = QAction(QIcon('resource/image/combine.png'), u'添加至炼金', self)
            self.tunnel_rightmenu.addAction(self.tunnel_action_edit)
            self.tunnel_rightmenu.addAction(self.tunnel_action_delete)
            self.tunnel_rightmenu.addAction(self.tunnel_action_script)
            self.tunnel_rightmenu.addAction(self.tunnel_action_selected)
            self.tunnel_action_edit.triggered.connect(self.tunnel_action_edit_event)
            self.tunnel_action_delete.triggered.connect(self.tunnel_action_delete_event)
            self.tunnel_action_script.triggered.connect(self.tunnel_action_script_event)
            self.tunnel_action_selected.triggered.connect(self.tunnel_action_selected_event)

            self.tunnel_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'tunnel_rightmenu_event', 'Tools')

    # 通道按钮重绘制
    def tunnel_buttons_repaint(self):
        try:
            # 保存配置
            self.save_config_tunnel('tools_buttons_tunnel.json')
            # 工具按钮位置重置
            for button_object_name in self.dict_to_button_tunnel.keys():
                x, y = self.button_list_tunnel.get_button_position(button_object_name)
                width, height = self.button_list_tunnel.width, self.button_list_tunnel.height
                self.tunnel_button[button_object_name].setText(self.dict_to_button_tunnel[button_object_name]['name'])
                self.tunnel_button[button_object_name].setToolTip('<html><head/><body><p>' + self.dict_to_button_tunnel[button_object_name]['name'] + '</p></body></html>')
                self.tunnel_button[button_object_name].setGeometry(QRect(x, y, width, height))
            # 刷新界面
            self.scrollAreaWidgetContents_tunnel.update()
        except Exception as e:
            print(e, 'tunnel_buttons_repaint', 'Tools')

    # 自定义槽函数
    # 有按钮配置变动，刷新配置事件
    def tunnel_refresh_event(self, object_name, object_dict, subitem_name):
        try:
            if subitem_name == 'all':
                self.dict_to_button_tunnel[object_name] = object_dict
                self.save_config_tunnel('tools_buttons_tunnel.json')
            else:
                try:
                    self.dict_to_button_tunnel[object_name][subitem_name] = object_dict[subitem_name]
                    self.save_config_tunnel('tools_buttons_tunnel.json')
                except Exception as e:
                    print(e, 'subitem_name error!', 'Tools')
            self.tunnel_buttons_repaint()
        except Exception as e:
            print(e, 'tunnel_refresh_event', 'Tools')

    # 按钮添加事件
    def addtunnel_add_event(self, button_config):
        try:
            # 获取新按钮编号
            num = int(self.button_list_tunnel.get_button_list()[-2].split('_')[-1]) + 1
            button_object_name = 'button_' + str(num)
            # 添加进按钮字典并保存配置
            self.dict_to_button_tunnel[button_object_name] = button_config
            # 获取按钮坐标并绘制
            self.button_list_tunnel.remove_button('button_add')
            x, y, width, height = self.button_list_tunnel.add_button(button_object_name)
            self.button_list_tunnel.add_button('button_add')
            self.tunnel_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_tunnel)
            self.tunnel_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.tunnel_button[button_object_name].setObjectName(button_object_name)
            self.tunnel_button[button_object_name].setText(button_config['name'])
            self.tunnel_button[button_object_name].setToolTip(
                '<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
            self.tunnel_button[button_object_name].setVisible(True)
            self.tunnel_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
            self.tunnel_button[button_object_name].clicked.connect(self.tunnel_buttons_clicked_event)
            self.tunnel_button[button_object_name].customContextMenuRequested.connect(self.tunnel_rightmenu_event)
            # 重新绘制所有按钮
            self.tunnel_buttons_repaint()
        except Exception as e:
            print(e, 'addtunnel_add_event', 'Tools')

    # 子窗口关闭
    def tunnel_close_event(self):
        self.childwindow_flag_tunnelbutton = False

    def addtunnel_close_event(self):
        self.childwindow_flag_addtunnelbutton = False

    def tunnel_script_close(self):
        self.childwindow_flag_tunnel_script = False

    # 点击通道栏的按钮
    def tunnel_buttons_clicked_event(self):
        try:
            self.tunnel_buttons = Tools_buttons_tunnel_event(self.sender().objectName(), self.dict_to_button_tunnel[self.sender().objectName()])
            self.childwindow_flag_tunnelbutton = True
            self.tunnel_buttons.tunnel_refresh.connect(self.tunnel_refresh_event)
            self.tunnel_buttons.tunnel_close.connect(self.tunnel_close_event)
            self.tunnel_buttons.refresh_selected_tunnel.connect(self.refresh_selected_tunnel_event)
            self.tunnel_buttons.show()
        except Exception as e:
            print(e, 'tunnel_buttons_clicked_event', 'Tools')

    # 通道栏的添加按钮
    def tunnel_buttons_add_event(self):
        try:
            self.tunnel_addbuttons = Tools_buttons_addtunnel_event()
            self.childwindow_flag_addtunnelbutton = True
            self.tunnel_addbuttons.tunnel_add.connect(self.addtunnel_add_event)
            self.tunnel_addbuttons.tunnel_close.connect(self.addtunnel_close_event)
            self.tunnel_addbuttons.show()
        except Exception as e:
            print(e, 'tunnel_buttons_add_event', 'Tools')

    # 右键菜单动作函数
    def tunnel_action_edit_event(self):
        try:
            self.tunnel_buttons = Tools_buttons_tunnel_event(self.rightmenu_curr, self.dict_to_button_tunnel[self.rightmenu_curr])
            self.childwindow_flag_tunnelbutton = True
            self.tunnel_buttons.tunnel_refresh.connect(self.tunnel_refresh_event)
            self.tunnel_buttons.tunnel_close.connect(self.tunnel_close_event)
            self.tunnel_buttons.refresh_selected_tunnel.connect(self.refresh_selected_tunnel_event)
            self.tunnel_buttons.show()
        except Exception as e:
            print(e, 'tunnel_action_edit_event', 'Tools')

    def tunnel_action_delete_event(self):
        if QMessageBox.warning(self, "操作警告", '是否删除这个通道？\n该操作不可恢复！',
                               QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            try:
                # 在按钮配置字典中删除
                del self.dict_to_button_tunnel[self.rightmenu_curr]
                # 在坐标类中删除
                self.button_list_tunnel.remove_button(self.rightmenu_curr)
                # 在按钮绘制字典中删除
                self.tunnel_button[self.rightmenu_curr].deleteLater()
                del self.tunnel_button[self.rightmenu_curr]
                # 保存配置并重新绘制
                self.tunnel_buttons_repaint()
            except Exception as e:
                print(e, 'tunnel_action_delete_event', 'Tools')

    def tunnel_action_script_event(self):
        try:
            if self.childwindow_flag_tunnelbutton:
                self.tunnel_buttons.close()
                self.childwindow_flag_tunnelbutton = False
            if self.dict_to_button_tunnel[self.rightmenu_curr]['position'].startswith('./script/'):
                self.tunnel_edit_script = Tools_tunnel_edit_script_event(self.dict_to_button_tunnel[self.rightmenu_curr]['position'])
                self.childwindow_flag_tunnel_script = True
                self.tunnel_edit_script.script_close.connect(self.tunnel_script_close)
                self.tunnel_edit_script.show()
            else:
                self.tunnel_edit_script = Tools_tunnel_edit_customscript_event(self.dict_to_button_tunnel[self.rightmenu_curr]['position'])
                self.childwindow_flag_tunnel_script = True
                self.tunnel_edit_script.script_close.connect(self.tunnel_script_close)
                self.tunnel_edit_script.show()
        except Exception as e:
            print(e, 'tunnel_action_script_event', 'Tools')

    def tunnel_action_selected_event(self):
        try:
            if QMessageBox.warning(self, "操作确认", '是否添加通道\n"' + self.dict_to_button_tunnel[self.rightmenu_curr]['name'] + '"\n至炼金工坊预选区域？', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                config = {"name": self.dict_to_button_tunnel[self.rightmenu_curr]['name'], "button_num": self.rightmenu_curr}
                with open('config/selected_tunnel.json', 'r', encoding='utf-8') as f:
                    selected_tunnel = json.load(f)
                selected_tunnel['selected_tunnel'].append(config)
                with open('config/selected_tunnel.json', 'w', encoding='utf-8') as f:
                    json.dump(selected_tunnel, f)
                self.refresh_selected_tunnel.emit()
        except Exception as e:
            print(e, 'tunnel_action_selected_event', 'Tools')

    def refresh_selected_tunnel_event(self):
        self.refresh_selected_tunnel.emit()

    ################################################################################
    ###############################      command      ###############################
    ################################################################################
    # 读取配置文件
    def read_config_command(self, filename):
        with open('config/' + filename, 'r', encoding='utf-8') as f:
            self.dict_to_button_command = json.load(f)
            self.dict_to_button_command['button_add'] = {
                "name": "添加",
                "introduction": "",
                "command": "",
                "variable": []
            }

    def save_config_command(self, filename):
        try:
            del self.dict_to_button_command['button_add']
            with open('config/' + filename, 'w', encoding='utf-8') as f:
                json.dump(self.dict_to_button_command, f)
            # print('保存配置：', self.dict_to_button_command)
            self.dict_to_button_command['button_add'] = {
                "name": "添加",
                "introduction": "",
                "command": "",
                "variable": []
            }
        except Exception as e:
            print(e, 'save_config_command', 'Tools')

    # 右键菜单
    def command_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()
            self.command_rightmenu = QMenu(self)
            self.command_action_exec = QAction(QIcon('resource/image/exec.png'), u'执行', self)
            self.command_action_edit = QAction(QIcon('resource/image/edit.png'), u'编辑', self)
            self.command_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.command_action_crontab = QAction(QIcon('resource/image/crontab.png'), u'定时执行', self)
            self.command_rightmenu.addAction(self.command_action_exec)
            self.command_rightmenu.addAction(self.command_action_edit)
            self.command_rightmenu.addAction(self.command_action_delete)
            self.command_rightmenu.addAction(self.command_action_crontab)
            self.command_action_exec.triggered.connect(self.command_action_exec_event)
            self.command_action_edit.triggered.connect(self.command_action_edit_event)
            self.command_action_delete.triggered.connect(self.command_action_delete_event)
            self.command_action_crontab.triggered.connect(self.command_action_crontab_event)

            self.command_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'command_rightmenu', 'Tools')

    # 命令按钮重绘制
    def command_buttons_repaint(self):
        try:
            # 保存配置
            self.save_config_command('tools_buttons_command.json')
            # 工具按钮位置重置
            for button_object_name in self.dict_to_button_command.keys():
                x, y = self.button_list_command.get_button_position(button_object_name)
                width, height = self.button_list_command.width, self.button_list_command.height
                self.command_button[button_object_name].setText(self.dict_to_button_command[button_object_name]['name'])
                if button_object_name == 'button_add':
                    self.command_button[button_object_name].setToolTip('添加')
                else:
                    self.command_button[button_object_name].setToolTip('名称：' + self.dict_to_button_command[button_object_name]['name'] + '\n' + '命令：' + self.dict_to_button_command[button_object_name]['command'])
                self.command_button[button_object_name].setGeometry(QRect(x, y, width, height))
            # 刷新界面
            self.scrollAreaWidgetContents_command.update()
        except Exception as e:
            print(e, 'command_buttons_repaint', 'Tools')

    # 有按钮配置变动，刷新配置事件
    def command_refresh_event(self, object_name, object_dict, subitem_name):
        try:
            if subitem_name == 'all':
                self.dict_to_button_command[object_name] = object_dict
                self.save_config_command('tools_buttons_command.json')
            else:
                try:
                    self.dict_to_button_command[object_name][subitem_name] = object_dict[subitem_name]
                    self.save_config_command('tools_buttons_command.json')
                except Exception as e:
                    print(e, 'subitem_name error!', 'Tools')
            self.command_buttons_repaint()
        except Exception as e:
            print(e, 'command_refresh_event', 'Tools')

    # 按钮添加事件
    def addcommand_add_event(self, button_config):
        try:
            # 获取新按钮编号
            num = int(self.button_list_command.get_button_list()[-2].split('_')[-1]) + 1
            button_object_name = 'button_' + str(num)
            # 添加进按钮字典并保存配置
            self.dict_to_button_command[button_object_name] = button_config
            # 获取按钮坐标并绘制
            self.button_list_command.remove_button('button_add')
            x, y, width, height = self.button_list_command.add_button(button_object_name)
            self.button_list_command.add_button('button_add')
            self.command_button[button_object_name] = Mybutton_command(self.scrollAreaWidgetContents_command)
            self.command_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.command_button[button_object_name].setObjectName(button_object_name)
            self.command_button[button_object_name].setText(button_config['name'])
            self.command_button[button_object_name].setToolTip('名称：' + button_config['name'] + '\n' + '命令：' + button_config['command'])
            self.command_button[button_object_name].setVisible(True)
            self.command_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
            self.command_button[button_object_name].double_clicked.connect(self.command_buttons_double_clicked_event)
            self.command_button[button_object_name].clicked.connect(self.command_buttons_clicked_event)
            self.command_button[button_object_name].customContextMenuRequested.connect(self.command_rightmenu_event)
            # 重新绘制所有按钮
            self.command_buttons_repaint()
        except Exception as e:
            print(e, 'addcommand_add_event', 'Tools')

    # 子窗口关闭
    def command_close_event(self):
        self.childwindow_flag_commandbutton = False

    def addcommand_close_event(self):
        self.childwindow_flag_addcommandbutton = False

    # 点击命令栏的按钮
    def command_buttons_clicked_event(self):
        try:
            # print(self.sender().objectName())
            # 具体作用待定
            pass
            # self.command_buttons = Tools_buttons_command_event(self.sender().objectName(),
            #                                                    self.dict_to_button_command[self.sender().objectName()])
            # self.childwindow_flag_commandbutton = True
            # self.command_buttons.command_refresh.connect(self.command_refresh_event)
            # self.command_buttons.command_close.connect(self.command_close_event)
            # self.command_buttons.show()
        except Exception as e:
            print(e, 'command_buttons_clicked_event', 'Tools')

    # 双击命令栏按钮
    def command_buttons_double_clicked_event(self, button_object_name):
        try:
            pass
            var_map = {}
            button_config = self.dict_to_button_command[button_object_name]
            variable_index = []
            for i in button_config['variable']:
                variable_index.append('variable_' + str(button_config['variable'].index(i) + 1))
            # 暂时定为直接打开新终端执行命令
            for i,j in zip(variable_index, button_config['variable']):
                var_map[i] = j
            command = Template(button_config['command']).safe_substitute(var_map)
            # print('正在执行', command)
            # try:
            #     proc = subprocess.Popen(command, shell=False, cwd='./')
            #     proc.wait()
            # except Exception as e:
            #     print('命令' + command + '执行异常！', e)
            # 模拟终端？？？
            _logger_trans = {
                "DEBUG": "DBG",
                "INFO": "INF",
                "WARNING": "WAR",
                "CRITICAL": "ERR"
            }
            _old_factory = logging.getLogRecordFactory()

            def factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None,
                        **kwargs) -> logging.LogRecord:
                record = _old_factory(name, level, fn, lno, msg, args, exc_info, func, sinfo, **kwargs)
                record.shortlevelname = _logger_trans[record.levelname]
                return record

            logging.setLogRecordFactory(factory)
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(message)s',
            )
            cmd_exec(command, ensure_success=False)
        except Exception as e:
            print(e, 'command_buttons_double_clicked_event', 'Tools')

    # 命令栏的添加按钮
    def command_buttons_add_event(self):
        try:
            self.command_addbuttons = Tools_buttons_addcommand_event()
            self.childwindow_flag_addcommandbutton = True
            self.command_addbuttons.command_add.connect(self.addcommand_add_event)
            self.command_addbuttons.command_close.connect(self.addcommand_close_event)
            self.command_addbuttons.show()
        except Exception as e:
            print(e, 'command_buttons_add_event', 'Tools')

    # 右键菜单动作函数
    def command_action_exec_event(self):
        try:
            pass
            var_map = {}
            variable_index = []
            button_config = self.dict_to_button_command[self.rightmenu_curr]
            for i in button_config['variable']:
                variable_index.append('variable_' + str(button_config['variable'].index(i) + 1))
            # 暂时定为直接打开新终端执行命令
            for i,j in zip(variable_index, button_config['variable']):
                var_map[i] = j
            command = Template(button_config['command']).safe_substitute(var_map)
            # print('正在执行', command)
            # try:
            #     proc = subprocess.Popen(command, shell=False, cwd='./')
            #     proc.wait()
            # except Exception as e:
            #     print('命令' + command + '执行异常！', e)
            # 模拟终端？？？
            _logger_trans = {
                "DEBUG": "DBG",
                "INFO": "INF",
                "WARNING": "WAR",
                "CRITICAL": "ERR"
            }
            _old_factory = logging.getLogRecordFactory()

            def factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None,
                        **kwargs) -> logging.LogRecord:
                record = _old_factory(name, level, fn, lno, msg, args, exc_info, func, sinfo, **kwargs)
                record.shortlevelname = _logger_trans[record.levelname]
                return record

            logging.setLogRecordFactory(factory)
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(message)s',
            )
            cmd_exec(command, ensure_success=False)
        except Exception as e:
            print(e, 'command_action_exec_event', 'Tools')

    def command_action_edit_event(self):
        try:
            self.command_buttons = Tools_buttons_command_event(self.rightmenu_curr,
                                                               self.dict_to_button_command[self.rightmenu_curr])
            self.childwindow_flag_commandbutton = True
            self.command_buttons.command_refresh.connect(self.command_refresh_event)
            self.command_buttons.command_close.connect(self.command_close_event)
            self.command_buttons.show()
        except Exception as e:
            print(e, 'command_action_edit_event', 'Tools')

    def command_action_delete_event(self):
        if QMessageBox.warning(self, "操作警告", '是否删除这个命令？\n该操作不可恢复！',
                               QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            try:
                # 在按钮配置字典中删除
                del self.dict_to_button_command[self.rightmenu_curr]
                # 在坐标类中删除
                self.button_list_command.remove_button(self.rightmenu_curr)
                # 在按钮绘制字典中删除
                self.command_button[self.rightmenu_curr].deleteLater()
                del self.command_button[self.rightmenu_curr]
                # 保存配置并重新绘制
                self.command_buttons_repaint()
            except Exception as e:
                print(e, 'command_action_delete_event', 'Tools')

    def command_action_crontab_event(self):
        # 定时执行，可设定次数和间隔时间
        pass







    def read_config_component(self, filename):
        with open('config/' + filename, 'r', encoding='utf-8') as f:
            self.dict_to_button_component = json.load(f)
            self.dict_to_button_component['button_add'] = {
                'name': '添加',
                'simple_name': '添加',
                "folder": "",
                "filename": "",
                'introduction': '',
                "command_template": [],
                "command_introduction": [],
                "command_example": [],
                "command_built_in": [],
                "result": [],
            }


    def component_buttons_add_event(self):
        pass


    def component_buttons_clicked_event(self):
        pass