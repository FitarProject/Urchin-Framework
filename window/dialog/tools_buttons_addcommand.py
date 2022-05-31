from window.ui.tools_buttons_addcommand_dialog import Ui_tools_buttons_addcommand_dialog
import re

from PyQt5.Qt import *


class Tools_buttons_addcommand_event(QWidget, Ui_tools_buttons_addcommand_dialog):
    command_add = pyqtSignal(dict)
    command_close = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.button_config = {
            "name": "添加",
            "introduction": "",
            "command": "",
            "variable": ["variable_1"]
        }
        self.variable_num = 1
        self.setupUi(self)

    def setupUi(self, tools_buttons_addcommand_dialog):
        super().setupUi(tools_buttons_addcommand_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            self.set_icon()
            # 填充内容
            self.lineEdit_name.setPlaceholderText('请输入命令名称')
            self.lineEdit_command.setPlaceholderText('请输入命令详情')
            # 添加根节点
            root = QTreeWidgetItem(self.list_variable)
            new_variable = 'variable_1'
            root.setText(0, new_variable)
            root.setText(1, new_variable)
            root.setFlags(root.flags() | Qt.ItemIsEditable)
            self.list_variable.addTopLevelItem(root)
            self.list_variable.openPersistentEditor(root, 1)
            self.plainTextEdit_introduction.setPlaceholderText('请输入命令介绍')
            # 连接下侧按钮的信号与槽
            self.button_yes.clicked.connect(self.button_yes_event)
            self.button_no.clicked.connect(self.button_no_event)
            # 连接右侧按钮的信号与槽
            self.button_name.clicked.connect(self.button_name_clear_event)
            self.button_command.clicked.connect(self.button_command_clear_event)
            self.button_addvariable.clicked.connect(self.button_addvariable_event)
            self.button_delvariable.clicked.connect(self.button_delvariable_event)
            # 列表信息改变
            self.list_variable.itemChanged.connect(self.list_change_event)
        except Exception as e:
            print(e, 'Tools_buttons_addcommand_event setupUi', 'Tools_buttons_addcommand_event')

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            self.command_close.emit()
        except Exception as e:
            print(e, 'closeEvent', 'Tools_buttons_addcommand_event')

    # 设置图标
    def set_icon(self):
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_del = QIcon("resource/image/del.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        self.button_name.setIcon(self.icon_clear)
        self.button_command.setIcon(self.icon_clear)
        self.button_addvariable.setIcon(self.icon_add)
        self.button_delvariable.setIcon(self.icon_del)

    # 检查配置内容
    def check_config(self):
        try:
            if len(self.lineEdit_name.text()) == 0:
                QMessageBox.warning(self, "操作提示", '命令名称不可为空！', QMessageBox.Ok)
                return False
            elif len(self.lineEdit_command.text()) == 0:
                QMessageBox.warning(self, "操作提示", '命令详情不可为空！', QMessageBox.Ok)
                return False
            else:
                return True
        except Exception as e:
            print(e, 'check_config', 'Tools_buttons_addcommand_event')

    # 自定义槽函数
    # 下侧按钮槽函数
    # 编辑通道脚本
    def button_yes_event(self):
        try:
            if self.check_config() == True:
                self.button_config['name'] = self.lineEdit_name.text()
                self.button_config['command'] = self.lineEdit_command.text()
                self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                # 发射添加信号
                self.command_add.emit(self.button_config)
                self.close()
        except Exception as e:
            print(e, 'button_yes_event', 'Tools_buttons_addcommand_event')

    # 快速编辑
    def button_no_event(self):
        self.close()

    # 右侧按钮槽函数
    # 名称清空
    def button_name_clear_event(self):
        self.lineEdit_name.clear()

    # 命令详情清空
    def button_command_clear_event(self):
        self.lineEdit_command.clear()

    # 添加变量
    def button_addvariable_event(self):
        try:
            self.variable_num += 1
            root = QTreeWidgetItem(self.list_variable)
            new_variable = 'variable_' + str(self.variable_num)
            root.setText(0, new_variable)
            root.setText(1, new_variable)
            root.setFlags(root.flags() | Qt.ItemIsEditable)
            self.list_variable.addTopLevelItem(root)
            self.list_variable.openPersistentEditor(root, 1)
            self.button_config['variable'].append(new_variable)
            self.lineEdit_command.setText(self.lineEdit_command.text() + ' $variable_' + str(self.variable_num))
            self.button_config['command'] = self.lineEdit_command.text()
        except Exception as e:
            print(e, 'button_addvariable_event', 'Tools_buttons_addcommand_event')

    # 去除变量
    def button_delvariable_event(self):
        try:
            if self.variable_num > 0:
                if self.lineEdit_command.text().endswith(' $variable_' + str(self.variable_num)):
                    self.lineEdit_command.setText(self.lineEdit_command.text().rstrip(' $variable_' + str(self.variable_num)))
                self.variable_num -= 1
                self.list_variable.takeTopLevelItem(self.variable_num)
                self.button_config['variable'].pop(-1)
        except Exception as e:
            print(e, 'button_delvariable_event', 'Tools_buttons_addcommand_event')

    def list_change_event(self, item, col):
        try:
            if item == self.list_variable.currentItem():
                num = re.findall(r'[0-9]+', item.text(0))
                index = int(num[0])
                self.button_config['variable'][index-1] = item.text(col)
        except Exception as e:
            print(e, 'list_change_event', 'Tools_buttons_addcommand_event')