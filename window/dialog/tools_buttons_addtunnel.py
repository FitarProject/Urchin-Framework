from window.ui.tools_buttons_addtunnel_dialog import Ui_tools_buttons_addtunnel_dialog

from PyQt5.Qt import *


class Tools_buttons_addtunnel_event(QWidget, Ui_tools_buttons_addtunnel_dialog):
    tunnel_add = pyqtSignal(dict)
    tunnel_close = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.button_config = {
                    "name": "",
                    "position": '',
                    "input": [],
                    "output": ["output_1"],
                    "introduction": "",
                }
        self.input_num = 0
        self.output_num = 1
        self.setupUi(self)

    def setupUi(self, tools_buttons_addtunnel_dialog):
        super().setupUi(tools_buttons_addtunnel_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            self.set_icon()
            # 填充内容
            self.lineEdit_name.setPlaceholderText('请输入通道名称')
            self.lineEdit_position.setPlaceholderText('请输入脚本位置')
            self.list_output.addItems(self.button_config['output'])
            self.plainTextEdit_introduction.setPlaceholderText('请输入通道说明')
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'setupUi')
        # 连接下侧按钮的信号与槽
        self.button_yes.clicked.connect(self.button_yes_event)
        self.button_no.clicked.connect(self.button_no_event)
        # 连接右侧按钮的信号与槽
        self.button_name.clicked.connect(self.button_name_clear_event)
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
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'closeEvent')

    # 设置图标
    def set_icon(self):
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_select_file = QIcon("resource/image/folder.png")
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_del = QIcon("resource/image/del.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        self.button_name.setIcon(self.icon_clear)
        self.button_position.setIcon(self.icon_select_file)
        self.button_addinput.setIcon(self.icon_add)
        self.button_delinput.setIcon(self.icon_del)
        self.button_addoutput.setIcon(self.icon_add)
        self.button_deloutput.setIcon(self.icon_del)

    # 检查配置内容
    def check_config(self):
        try:
            if len(self.lineEdit_name.text()) == 0:
                QMessageBox.warning(self, "操作提示", '通道名称不可为空！', QMessageBox.Ok)
                return False
            elif len(self.lineEdit_position.text()) == 0:
                QMessageBox.warning(self, "操作提示", '脚本位置不可为空！', QMessageBox.Ok)
                return False
            else:
                return True
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'check_config')

    # 自定义槽函数
    # 添加通道
    def button_yes_event(self):
        try:
            if self.check_config() == True:
                self.button_config['name'] = self.lineEdit_name.text()
                self.button_config['position'] = self.lineEdit_position.text()
                self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                # 发射添加信号
                self.tunnel_add.emit(self.button_config)
                self.close()
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'button_yes_event')

    def button_no_event(self):
        self.close()

    # 右侧按钮槽函数
    # 名称清空
    def button_name_clear_event(self):
        self.lineEdit_name.clear()

    # 位置选择
    def button_position_event(self):
        select_file, file_type = QFileDialog.getOpenFileName(self, '选择文件', './script/', 'py(*.py)')
        if select_file != '':
            self.lineEdit_position.setText(select_file)
            self.button_config['position'] = select_file

    # 添加输入变量
    def button_addinput_event(self):
        try:
            self.input_num += 1
            new_input = 'input_' + str(self.input_num)
            self.button_config['input'].append(new_input)
            self.list_input.addItem(new_input)
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'button_addinput_event')

    # 去除输入变量
    def button_delinput_event(self):
        try:
            if self.input_num > 0:
                self.input_num -= 1
                self.list_input.takeItem(self.input_num)
                self.button_config['input'].pop(-1)
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'button_delinput_event')

    # 添加输出变量
    def button_addoutput_event(self):
        try:
            self.output_num += 1
            new_output = 'output_' + str(self.output_num)
            self.button_config['output'].append(new_output)
            self.list_output.addItem(new_output)
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'button_addoutput_event')

    # 去除输出变量
    def button_deloutput_event(self):
        try:
            if self.output_num > 1:
                self.output_num -= 1
                self.list_output.takeItem(self.output_num)
                self.button_config['output'].pop(-1)
        except Exception as e:
            print(e, 'Tools_buttons_addtunnel_event', 'button_deloutput_event')
