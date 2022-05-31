from window.ui.combine_buttons_tool_dialog import Ui_combine_buttons_tool_dialog

from PyQt5.Qt import *
from window.func.mylist_item import Mylist_item


class Combine_buttons_tool_event(QWidget, Ui_combine_buttons_tool_dialog):
    config_change = pyqtSignal(dict)
    dialog_close = pyqtSignal()

    def __init__(self, mydata, tool_config, component_config, selectable_result):
        super().__init__()
        # self.childwindow_flag_result = False
        self.mydata = mydata
        self.tool_config = tool_config
        self.component_config = component_config
        self.selectable_result = selectable_result

        self.setupUi(self)

    def setupUi(self, combine_buttons_tool_dialog):
        try:
            super().setupUi(combine_buttons_tool_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.set_icon()
            command = self.tool_config['command_template'][self.mydata['command_num']]
            # 绘制配件详情栏
            layout = QGridLayout()
            self.components = Mylist_item(self.widget_component, self.mydata, self.component_config, 'component')
            layout.addWidget(self.components)
            self.widget_component.setLayout(layout)
            # 填充内容
            self.lineEdit_name.setText(self.tool_config['name'])
            self.lineEdit_command.setText(command)
            self.comboBox_variable.addItems(self.mydata['variable'])
            if len(self.mydata['variable_value']) != 0:
                self.lineEdit_variable_value.setText(self.mydata['variable_value'][0])
            self.comboBox_result.addItems(self.tool_config['result'])
            self.lineEdit_result_name.setText(self.mydata['result_name'][0])
            # 设置按钮菜单
            menus = QMenu(self.toolButton_variable_value)
            action_list = {}
            for i in self.selectable_result:
                action_list[i] = QAction(self.icon_select_text, i, self)
                action_list[i].setData(i)
                menus.addAction(action_list[i])
                action_list[i].triggered.connect(lambda: self.lineEdit_variable_value.setText(self.sender().data()))
            self.toolButton_variable_value.setMenu(menus)
            self.toolButton_variable_value.setPopupMode(QToolButton.InstantPopup)
            # 去角标
            self.setStyleSheet('QToolButton::menu-indicator{image: none;}')
            # 连接命令选择信号
            self.comboBox_variable.currentIndexChanged[int].connect(self.change_variable_event)
            self.comboBox_result.currentIndexChanged[int].connect(self.change_result_event)
            # 连接信号
            self.toolButton_variable.clicked.connect(self.toolButton_variable_event)
            # self.toolButton_variable_value.clicked.connect(self.toolButton_variable_value_event)
            # self.toolButton_result.clicked.connect(self.toolButton_result_event)
            self.toolButton_result_name.clicked.connect(self.toolButton_result_name_event)
            self.lineEdit_variable_value.textChanged.connect(self.change_variable_value_event)
            self.lineEdit_result_name.textChanged.connect(self.change_result_name_event)
            self.components.config_change.connect(self.refresh_component)
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'setupUi')

    def set_icon(self):
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_select_line = QIcon("resource/image/select_line.png")
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_select_text = QIcon("resource/image/select_text.png")
        self.toolButton_variable.setIcon(self.icon_edit)
        self.toolButton_variable_value.setIcon(self.icon_select_line)
        # self.toolButton_result.setIcon(self.icon_add)
        self.toolButton_result_name.setIcon(self.icon_edit)

    # def closeEvent(self, QCloseEvent):
    #     super().closeEvent(QCloseEvent)
    #     if self.childwindow_flag_result:
    #         self.tool_add_result.close()

    def refresh_component(self, new_mydata):
        self.mydata = new_mydata
        self.refresh()

    def refresh(self):
        self.config_change.emit(self.mydata)
        # print(self.mydata)

    # 命令变量更换所选行
    def change_variable_event(self, index):
        try:
            self.lineEdit_variable_value.setText(self.mydata['variable_value'][index])
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'change_variable_event')

    # 输出变量更换所选行
    def change_result_event(self, index):
        try:
            print(self.mydata['result_name'], index)
            self.lineEdit_result_name.setText(self.mydata['result_name'][index])
            self.lineEdit_result_name.setReadOnly(True)
            self.toolButton_result_name.setIcon(self.icon_edit)
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'change_result_event')

    # 命令变量更改文本
    def change_variable_text_event(self, new_text):
        try:
            if len(new_text) > 1:
                if new_text[0] == '$' and new_text[1] != '$':
                    self.comboBox_variable.setItemText(self.comboBox_variable.currentIndex(), new_text)
                    self.mydata['variable'][self.comboBox_variable.currentIndex()] = new_text
                # else:
                #     QMessageBox.warning(self, "操作提示", '请注意变量格式！请以\'$\'开头。', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'change_variable_text_event')

    # 变量值更改文本
    def change_variable_value_event(self, new_text):
        try:
            self.mydata['variable_value'][self.comboBox_variable.currentIndex()] = new_text
            self.refresh()
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'change_variable_value_event')

    # 结果变量更改文本
    def change_result_name_event(self, new_text):
        try:
            if len(new_text) == 0:
                self.mydata['result_name'][self.comboBox_result.currentIndex()] = ''
                self.refresh()
            elif len(new_text) > 1 and new_text[0] == '$' and new_text[1] != '$':
                if new_text not in self.selectable_result:
                    self.mydata['result_name'][self.comboBox_result.currentIndex()] = new_text
                    self.refresh()
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'change_result_name_event')

    #  右侧按钮槽函数
    def toolButton_variable_event(self):
        try:
            if self.comboBox_variable.isEditable():
                self.comboBox_variable.setEditable(False)
                self.toolButton_variable.setIcon(self.icon_edit)
                self.comboBox_variable.editTextChanged.disconnect(self.change_variable_text_event)
                self.refresh()
            else:
                if len(self.mydata['variable']) > 0:
                    self.comboBox_variable.setEditable(True)
                    self.toolButton_variable.setIcon(self.icon_save)
                    self.comboBox_variable.editTextChanged.connect(self.change_variable_text_event)
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'toolButton_variable_event')

    # def toolButton_variable_value_event(self):
    #     menus = QMenu(self.toolButton_variable_value)
    #     action_list = {}
    #     for i in self.selectable_result:
    #         action_list[i] = QAction(i, self)
    #         action_list[i].setData(i)
    #         menus.addAction(action_list[i])
    #         action_list[i].triggered.connect(lambda: self.lineEdit_variable_value.setText(self.sender().data()))
    #     self.toolButton_variable_value.setMenu(menus)
    #     self.toolButton_variable_value.setPopupMode(QToolButton.InstantPopup)
    #     self.toolButton_variable_value.setArrowType(Qt.DownArrow)

    def toolButton_result_name_event(self):
        try:
            if self.lineEdit_result_name.isReadOnly():
                self.lineEdit_result_name.setReadOnly(False)
                self.toolButton_result_name.setIcon(self.icon_save)
            else:
                self.lineEdit_result_name.setReadOnly(True)
                self.toolButton_result_name.setIcon(self.icon_edit)
                new_text = self.lineEdit_result_name.text()
                if len(new_text) == 1:
                    QMessageBox.warning(self, "操作提示", '请注意变量格式！变量以\'$\'开头。', QMessageBox.Ok)
                    self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_result.currentIndex()])
                elif len(new_text) > 1:
                    if new_text[0] != '$' or new_text[1] == '$':
                        QMessageBox.warning(self, "操作提示", '请注意变量格式！变量以\'$\'开头。', QMessageBox.Ok)
                        self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_result.currentIndex()])
                if new_text in self.selectable_result:
                    QMessageBox.warning(self, "操作提示", '请勿使用重复变量名称！', QMessageBox.Ok)
                self.refresh()
        except Exception as e:
            print(e, 'Combine_buttons_tool_event', 'toolButton_result_name_event')
    # def get_result(self, flag, new_result):
    #     try:
    #         if flag:
    #             self.button_config['result'].append(new_result)
    #             self.comboBox_result.addItem(new_result)
    #             self.refresh()
    #         else:
    #             self.childwindow_flag_result = False
    #     except Exception as e:
    #         print(e, 'Combine_buttons_tool_event', 'get_result')

