from window.ui.tools_buttons_tool_dialog import Ui_tools_buttons_tool_dialog
from window.dialog.tools_tool_add_command_template import Tools_tool_add_command_template_event
from window.dialog.tools_tool_add_command_built_in import Tools_tool_add_command_built_in_event
from window.dialog.tools_tool_add_result import Tools_tool_add_result_event

import json
from PyQt5.Qt import *


class Tools_buttons_tool_event(QWidget, Ui_tools_buttons_tool_dialog):
    tool_refresh = pyqtSignal(str, dict, str)
    tool_close = pyqtSignal(bool)
    refresh_selected_tool = pyqtSignal()

    def __init__(self, button_object, button_config):
        super().__init__()
        self.button_object = button_object
        self.button_config = button_config
        self.save_flag = True
        self.childwindow_flag_template = False
        self.childwindow_flag_built_in = False
        self.childwindow_flag_result = False
        self.setupUi(self)

    def setupUi(self, tools_buttons_tool_dialog):
        super().setupUi(tools_buttons_tool_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        if self.button_config['name'] == '':
            self.button_config['name'] = '默认工具全称'
            self.save_config_event('name')
        if self.button_config['simple_name'] == '':
            self.button_config['simple_name'] = '默认工具简称'
            self.save_config_event('simple_name')
        try:
            self.set_icon()
            # 填充内容
            self.lineEdit_name.setText(self.button_config['name'])
            self.lineEdit_simple_name.setText(self.button_config['simple_name'])
            self.lineEdit_position.setText(self.button_config['folder'] + self.button_config['filename'])
            if len(self.button_config['command_template']) != 0:
                self.comboBox_command_template.addItems(self.button_config['command_template'])
                if self.button_config['command_introduction'][0] == '':
                    self.button_config['command_introduction'][0] = 'Tool\'s introduction'
                self.lineEdit_command_introduction.setText(self.button_config['command_introduction'][0])
                if self.button_config['command_example'][0] == '':
                    self.button_config['command_example'][0] = self.button_config['command_template'][0]
                self.lineEdit_command_example.setText(self.button_config['command_example'][0])
            if len(self.button_config['command_built_in']) != 0:
                self.comboBox_command_built_in.addItems(self.button_config['command_built_in'])
            if len(self.button_config['result']) != 0:
                self.comboBox_result.addItems(self.button_config['result'])
            self.plainTextEdit_introduction.setPlainText(self.button_config['introduction'])
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'setupUI')
        # 连接命令选择信号
        self.comboBox_command_template.currentIndexChanged[int].connect(self.change_command_event)
        # 连接下侧按钮的信号与槽
        self.button_add_command_template.clicked.connect(self.button_add_command_template_event)
        self.button_add_command_built_in.clicked.connect(self.button_add_command_built_in_event)
        self.button_add_result.clicked.connect(self.button_add_result_event)
        self.button_add_selected.clicked.connect(self.button_addto_selected_event)
        self.button_addto_task.clicked.connect(self.button_addto_task_event)
        self.button_addto_func.clicked.connect(self.button_addto_func_event)
        self.button_edit_all.clicked.connect(self.button_edit_all_event)
        # 连接右侧按钮的信号与槽
        self.toolButton_rename.clicked.connect(self.toolButton_rename_event)
        self.toolButton_simple_rename.clicked.connect(self.toolButton_simple_rename_event)
        self.toolButton_position.clicked.connect(self.toolButton_position_event)
        self.toolButton_command_template.clicked.connect(self.toolButton_command_template_event)
        self.toolButton_command_introduction.clicked.connect(self.toolButton_command_introduction_event)
        self.toolButton_command_example.clicked.connect(self.toolButton_command_example_event)
        self.toolButton_command_built_in.clicked.connect(self.toolButton_command_built_in_event)
        self.toolButton_result.clicked.connect(self.toolButton_result_event)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        # 发送关闭信号（配置已保存）
        self.tool_close.emit(True)
        if not self.save_flag:
            self.tool_close.emit(False)
        if self.childwindow_flag_template:
            self.tool_add_template.close()
        if self.childwindow_flag_built_in:
            self.tool_add_built_in.close()
        if self.childwindow_flag_result:
            self.tool_add_result.close()

    # 设置图标
    def set_icon(self):
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_select_file = QIcon("resource/image/folder.png")
        self.icon_replace = QIcon("resource/image/replace.png")
        self.icon_delete = QIcon("resource/image/delete.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        # self.icon_edit.addPixmap(QPixmap("edit.svg"), QIcon.Normal, QIcon.Off)
        self.toolButton_rename.setIcon(self.icon_edit)
        self.toolButton_simple_rename.setIcon(self.icon_edit)
        self.toolButton_command_template.setIcon(self.icon_edit)
        self.toolButton_position.setIcon(self.icon_select_file)
        self.toolButton_command_introduction.setIcon(self.icon_edit)
        self.toolButton_command_built_in.setIcon(self.icon_edit)
        self.toolButton_command_example.setIcon(self.icon_edit)
        self.toolButton_result.setIcon(self.icon_edit)

    # 返回配置给主界面
    def save_config_event(self, subitem_name='all'):
        self.tool_refresh.emit(self.button_object, self.button_config, subitem_name)

    # 自定义槽函数
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
                self.save_config_event()
            else:
                self.childwindow_flag_template = False
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'get_template')

    def get_built_in(self, flag, new_command_built_in):
        try:
            if flag:
                self.button_config['command_built_in'].append(new_command_built_in)
                self.comboBox_command_built_in.addItem(new_command_built_in)
                self.save_config_event('command_built_in')
            else:
                self.childwindow_flag_built_in = False
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'get_built_in')

    def get_result(self, flag, new_result):
        try:
            if flag:
                self.button_config['result'].append(new_result)
                self.comboBox_result.addItem(new_result)
                self.save_config_event('result')
            else:
                self.childwindow_flag_result = False
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'get_result')

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
            print(e, 'Tools_buttons_tool_event', 'change_command_event')

    # 命令模板更改文本
    def change_command_text_event(self, new_text):
        self.comboBox_command_template.setItemText(self.comboBox_command_template.currentIndex(), new_text)
        self.button_config['command_template'][self.comboBox_command_template.currentIndex()] = new_text

    # 命令介绍更改文本
    def change_command_introduction_text_event(self, new_text):
        index = self.comboBox_command_template.currentIndex()
        if index >= 0:
            self.button_config['command_introduction'][index] = new_text

    # 命令示例更改文本
    def change_command_example_text_event(self, new_text):
            index = self.comboBox_command_template.currentIndex()
            if index >= 0:
                self.button_config['command_example'][index] = new_text

    # 固定命令更改文本
    def change_command_built_in_text_event(self, new_text):
        self.comboBox_command_built_in.setItemText(self.comboBox_command_built_in.currentIndex(), new_text)
        self.button_config['command_built_in'][self.comboBox_command_built_in.currentIndex()] = new_text

    # 有效结果更改文本
    def change_result_text_event(self, new_text):
        index = self.comboBox_result.currentIndex()
        self.comboBox_result.setItemText(index, new_text)
        self.button_config['result'][index] = new_text

    # 下侧按钮槽函数
    # 添加命令模板
    def button_add_command_template_event(self):
        if self.save_flag:
            self.tool_add_template = Tools_tool_add_command_template_event(self.button_config['filename'])
            self.tool_add_template.tool_add_command_template.connect(self.get_template)
            self.childwindow_flag_template = True
            self.tool_add_template.show()
        else:
            QMessageBox.warning(self, "操作提示", '请先保存修改！', QMessageBox.Ok)

    # 添加固定命令
    def button_add_command_built_in_event(self):
        try:
            if self.save_flag:
                self.tool_add_built_in = Tools_tool_add_command_built_in_event(self.button_config['filename'])
                self.tool_add_built_in.tool_add_command_built_in.connect(self.get_built_in)
                self.childwindow_flag_built_in = True
                self.tool_add_built_in.show()
            else:
                QMessageBox.warning(self, "操作提示", '请先保存修改！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'button_add_command_built_in_event')

    # 添加有效结果
    def button_add_result_event(self):
        try:
            if self.save_flag:
                self.tool_add_result = Tools_tool_add_result_event()
                self.tool_add_result.tool_add_result.connect(self.get_result)
                self.childwindow_flag_result = True
                self.tool_add_result.show()
            else:
                QMessageBox.warning(self, "操作提示", '请先保存修改！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'button_add_result_event')

    # 添加为任务
    def button_addto_task_event(self):
        QMessageBox.warning(self, "操作提示", '暂不支持工具执行', QMessageBox.Ok)
        pass

    # 添加为炼金
    def button_addto_selected_event(self):
        try:
            index = self.comboBox_command_template.currentIndex()
            if QMessageBox.warning(self, "操作确认", '是否添加工具命令\n"' + self.button_config['command_template'][index] + '"\n至炼金工坊预选区域？', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                config = {"name": self.button_config['name'], "button_num": self.button_object, "command_num": index}
                with open('config/selected_tool.json', 'r', encoding='utf-8') as f:
                    selected_tool = json.load(f)
                selected_tool['selected_tool'].append(config)
                with open('config/selected_tool.json', 'w', encoding='utf-8') as f:
                    json.dump(selected_tool, f)
                self.refresh_selected_tool.emit()
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'button_addto_selected_event')

    # 添加为功能
    def button_addto_func_event(self):
        pass

    # 快速编辑
    def button_edit_all_event(self):
        try:
            if self.button_edit_all.text() == '快速编辑':
                self.save_flag = False
                self.button_edit_all.setText('保存')
                # 名称
                self.lineEdit_name.setReadOnly(False)
                self.toolButton_rename.clicked.disconnect(self.toolButton_rename_event)
                self.toolButton_rename.clicked.connect(self.toolButton_rename_clear_event)
                self.toolButton_rename.setIcon(self.icon_clear)
                # 简称
                self.lineEdit_simple_name.setReadOnly(False)
                self.toolButton_simple_rename.clicked.disconnect(self.toolButton_simple_rename_event)
                self.toolButton_simple_rename.clicked.connect(self.toolButton_simple_rename_clear_event)
                self.toolButton_simple_rename.setIcon(self.icon_clear)
                # 工具位置
                self.lineEdit_position.setReadOnly(False)
                # 命令模板
                if len(self.button_config['command_template']) != 0:
                    self.comboBox_command_template.setEditable(True)
                    self.comboBox_command_template.editTextChanged.connect(self.change_command_text_event)
                self.toolButton_command_template.clicked.disconnect(self.toolButton_command_template_event)
                self.toolButton_command_template.clicked.connect(self.toolButton_command_template_delete_event)
                self.toolButton_command_template.setIcon(self.icon_delete)
                # 命令介绍
                if len(self.button_config['command_template']) != 0:
                    self.lineEdit_command_introduction.setReadOnly(False)
                    self.lineEdit_command_introduction.textChanged.connect(self.change_command_introduction_text_event)
                self.toolButton_command_introduction.clicked.disconnect(self.toolButton_command_introduction_event)
                self.toolButton_command_introduction.clicked.connect(self.toolButton_command_introduction_clear_event)
                self.toolButton_command_introduction.setIcon(self.icon_clear)
                # self.button_config['command_introduction'][self.comboBox_command_template.currentIndex()] = self.lineEdit_command_introduction.text()
                # 命令示例
                if len(self.button_config['command_template']) != 0:
                    self.lineEdit_command_example.setReadOnly(False)
                    self.lineEdit_command_example.textChanged.connect(self.change_command_example_text_event)
                self.toolButton_command_example.clicked.disconnect(self.toolButton_command_example_event)
                self.toolButton_command_example.clicked.connect(self.toolButton_command_example_clear_event)
                self.toolButton_command_example.setIcon(self.icon_clear)
                # 固定命令
                if len(self.button_config['command_built_in']) != 0:
                    self.comboBox_command_built_in.setEditable(True)
                    self.comboBox_command_built_in.editTextChanged.connect(self.change_command_built_in_text_event)
                self.toolButton_command_built_in.clicked.disconnect(self.toolButton_command_built_in_event)
                self.toolButton_command_built_in.clicked.connect(self.toolButton_command_built_in_delete_event)
                self.toolButton_command_built_in.setIcon(self.icon_delete)
                # 有效结果
                if len(self.button_config['result']) != 0:
                    self.comboBox_result.setEditable(True)
                    self.comboBox_result.editTextChanged.connect(self.change_result_text_event)
                self.toolButton_result.clicked.disconnect(self.toolButton_result_event)
                self.toolButton_result.clicked.connect(self.toolButton_result_delete_event)
                self.toolButton_result.setIcon(self.icon_delete)
                # 工具说明
                self.plainTextEdit_introduction.setReadOnly(False)
            else:
                self.save_flag = True
                self.button_edit_all.setText('快速编辑')
                # 名称
                self.lineEdit_name.setReadOnly(True)
                self.toolButton_rename.clicked.disconnect(self.toolButton_rename_clear_event)
                self.toolButton_rename.clicked.connect(self.toolButton_rename_event)
                self.toolButton_rename.setIcon(self.icon_edit)
                self.button_config['name'] = self.lineEdit_name.text()
                if self.button_config['name'] == '':
                    self.button_config['name'] = '默认工具全称'
                    self.lineEdit_name.setText('默认工具全称')
                # 简称
                self.lineEdit_simple_name.setReadOnly(True)
                self.toolButton_simple_rename.clicked.disconnect(self.toolButton_simple_rename_clear_event)
                self.toolButton_simple_rename.clicked.connect(self.toolButton_simple_rename_event)
                self.toolButton_simple_rename.setIcon(self.icon_edit)
                self.button_config['simple_name'] = self.lineEdit_simple_name.text()
                if self.button_config['simple_name'] == '':
                    self.button_config['simple_name'] = '默认工具简称'
                    self.lineEdit_simple_name.setText('默认工具简称')
                # 工具位置
                self.lineEdit_position.setReadOnly(True)
                folder_filename = self.lineEdit_position.text()
                if folder_filename != '':
                    file_all = folder_filename.replace('\\\\', '/').split('/')
                    file_url = ''
                    for i in file_all[:-1]:
                        file_url = file_url + i + '/'
                    self.button_config['folder'] = file_url
                    self.button_config['filename'] = file_all[-1]
                # 命令模板
                self.comboBox_command_template.setEditable(False)
                self.toolButton_command_template.clicked.disconnect(self.toolButton_command_template_delete_event)
                self.toolButton_command_template.clicked.connect(self.toolButton_command_template_event)
                self.toolButton_command_template.setIcon(self.icon_edit)
                # 命令介绍
                self.lineEdit_command_introduction.setReadOnly(True)
                self.toolButton_command_introduction.clicked.disconnect(
                    self.toolButton_command_introduction_clear_event)
                self.toolButton_command_introduction.clicked.connect(self.toolButton_command_introduction_event)
                self.toolButton_command_introduction.setIcon(self.icon_edit)
                # 命令示例
                self.lineEdit_command_example.setReadOnly(True)
                self.toolButton_command_example.clicked.disconnect(self.toolButton_command_example_clear_event)
                self.toolButton_command_example.clicked.connect(self.toolButton_command_example_event)
                self.toolButton_command_example.setIcon(self.icon_edit)
                # 固定命令
                self.comboBox_command_built_in.setEditable(False)
                self.toolButton_command_built_in.clicked.disconnect(self.toolButton_command_built_in_delete_event)
                self.toolButton_command_built_in.clicked.connect(self.toolButton_command_built_in_event)
                self.toolButton_command_built_in.setIcon(self.icon_edit)
                # 有效结果
                self.comboBox_result.setEditable(False)
                self.toolButton_result.clicked.disconnect(self.toolButton_result_delete_event)
                self.toolButton_result.clicked.connect(self.toolButton_result_event)
                self.toolButton_result.setIcon(self.icon_replace)
                # 工具说明
                self.plainTextEdit_introduction.setReadOnly(True)
                self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                # 保存配置
                self.save_config_event()
        except Exception as e:
            print(e, 'Tools_buttons_tool_event', 'button_edit_all_event')

    # 右侧按钮槽函数
    # 名称更改
    def toolButton_rename_event(self):
        if self.lineEdit_name.isReadOnly():
            self.lineEdit_name.setReadOnly(False)
            self.toolButton_rename.setIcon(self.icon_save)
        else:
            self.lineEdit_name.setReadOnly(True)
            self.toolButton_rename.setIcon(self.icon_edit)
            self.button_config['name'] = self.lineEdit_name.text()
            if self.button_config['name'] == '':
                self.button_config['name'] = '默认工具全称'
                self.lineEdit_name.setText('默认工具全称')
            self.save_config_event('name')

    # 名称清空
    def toolButton_rename_clear_event(self):
        self.lineEdit_name.clear()

    # 简称更改
    def toolButton_simple_rename_event(self):
        if self.lineEdit_simple_name.isReadOnly():
            self.lineEdit_simple_name.setReadOnly(False)
            self.toolButton_simple_rename.setIcon(self.icon_save)
        else:
            self.lineEdit_simple_name.setReadOnly(True)
            self.toolButton_simple_rename.setIcon(self.icon_edit)
            self.button_config['simple_name'] = self.lineEdit_simple_name.text()
            if self.button_config['simple_name'] == '' and self.button_config['name'] == '':
                self.button_config['simple_name'] = '默认工具简称'
                self.lineEdit_simple_name.setText('默认工具简称')
            elif self.button_config['simple_name'] == '':
                self.button_config['simple_name'] = self.button_config['name']
                self.lineEdit_simple_name.setText(self.button_config['name'])
            self.save_config_event('simple_name')

    # 简称清空
    def toolButton_simple_rename_clear_event(self):
        self.lineEdit_simple_name.clear()

    # 位置更改
    def toolButton_position_event(self):
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
            self.save_config_event('folder')
            self.save_config_event('filename')

    # 命令模板更改
    def toolButton_command_template_event(self):
        if self.comboBox_command_template.isEditable():
            self.comboBox_command_template.setEditable(False)
            self.toolButton_command_template.setIcon(self.icon_edit)
            self.comboBox_command_template.editTextChanged.disconnect(self.change_command_text_event)
            self.save_config_event('command_template')
        else:
            if len(self.button_config['command_template']) != 0:
                self.comboBox_command_template.setEditable(True)
                self.toolButton_command_template.setIcon(self.icon_save)
                self.comboBox_command_template.editTextChanged.connect(self.change_command_text_event)

    # 命令模板删除行
    def toolButton_command_template_delete_event(self):
        if QMessageBox.warning(self, "操作确认", '是否删除这一项？\n删除后不可恢复！', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            if len(self.button_config['command_template']) > 0:
                index = self.comboBox_command_template.currentIndex()
                self.comboBox_command_template.removeItem(index)
                self.button_config['command_template'].pop(index)
                self.button_config['command_introduction'].pop(index)
                self.button_config['command_example'].pop(index)
                if len(self.button_config['command_template']) == 0:
                    self.lineEdit_command_introduction.setText('')
                    self.lineEdit_command_example.setText('')
                    self.comboBox_command_template.setEditable(False)
                    self.lineEdit_command_introduction.setReadOnly(True)
                    self.lineEdit_command_example.setReadOnly(True)
                else:
                    self.lineEdit_command_introduction.setText(self.button_config['command_introduction'][self.comboBox_command_template.currentIndex()])
                    self.lineEdit_command_example.setText(self.button_config['command_example'][self.comboBox_command_template.currentIndex()])

    # 命令介绍更改
    def toolButton_command_introduction_event(self):
        if len(self.button_config['command_template']) != 0:
            if self.lineEdit_command_introduction.isReadOnly():
                self.lineEdit_command_introduction.setReadOnly(False)
                self.toolButton_command_introduction.setIcon(self.icon_save)
            else:
                self.lineEdit_command_introduction.setReadOnly(True)
                self.toolButton_command_introduction.setIcon(self.icon_edit)
                self.button_config['command_introduction'][self.comboBox_command_template.currentIndex()] = self.lineEdit_command_introduction.text()
                self.save_config_event('command_introduction')

    # 命令介绍清空
    def toolButton_command_introduction_clear_event(self):
        self.lineEdit_command_introduction.clear()

    # 命令示例更改
    def toolButton_command_example_event(self):
        if len(self.button_config['command_template']) != 0:
            if self.lineEdit_command_example.isReadOnly():
                self.lineEdit_command_example.setReadOnly(False)
                self.toolButton_command_example.setIcon(self.icon_save)
            else:
                self.lineEdit_command_example.setReadOnly(True)
                self.toolButton_command_example.setIcon(self.icon_edit)
                self.button_config['command_example'][self.comboBox_command_template.currentIndex()] = self.lineEdit_command_example.text()
                self.save_config_event('command_example')

    # 命令示例清空
    def toolButton_command_example_clear_event(self):
        self.lineEdit_command_example.clear()

    # 固定命令更改
    def toolButton_command_built_in_event(self):
        if len(self.button_config['command_built_in']) != 0:
            if self.comboBox_command_built_in.isEditable():
                self.comboBox_command_built_in.setEditable(False)
                self.toolButton_command_built_in.setIcon(self.icon_edit)
                self.comboBox_command_built_in.editTextChanged.disconnect(self.change_command_built_in_text_event)
                self.save_config_event('command_built_in')
            else:
                self.comboBox_command_built_in.setEditable(True)
                self.toolButton_command_built_in.setIcon(self.icon_save)
                self.comboBox_command_built_in.editTextChanged.connect(self.change_command_built_in_text_event)

    # 固定命令删除行
    def toolButton_command_built_in_delete_event(self):
        if QMessageBox.warning(self, "操作确认", '是否删除这一项？\n删除后不可恢复！',
                               QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            if len(self.button_config['command_built_in']) > 0:
                index = self.comboBox_command_built_in.currentIndex()
                self.comboBox_command_built_in.removeItem(index)
                self.button_config['command_built_in'].pop(index)
                if len(self.button_config['command_built_in']) == 0:
                    self.comboBox_command_built_in.setEditable(False)

    # 有效结果更改
    def toolButton_result_event(self):
        if len(self.button_config['result']) != 0:
            if self.comboBox_result.isEditable():
                self.comboBox_result.setEditable(False)
                self.toolButton_result.setIcon(self.icon_edit)
                self.comboBox_result.editTextChanged.disconnect(self.change_result_text_event)
                self.save_config_event('result')
            else:
                self.comboBox_result.setEditable(True)
                self.toolButton_result.setIcon(self.icon_save)
                self.comboBox_result.editTextChanged.connect(self.change_result_text_event)

    # 有效结果删除行
    def toolButton_result_delete_event(self):
        if self.comboBox_result.currentIndex() == 0:
            QMessageBox.warning(self, "操作提示", '该项不可删除！', QMessageBox.Ok)
        else:
            if QMessageBox.warning(self, "操作确认", '是否删除这一项？\n删除后不可恢复！',
                                   QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                if len(self.button_config['result']) > 0:
                    index = self.comboBox_result.currentIndex()
                    self.comboBox_result.removeItem(index)
                    self.button_config['result'].pop(index)
                    if len(self.button_config['result']) == 0:
                        self.comboBox_result.setEditable(False)
            # if len(self.button_config['result']) > 0:
            #     i = 0
            #     index = self.comboBox_result.currentIndex()
            #     self.comboBox_result.removeItem(index)
            #     for j in self.button_config['result'].keys():
            #         if i == index:
            #             self.button_config['result'].pop(j)
            #             break
            #         i += 1
            #     if len(self.button_config['result']) == 0:
            #         self.comboBox_result.setEditable(False)