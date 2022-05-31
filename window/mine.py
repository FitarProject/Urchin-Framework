from PyQt5.Qt import *
import json

from window.paint.button_record import Button_list
from window.ui.mine_window import Ui_mine_window
from window.dialog.mine_func_detatil import Mine_func_detatil_event


class Mine(QWidget, Ui_mine_window):
    signal_add_task = pyqtSignal(dict)
    signal_refresh_combine = pyqtSignal()
    signal_add_collect = pyqtSignal(str)
    signal_del_collect = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.childwindow_flag_func_detatil = False
        # 右键菜单所指按钮
        self.rightmenu_curr = ''

        # self.setupUi(self)

    def setupUi(self, mine_window):
        super().setupUi(mine_window)
        with open('qss/mine_window.qss', 'r', encoding='UTF-8') as f:
            self.widget.setStyleSheet(f.read())
        with open('qss/mine_scrollArea.qss', 'r', encoding='UTF-8') as f:
            my_qss = f.read()
            self.scrollAreaWidgetContents.setStyleSheet(my_qss)
            self.scrollAreaWidgetContents_custom.setStyleSheet(my_qss)
            self.widget_2.setStyleSheet(my_qss)
        self.button_manage.hide()
        self.built_in_button = {}
        self.custom_button = {}
        self.dict_to_button_built_in = {}
        self.dict_to_button_custom = {}
        self.button_list_built_in = Button_list(10, 30, 50, 50, 40, 40, 570, 5800)
        self.button_list_custom = Button_list(10, 30, 50, 50, 40, 40, 570, 5800)
        # 读取所有按钮信息并绘制
        self.read_config_built_in('mine_func_built_in.json')
        self.read_config_custom('mine_func_custom.json')
        self.buttons_paint()

    # 绘制按钮
    def buttons_paint(self):
        # 绘制内置功能按钮
        for button_object_name, button_config in self.dict_to_button_built_in.items():
            try:
                x, y, width, height = self.button_list_built_in.add_button(button_object_name)
                self.built_in_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents)
                self.built_in_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.built_in_button[button_object_name].setObjectName(button_object_name)
                self.built_in_button[button_object_name].setText(button_config['name'])
                self.built_in_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                self.built_in_button[button_object_name].setVisible(True)
                self.built_in_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
                self.built_in_button[button_object_name].clicked.connect(self.built_in_buttons_clicked_event)
                self.built_in_button[button_object_name].customContextMenuRequested.connect(self.built_in_rightmenu_event)
            except Exception as e:
                print(e, 'Mine', 'buttons_paint built_in')
        # 绘制自定义功能按钮
        for button_object_name, button_config in self.dict_to_button_custom.items():
            try:
                x, y, width, height = self.button_list_custom.add_button(button_object_name)
                self.custom_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_custom)
                self.custom_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.custom_button[button_object_name].setObjectName(button_object_name)
                self.custom_button[button_object_name].setText(button_config['name'])
                self.custom_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                self.custom_button[button_object_name].setVisible(True)
                self.custom_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
                self.custom_button[button_object_name].clicked.connect(self.custom_buttons_clicked_event)
                self.custom_button[button_object_name].customContextMenuRequested.connect(self.custom_rightmenu_event)
            except Exception as e:
                print(e, 'Mine', 'buttons_paint custom')

    ################################################################################
    ###############################       built_in       ###########################
    ################################################################################
    # 读取配置文件
    def read_config_built_in(self, filename):
        with open('config/' + filename, 'r', encoding='utf-8') as f:
            self.dict_to_button_built_in = json.load(f)

    # 保存配置文件
    def save_config_built_in(self, filename):
        with open('config/' + filename, 'w', encoding='utf-8') as f:
            json.dump(self.dict_to_button_built_in, f)

    # 右键菜单
    def built_in_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()
            self.built_in_rightmenu = QMenu(self)
            # self.built_in_action_edit = QAction(QIcon('resource/image/edit.png'), u'炼金重塑', self)
            # self.built_in_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.built_in_action_task = QAction(QIcon('resource/image/task.png'), u'添加至任务', self)
            self.built_in_action_selected = QAction(QIcon('resource/image/combine.png'), u'添加至炼金', self)
            # self.built_in_rightmenu.addAction(self.built_in_action_edit)
            # self.built_in_rightmenu.addAction(self.built_in_action_delete)
            self.built_in_rightmenu.addAction(self.built_in_action_task)
            # self.built_in_rightmenu.addAction(self.built_in_action_selected)
            # self.built_in_action_edit.triggered.connect(self.built_in_action_edit_event)
            # self.built_in_action_delete.triggered.connect(self.built_in_action_delete_event)
            self.built_in_action_task.triggered.connect(self.built_in_action_task_event)
            self.built_in_action_selected.triggered.connect(self.built_in_action_selected_event)

            self.built_in_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'Mine', 'built_in_rightmenu_event')

    # 工具按钮重绘制
    def built_in_buttons_repaint(self):
        try:
            # 保存配置
            self.save_config_built_in('mine_func_built_in.json')
            # 工具按钮位置重置
            for button_object_name in self.dict_to_button_built_in.keys():
                x, y = self.button_list_built_in.get_button_position(button_object_name)
                width, height = self.button_list_built_in.width, self.button_list_built_in.height
                self.built_in_button[button_object_name].setText(self.dict_to_button_built_in[button_object_name]['name'])
                self.built_in_button[button_object_name].setToolTip('<html><head/><body><p>' + self.dict_to_button_built_in[button_object_name]['name'] + '</p></body></html>')
                self.built_in_button[button_object_name].setGeometry(QRect(x, y, width, height))
            # 刷新界面
            self.scrollAreaWidgetContents.update()
        except Exception as e:
            print(e, 'Mine', 'built_in_buttons_repaint')

    # 自定义槽函数
    # 按钮配置覆盖
    def built_in_refresh_event(self, object_name, object_dict):
        try:
            self.dict_to_button_built_in[object_name] = object_dict
            self.save_config_built_in('mine_func_built_in.json')
            self.built_in_buttons_repaint()
        except Exception as e:
            print(e, 'Mine', 'built_in_refresh_event')

    # 点击内置功能栏的按钮
    def built_in_buttons_clicked_event(self):
        try:
            self.func_detatil = Mine_func_detatil_event(self.sender().objectName(), self.dict_to_button_built_in[self.sender().objectName()], 'built_in')
            self.childwindow_flag_func_detatil = True
            self.func_detatil.dialog_close.connect(self.func_detatil_close_event)
            self.func_detatil.signal_add_task.connect(self.func_detatil_add_task_event)
            self.func_detatil.signal_edit_func.connect(self.func_detatil_edit_func_event)
            self.func_detatil.show()
        except Exception as e:
            print(e, 'Mine', 'built_in_buttons_clicked_event')

    def built_in_action_task_event(self):
        # print(self.dict_to_button_built_in[self.rightmenu_curr])
        self.signal_add_task.emit(self.dict_to_button_built_in[self.rightmenu_curr])

    def built_in_action_selected_event(self):
        print(self.rightmenu_curr)
        pass

    ################################################################################
    ###############################      custom      ###############################
    ################################################################################
    # 读取配置文件
    def read_config_custom(self, filename):
        try:
            with open('config/' + filename, 'r', encoding='utf-8') as f:
                self.dict_to_button_custom = json.load(f)
        except Exception as e:
            print(e, 'Mine', 'read_config_custom')

    def save_config_custom(self, filename):
        try:
            with open('config/' + filename, 'w', encoding='utf-8') as f:
                json.dump(self.dict_to_button_custom, f)
        except Exception as e:
            print(e, 'Mine', 'save_config_custom')

    # 右键菜单
    def custom_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()

            self.custom_rightmenu = QMenu(self)
            self.custom_action_edit = QAction(QIcon('resource/image/edit.png'), u'炼金重塑', self)
            self.custom_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.custom_action_task = QAction(QIcon('resource/image/task.png'), u'添加至任务', self)
            self.custom_action_selected = QAction(QIcon('resource/image/combine.png'), u'添加至炼金', self)
            self.custom_action_collect = QAction(QIcon('resource/image/collect.png'), u'添加至常用', self)
            self.custom_rightmenu.addAction(self.custom_action_edit)
            self.custom_rightmenu.addAction(self.custom_action_delete)
            self.custom_rightmenu.addAction(self.custom_action_task)
            self.custom_rightmenu.addAction(self.custom_action_selected)
            self.custom_rightmenu.addAction(self.custom_action_collect)
            self.custom_action_edit.triggered.connect(self.custom_action_edit_event)
            self.custom_action_delete.triggered.connect(self.custom_action_delete_event)
            self.custom_action_task.triggered.connect(self.custom_action_task_event)
            self.custom_action_selected.triggered.connect(self.custom_action_selected_event)
            self.custom_action_collect.triggered.connect(self.custom_action_collect_event)

            self.custom_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'Mine', 'custom_rightmenu_event')

    # 自定义功能按钮重绘制
    def custom_buttons_repaint(self):
        try:
            # 保存配置
            self.save_config_custom('mine_func_custom.json')
            # 工具按钮位置重置
            for button_object_name in self.dict_to_button_custom.keys():
                x, y = self.button_list_custom.get_button_position(button_object_name)
                width, height = self.button_list_custom.width, self.button_list_custom.height
                self.custom_button[button_object_name].setText(self.dict_to_button_custom[button_object_name]['name'])
                self.custom_button[button_object_name].setToolTip('<html><head/><body><p>' + self.dict_to_button_custom[button_object_name]['name'] + '</p></body></html>')
                self.custom_button[button_object_name].setGeometry(QRect(x, y, width, height))
            # 刷新界面
            self.scrollAreaWidgetContents_custom.update()
        except Exception as e:
            print(e, 'Mine', 'custom_buttons_repaint')

    # 自定义槽函数
    # 自定义按钮覆盖事件
    def custom_refresh_event(self, object_name, object_dict):
        try:
            self.dict_to_button_custom[object_name] = object_dict
            self.save_config_custom('mine_func_custom.json')
            self.custom_buttons_repaint()
        except Exception as e:
            print(e, 'Mine', 'custom_refresh_event')

    # 添加自定义功能事件
    def addcustom_add_event(self, button_config):
        try:
            # 获取新按钮编号
            num = int(self.button_list_custom.get_button_list()[-1].split('_')[-1]) + 1
            button_object_name = 'button_' + str(num)
            # 添加进按钮字典并保存配置
            self.dict_to_button_custom[button_object_name] = button_config
            # 获取按钮坐标并绘制
            x, y, width, height = self.button_list_custom.add_button(button_object_name)
            self.custom_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_custom)
            self.custom_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.custom_button[button_object_name].setObjectName(button_object_name)
            self.custom_button[button_object_name].setText(button_config['name'])
            self.custom_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
            self.custom_button[button_object_name].setVisible(True)
            self.custom_button[button_object_name].setContextMenuPolicy(Qt.CustomContextMenu)
            self.custom_button[button_object_name].clicked.connect(self.custom_buttons_clicked_event)
            self.custom_button[button_object_name].customContextMenuRequested.connect(self.custom_rightmenu_event)
            # 重新绘制所有按钮
            self.custom_buttons_repaint()
        except Exception as e:
            print(e, 'Mine', 'addcustom_add_event')

    # 子窗口关闭
    def func_detatil_close_event(self):
        self.childwindow_flag_func_detatil = False

    def func_detatil_add_task_event(self, object_name, func_type):
        if func_type == 'built_in':
            self.signal_add_task.emit(self.dict_to_button_built_in[object_name])
        elif func_type == 'custom':
            self.signal_add_task.emit(self.dict_to_button_custom[object_name])
        else:
            print('type error!')

    def func_detatil_edit_func_event(self, object_name, config, func_type):
        if func_type == 'built_in':
            self.dict_to_button_built_in[object_name] = config
            self.built_in_refresh_event(object_name, config)
        elif func_type == 'custom':
            self.dict_to_button_custom[object_name] = config
            self.custom_refresh_event(object_name, config)
        else:
            print('type error!')

    # 点击自定义功能栏的按钮
    def custom_buttons_clicked_event(self):
        try:
            self.func_detatil = Mine_func_detatil_event(self.sender().objectName(), self.dict_to_button_custom[self.sender().objectName()], 'custom')
            self.childwindow_flag_func_detatil = True
            self.func_detatil.dialog_close.connect(self.func_detatil_close_event)
            self.func_detatil.signal_add_task.connect(self.func_detatil_add_task_event)
            self.func_detatil.signal_edit_func.connect(self.func_detatil_edit_func_event)
            self.func_detatil.show()
        except Exception as e:
            print(e, 'Mine', 'custom_buttons_clicked_event')

    # 炼金重塑
    def custom_action_edit_event(self):
        try:
            if QMessageBox.warning(self, "操作警告", '该操作将会清空炼金工坊合成部件？\n是否继续？', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                with open('config/combine.txt', 'w', encoding='utf-8') as f:
                    for data in self.dict_to_button_custom[self.rightmenu_curr]['config']:
                        f.write(str(data) + '\n')
                with open('config/combine_variable.json', 'w', encoding='utf-8') as f:
                    json.dump(self.dict_to_button_custom[self.rightmenu_curr], f)
                self.signal_refresh_combine.emit()
        except Exception as e:
            print(e, 'Mine', 'custom_action_edit_event')

    def custom_action_delete_event(self):
        if QMessageBox.warning(self, "操作警告", '是否删除这个自定义功能？\n该操作不可恢复！', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            try:
                # 在按钮配置字典中删除
                del self.dict_to_button_custom[self.rightmenu_curr]
                # 在坐标类中删除
                self.button_list_custom.remove_button(self.rightmenu_curr)
                # 在按钮绘制字典中删除
                self.custom_button[self.rightmenu_curr].deleteLater()
                del self.custom_button[self.rightmenu_curr]
                # 在常用功能中删除
                self.signal_del_collect.emit(self.rightmenu_curr)
                # 保存配置并重新绘制
                self.custom_buttons_repaint()
            except Exception as e:
                print(e, 'Mine', 'custom_action_delete_event')

    def custom_action_task_event(self):
        try:
            # print(self.dict_to_button_custom[self.rightmenu_curr])
            self.signal_add_task.emit(self.dict_to_button_custom[self.rightmenu_curr])
        except Exception as e:
            print(e, 'Mine', 'custom_action_task_event')

    def custom_action_selected_event(self):
        pass

    # 发送至常用功能
    def custom_action_collect_event(self):
        self.signal_add_collect.emit(self.rightmenu_curr)
