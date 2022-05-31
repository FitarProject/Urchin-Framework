from window.ui.tools_buttons_addtool_dialog import Ui_tools_buttons_addtool_dialog
from window.dialog.tools_tool_add_command_template import Tools_tool_add_command_template_event
from window.dialog.tools_tool_add_command_built_in import Tools_tool_add_command_built_in_event
from window.dialog.tools_tool_add_result import Tools_tool_add_result_event


from PyQt5.Qt import *


class Tools_buttons_addtool_event(QWidget, Ui_tools_buttons_addtool_dialog):
    tool_add = pyqtSignal(dict)
    tool_close = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.childwindow_flag_template = False
        self.childwindow_flag_built_in = False
        self.childwindow_flag_result = False
        self.button_config = {
                'name': "",
                'simple_name': "",
                "folder": "",
                "filename": "",
                'introduction': "",
                "command_template": ["toolname --parameter"],
                "command_introduction": [""],
                "command_example": [""],
                "command_built_in": ["toolname -h"],
                "result": ["cmd output"],
            }
        self.setupUi(self)

    def setupUi(self, tools_buttons_addtool_dialog):
        super().setupUi(tools_buttons_addtool_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            self.set_icon()
            # 填充内容
            self.comboBox_command_template.addItems(self.button_config['command_template'])
            self.lineEdit_command_introduction.setText(self.button_config['command_introduction'][0])
            self.lineEdit_command_example.setText(self.button_config['command_example'][0])
            self.comboBox_command_built_in.addItems(self.button_config['command_built_in'])
            self.comboBox_result.addItems(self.button_config['result'])
            self.plainTextEdit_introduction.setPlainText(self.button_config['introduction'])
            # 占位符
            self.lineEdit_name.setPlaceholderText('请输入工具全称')
            self.lineEdit_simple_name.setPlaceholderText('请输入工具简称')
            self.lineEdit_position.setPlaceholderText('请输入工具位置')
            # self.comboBox_command_template.setPlaceholderText('请输入命令模板内容')
            self.lineEdit_command_introduction.setPlaceholderText('请输入该条命令介绍')
            self.lineEdit_command_example.setPlaceholderText('请输入该条命令示例')
            # self.comboBox_command_built_in.setPlaceholderText('请输入内置命令内容')
            # self.comboBox_result.setPlaceholderText('请输入结果文件位置')
            self.plainTextEdit_introduction.setPlaceholderText('请输入工具介绍')
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'setupUi')
        try:
            # 连接命令选择信号
            self.comboBox_command_template.currentIndexChanged[int].connect(self.change_command_event)
            # 连接下侧按钮的信号与槽
            self.button_yes.clicked.connect(self.button_yes_event)
            self.button_no.clicked.connect(self.button_no_event)
            # 连接右侧按钮的信号与槽
            self.toolButton_rename.clicked.connect(self.toolButton_rename_clear_event)
            self.toolButton_simple_rename.clicked.connect(self.toolButton_simple_rename_clear_event)
            self.toolButton_position.clicked.connect(self.toolButton_position_event)
            self.toolButton_command_template.clicked.connect(self.button_add_command_template_event)
            self.toolButton_command_introduction.clicked.connect(self.toolButton_command_introduction_clear_event)
            self.toolButton_command_example.clicked.connect(self.toolButton_command_example_clear_event)
            self.toolButton_command_built_in.clicked.connect(self.button_add_command_built_in_event)
            self.toolButton_result.clicked.connect(self.button_add_result_event)
            # 连接文本框改变函数
            # self.lineEdit_name.textChanged.connect(self.change_name_text_event)
            # self.lineEdit_simple_name.textChanged.connect(self.change_simple_name_text_event)
            self.lineEdit_position.textChanged.connect(self.change_position_text_event)
            self.comboBox_command_template.editTextChanged.connect(self.change_command_text_event)
            self.lineEdit_command_introduction.textChanged.connect(self.change_command_introduction_text_event)
            self.lineEdit_command_example.textChanged.connect(self.change_command_example_text_event)
            self.comboBox_command_built_in.editTextChanged.connect(self.change_command_built_in_text_event)
            self.comboBox_result.editTextChanged.connect(self.change_result_text_event)
            # self.plainTextEdit_introduction.textChanged.connect(self.change_introduction_text_event)
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', '信号连接')

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            # 发送关闭信号（配置已保存）
            self.tool_close.emit()
            if self.childwindow_flag_template:
                self.tool_add_template.close()
            if self.childwindow_flag_built_in:
                self.tool_add_built_in.close()
            if self.childwindow_flag_result:
                self.tool_add_result.close()
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'closeEvent')

    # 设置图标
    def set_icon(self):
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_select_file = QIcon("resource/image/folder.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        self.toolButton_rename.setIcon(self.icon_clear)
        self.toolButton_simple_rename.setIcon(self.icon_clear)
        self.toolButton_command_template.setIcon(self.icon_add)
        self.toolButton_position.setIcon(self.icon_select_file)
        self.toolButton_command_introduction.setIcon(self.icon_clear)
        self.toolButton_command_example.setIcon(self.icon_clear)
        self.toolButton_command_built_in.setIcon(self.icon_add)
        self.toolButton_result.setIcon(self.icon_add)

    # 检查配置内容
    def check_config(self):
        try:
            if self.button_config['simple_name'] == '':
                self.button_config['simple_name'] = self.button_config['name']
                self.lineEdit_simple_name.setText(self.button_config['name'])
            if self.button_config['result'][0] == '':
                self.button_config['result'][0] = 'cmd output'
                self.comboBox_result.setItemText(0, 'cmd output')
            for i in self.button_config['command_template']:
                if i == '':
                    index = self.button_config['command_template'].index(i)
                    self.comboBox_command_template.removeItem(index)
                    self.button_config['command_template'].pop(index)
                    self.button_config['command_introduction'].pop(index)
                    self.button_config['command_example'].pop(index)
            for i in self.button_config['command_built_in']:
                if i == '':
                    index = self.button_config['command_built_in'].index(i)
                    self.comboBox_command_built_in.removeItem(index)
                    self.button_config['command_built_in'].pop(index)
            for i in self.button_config['result']:
                if i == '':
                    index = self.button_config['result'].index(i)
                    self.comboBox_result.removeItem(index)
                    self.button_config['result'].pop(index)
            if len(self.button_config['name']) == 0:
                QMessageBox.warning(self, "操作提示", '工具名称不可为空！', QMessageBox.Ok)
                return False
            elif len(self.button_config['folder']) == 0 and len(self.button_config['filename']) == 0:
                QMessageBox.warning(self, "操作提示", '工具位置不可为空！', QMessageBox.Ok)
                return False
            elif len(self.button_config['command_template']) == 0:
                QMessageBox.warning(self, "操作提示", '命令模板不可为空！', QMessageBox.Ok)
                return False
            else:
                return True
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'check_config')

    # 自定义槽函数
    def button_yes_event(self):
        try:
            self.button_config['name'] = self.lineEdit_name.text()
            self.button_config['simple_name'] = self.lineEdit_simple_name.text()
            self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
            if self.check_config() == True:
                self.tool_add.emit(self.button_config)
                self.close()
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'button_yes_event')

    def button_no_event(self):
        self.close()

    # 子窗口槽函数
    def get_template(self, flag, new_command_template, new_command_introduction, new_command_example):
        try:
            if flag:
                self.button_config['command_template'].append(new_command_template)
                self.button_config['command_introduction'].append(new_command_introduction)
                self.button_config['command_example'].append(new_command_example)
                self.comboBox_command_template.addItem(new_command_template)
                self.lineEdit_command_introduction.setText(self.button_config['command_introduction'][self.comboBox_command_template.currentIndex()])
                self.lineEdit_command_example.setText(self.button_config['command_example'][self.comboBox_command_template.currentIndex()])
            else:
                self.childwindow_flag_template = False
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'get_template')

    def get_built_in(self, flag, new_command_built_in):
        try:
            if flag:
                self.button_config['command_built_in'].append(new_command_built_in)
                self.comboBox_command_built_in.addItem(new_command_built_in)
            else:
                self.childwindow_flag_built_in = False
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'get_built_in')

    def get_result(self, flag, new_result):
        try:
            if flag:
                self.button_config['result'].append(new_result)
                self.comboBox_result.addItem(new_result)
            else:
                self.childwindow_flag_built_in = False
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'get_result')

    # 命令模板更换所选行
    def change_command_event(self, index):
        try:
            text_introduction = self.button_config['command_introduction'][index]
            text_example = self.button_config['command_example'][index]
            if text_introduction != '':
                self.lineEdit_command_introduction.setText(text_introduction)
            else:
                self.button_config['command_introduction'][index] = 'Tool\'s introduction'
                self.lineEdit_command_introduction.setText('Tool\'s introduction')
            if text_example != '':
                self.lineEdit_command_example.setText(text_example)
            else:
                new_example = self.button_config['command_template'][index]
                self.button_config['command_example'][index] = new_example
                self.lineEdit_command_introduction.setText(new_example)
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_command_event')

    # 工具名称更改文本
    def change_name_text_event(self, new_text):
        self.button_config['name'] = new_text

    # 工具简称更改文本
    def change_simple_name_text_event(self, new_text):
        self.button_config['simple_name'] = new_text

    # 工具位置更改文本
    def change_position_text_event(self, new_text):
        try:
            folder_filename = new_text
            if folder_filename != '':
                file_all = folder_filename.replace('\\\\', '/').split('/')
                file_url = ''
                for i in file_all[:-1]:
                    file_url = file_url + i + '/'
                self.button_config['folder'] = file_url
                self.button_config['filename'] = file_all[-1]
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_position_text_event')

    # 命令模板更改文本
    def change_command_text_event(self, new_text):
        try:
            self.comboBox_command_template.setItemText(self.comboBox_command_template.currentIndex(), new_text)
            self.button_config['command_template'][self.comboBox_command_template.currentIndex()] = new_text
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_command_text_event')

    # 命令介绍更改文本
    def change_command_introduction_text_event(self, new_text):
        try:
            index = self.comboBox_command_template.currentIndex()
            if index >= 0:
                self.button_config['command_introduction'][index] = new_text
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_command_introduction_text_event')

    # 命令示例更改文本
    def change_command_example_text_event(self, new_text):
        try:
            index = self.comboBox_command_template.currentIndex()
            if index >= 0:
                self.button_config['command_example'][index] = new_text
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_command_example_text_event')

    # 固定命令更改文本
    def change_command_built_in_text_event(self, new_text):
        try:
            self.comboBox_command_built_in.setItemText(self.comboBox_command_built_in.currentIndex(), new_text)
            self.button_config['command_built_in'][self.comboBox_command_built_in.currentIndex()] = new_text
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_command_built_in_text_event')

    # 有效结果更改文本
    def change_result_text_event(self, new_text):
        try:
            index = self.comboBox_result.currentIndex()
            self.comboBox_result.setItemText(index, new_text)
            self.button_config['result'][index] = new_text
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_result_text_event')

    # 工具介绍更改文本
    def change_introduction_text_event(self):
        try:
            print(self.plainTextEdit_introduction.toPlainText())
            self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'change_introduction_text_event')

    # 下侧按钮槽函数
    # 添加命令模板
    def button_add_command_template_event(self):
        self.tool_add_template = Tools_tool_add_command_template_event(self.button_config['filename'])
        self.tool_add_template.tool_add_command_template.connect(self.get_template)
        self.childwindow_flag_template = True
        self.tool_add_template.show()

    # 添加固定命令
    def button_add_command_built_in_event(self):
        self.tool_add_built_in = Tools_tool_add_command_built_in_event(self.button_config['filename'])
        self.tool_add_built_in.tool_add_command_built_in.connect(self.get_built_in)
        self.childwindow_flag_built_in = True
        self.tool_add_built_in.show()

    # 添加有效结果
    def button_add_result_event(self):
        self.tool_add_result = Tools_tool_add_result_event()
        self.tool_add_result.tool_add_result.connect(self.get_result)
        self.childwindow_flag_result = True
        self.tool_add_result.show()

    # 右侧按钮槽函数
    # 名称清空
    def toolButton_rename_clear_event(self):
        self.lineEdit_name.clear()

    # 简称清空
    def toolButton_simple_rename_clear_event(self):
        self.lineEdit_simple_name.clear()

    # 位置更改
    def toolButton_position_event(self):
        try:
            select_file, file_type = QFileDialog.getOpenFileName(self, '选择文件', './', 'all(*.*);;exe(*.exe);;py(*.py);;jar(*.jar)')
            if select_file != '':
                self.lineEdit_position.setText(select_file)
                file_all = select_file.replace('\\\\', '/').split('/')
                file_url = ''
                file_name = file_all[-1]
                for i in file_all[:-1]:
                    file_url = file_url + i + '/'
                self.button_config['folder'] = file_url
                self.button_config['filename'] = file_name
        except Exception as e:
            print(e, 'Tools_buttons_addtool_event', 'toolButton_position_event')

    # 命令介绍清空
    def toolButton_command_introduction_clear_event(self):
        self.lineEdit_command_introduction.clear()

    # 命令示例清空
    def toolButton_command_example_clear_event(self):
        self.lineEdit_command_example.clear()
