from window.ui.tools_buttons_tunnel_dialog import Ui_tools_buttons_tunnel_dialog
from window.dialog.tools_tunnel_edit_script import Tools_tunnel_edit_script_event
from window.dialog.tools_tunnel_edit_customscript import Tools_tunnel_edit_customscript_event

import json
from PyQt5.Qt import *


class Tools_buttons_tunnel_event(QWidget, Ui_tools_buttons_tunnel_dialog):
    tunnel_refresh = pyqtSignal(str, dict, str)
    tunnel_close = pyqtSignal()
    refresh_selected_tunnel = pyqtSignal()

    def __init__(self, button_object, button_config):
        super().__init__()
        self.button_object = button_object
        self.button_config = button_config
        self.input_num = len(button_config['input'])
        self.output_num = len(button_config['output'])
        self.save_flag = True
        self.childwindow_flag_script = False
        self.setupUi(self)

    def setupUi(self, tools_buttons_tunnel_dialog):
        super().setupUi(tools_buttons_tunnel_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            if self.button_config['name'] == '':
                self.button_config['name'] = '默认通道名称'
                self.save_config_event('name')
            for i in range(self.input_num):
                self.button_config['input'][i] = 'input_' + str(i + 1)
            for i in range(self.output_num):
                self.button_config['output'][i] = 'output_' + str(i + 1)
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'setupUi')
        try:
            self.set_icon()
            # 填充内容
            self.lineEdit_name.setText(self.button_config['name'])
            self.lineEdit_position.setText(self.button_config['position'])
            self.list_input.addItems(self.button_config['input'])
            self.list_output.addItems(self.button_config['output'])
            self.plainTextEdit_introduction.setPlainText(self.button_config['introduction'])
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'setupUi')
        # 连接下侧按钮的信号与槽
        self.button_edit_script.clicked.connect(self.button_edit_script_event)
        self.button_add_to_selected.clicked.connect(self.button_add_to_selected_event)
        self.button_editall.clicked.connect(self.button_editall_event)
        # 连接右侧按钮的信号与槽
        self.button_name.clicked.connect(self.button_name_event)
        self.button_position.clicked.connect(self.button_position_event)
        self.button_addinput.clicked.connect(self.button_addinput_event)
        self.button_delinput.clicked.connect(self.button_delinput_event)
        self.button_addoutput.clicked.connect(self.button_addoutput_event)
        self.button_deloutput.clicked.connect(self.button_deloutput_event)

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            # 发送关闭信号（配置已保存）
            self.tunnel_close.emit()
            if self.childwindow_flag_script:
                self.tunnel_edit_script.close()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'closeEvent')

    # 设置图标
    def set_icon(self):
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_select_file = QIcon("resource/image/folder.png")
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_del = QIcon("resource/image/del.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        self.button_name.setIcon(self.icon_edit)
        self.button_position.setIcon(self.icon_select_file)
        self.button_addinput.setIcon(self.icon_add)
        self.button_delinput.setIcon(self.icon_del)
        self.button_addoutput.setIcon(self.icon_add)
        self.button_deloutput.setIcon(self.icon_del)

    # 返回配置给主界面
    def save_config_event(self, subitem_name='all'):
        try:
            self.tunnel_refresh.emit(self.button_object, self.button_config, subitem_name)
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'save_config_event')

    # 自定义槽函数
    # 下侧按钮槽函数
    # 编辑通道脚本
    def button_edit_script_event(self):
        try:
            if self.save_flag:
                if self.button_config['position'].startswith('./script/'):
                    self.tunnel_edit_script = Tools_tunnel_edit_script_event(self.button_config['position'])
                    self.childwindow_flag_script = True
                    self.tunnel_edit_script.show()
                else:
                    self.tunnel_edit_script = Tools_tunnel_edit_customscript_event(self.button_config['position'])
                    # self.tunnel_edit_script = Tools_tunnel_edit_script_event(self.button_config['position'])
                    self.childwindow_flag_script = True
                    self.tunnel_edit_script.show()
            else:
                QMessageBox.warning(self, "操作提示", '请先保存修改！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_edit_script_event')

    # 添加为炼金
    def button_add_to_selected_event(self):
        if QMessageBox.warning(self, "操作确认", '是否添加通道\n"' + self.button_config['name'] + '"\n至炼金工坊预选区域？', QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
            config = {"name": self.button_config['name'], "button_num": self.button_object}
            with open('config/selected_tunnel.json', 'r', encoding='utf-8') as f:
                selected_tunnel = json.load(f)
            selected_tunnel['selected_tunnel'].append(config)
            with open('config/selected_tunnel.json', 'w', encoding='utf-8') as f:
                json.dump(selected_tunnel, f)
            self.refresh_selected_tunnel.emit()

    # 快速编辑
    def button_editall_event(self):
        try:
            if self.button_editall.text() == '快速编辑':
                self.save_flag = False
                self.button_editall.setText('保存')
                # 名称
                self.lineEdit_name.setReadOnly(False)
                self.button_name.clicked.disconnect(self.button_name_event)
                self.button_name.clicked.connect(self.button_name_clear_event)
                self.button_name.setIcon(self.icon_clear)
                # 脚本位置
                self.lineEdit_position.setReadOnly(False)
                # 通道说明
                self.plainTextEdit_introduction.setReadOnly(False)
            else:
                self.save_flag = True
                self.button_editall.setText('快速编辑')
                # 名称
                self.lineEdit_name.setReadOnly(True)
                self.button_name.clicked.disconnect(self.button_name_clear_event)
                self.button_name.clicked.connect(self.button_name_event)
                self.button_name.setIcon(self.icon_edit)
                self.button_config['name'] = self.lineEdit_name.text()
                if self.button_config['name'] == '':
                    self.button_config['name'] = '默认通道名称'
                    self.lineEdit_name.setText('默认通道名称')
                # 脚本位置
                self.lineEdit_position.setReadOnly(True)
                self.button_config['position'] = self.lineEdit_position.text()
                # 通道说明
                self.plainTextEdit_introduction.setReadOnly(True)
                self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                # 保存配置
                self.save_config_event()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_editall_event')

    # 右侧按钮槽函数
    # 名称更改
    def button_name_event(self):
        try:
            if self.lineEdit_name.isReadOnly():
                self.lineEdit_name.setReadOnly(False)
                self.button_name.setIcon(self.icon_save)
            else:
                self.lineEdit_name.setReadOnly(True)
                self.button_name.setIcon(self.icon_edit)
                self.button_config['name'] = self.lineEdit_name.text()
                if self.button_config['name'] == '':
                    self.button_config['name'] = '默认通道名称'
                    self.lineEdit_name.setText('默认通道名称')
                self.save_config_event('name')
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_name_event')

    # 名称清空
    def button_name_clear_event(self):
        self.lineEdit_name.clear()

    # 位置选择
    def button_position_event(self):
        select_file, file_type = QFileDialog.getOpenFileName(self, '选择文件', './script/', 'py(*.py)')
        if select_file != '':
            self.lineEdit_position.setText(select_file)
            self.button_config['position'] = select_file
            self.save_config_event('position')

    # 添加输入变量
    def button_addinput_event(self):
        try:
            self.input_num += 1
            new_input = 'input_' + str(self.input_num)
            self.button_config['input'].append(new_input)
            self.list_input.addItem(new_input)
            self.save_config_event('input')
            self.change_script_input()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_addinput_event')

    # 去除输入变量
    def button_delinput_event(self):
        try:
            if self.input_num > 0:
                self.input_num -= 1
                self.list_input.takeItem(self.input_num)
                self.button_config['input'].pop(-1)
                self.save_config_event('input')
                self.change_script_input()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_delinput_event')

    # 添加输出变量
    def button_addoutput_event(self):
        try:
            self.output_num += 1
            new_output = 'output_' + str(self.output_num)
            self.button_config['output'].append(new_output)
            self.list_output.addItem(new_output)
            self.save_config_event('output')
            self.change_script_output()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_addoutput_event')

    # 去除输出变量
    def button_deloutput_event(self):
        try:
            if self.output_num > 1:
                self.output_num -= 1
                self.list_output.takeItem(self.output_num)
                self.button_config['output'].pop(-1)
                self.save_config_event('output')
                self.change_script_output()
        except Exception as e:
            print(e, 'Tools_buttons_tunnel_event', 'button_deloutput_event')

    # 脚本变量改变函数
    def change_script_input(self):
        with open(self.button_config['position'], 'r', encoding='utf-8') as f:
            script = f.readlines()
        new_input = ''
        if self.input_num > 0:
            for i in self.button_config['input']:
                new_input += i + '=any, '
            new_input = new_input.rstrip(', ')
        for i in script:
            if i.startswith('def deal_data('):
                script[script.index(i)] = 'def deal_data(' + new_input + '):\n'
                break
        with open(self.button_config['position'], 'w', encoding='utf-8') as f:
            f.writelines(script)

    def change_script_output(self):
        with open(self.button_config['position'], 'r', encoding='utf-8') as f:
            script = f.readlines()
        new_output = ''
        for i in self.button_config['output']:
            new_output += i + ', '
        new_output = new_output.rstrip(', ')
        for i in script:
            if i.startswith('    return output_1'):
                script[script.index(i)] = '    return ' + new_output + '\n'
                break
        with open(self.button_config['position'], 'w', encoding='utf-8') as f:
            f.writelines(script)