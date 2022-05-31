from window.ui.tools_buttons_command_dialog import Ui_tools_buttons_command_dialog
from window.func.get_cmd_out import cmd_exec
from string import Template
import subprocess, re, logging

from PyQt5.Qt import *


class Tools_buttons_command_event(QWidget, Ui_tools_buttons_command_dialog):
    command_refresh = pyqtSignal(str, dict, str)
    command_close = pyqtSignal()

    def __init__(self, button_object, button_config):
        super().__init__()
        self.variable_index = []
        self.var_map = {}
        self.button_object = button_object
        self.button_config = button_config
        self.variable_num = len(button_config['variable'])
        self.save_flag = True
        self.setupUi(self)

    def setupUi(self, tools_buttons_command_dialog):
        super().setupUi(tools_buttons_command_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            if self.button_config['name'] == '':
                self.button_config['name'] = '默认命令名称'
                self.save_config_event('name')
            self.set_icon()
            # 填充内容
            self.lineEdit_name.setText(self.button_config['name'])
            self.lineEdit_command.setText(self.button_config['command'])
            for i in self.button_config['variable']:
                # 添加根节点
                root = QTreeWidgetItem(self.list_variable)
                new_variable = 'variable_' + str(self.button_config['variable'].index(i) + 1)
                root.setText(0, new_variable)
                root.setText(1, i)
                root.setFlags(root.flags() | Qt.ItemIsEditable)
                self.variable_index.append(new_variable)
                self.var_map[new_variable] = i
                self.list_variable.addTopLevelItem(root)
            self.plainTextEdit_introduction.setPlainText(self.button_config['introduction'])
            # 连接下侧按钮的信号与槽
            self.button_exec.clicked.connect(self.button_exec_event)
            self.button_edit.clicked.connect(self.button_edit_event)
            # 连接右侧按钮的信号与槽
            self.button_name.clicked.connect(self.button_name_event)
            self.button_command.clicked.connect(self.button_command_event)
            self.button_addvariable.clicked.connect(self.button_addvariable_event)
            self.button_editvariable.clicked.connect(self.button_editvariable_event)
            self.button_delvariable.clicked.connect(self.button_delvariable_event)
            # 列表信息改变
            self.list_variable.itemChanged.connect(self.list_change_event)
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'setupUi')

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            self.command_close.emit()
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'closeEvent')

    # 设置图标
    def set_icon(self):
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_add = QIcon("resource/image/add.png")
        self.icon_del = QIcon("resource/image/del.png")
        self.icon_clear = QIcon("resource/image/clear.png")
        self.button_name.setIcon(self.icon_edit)
        self.button_command.setIcon(self.icon_edit)
        self.button_addvariable.setIcon(self.icon_add)
        self.button_editvariable.setIcon(self.icon_edit)
        self.button_delvariable.setIcon(self.icon_del)

    # 返回配置给主界面
    def save_config_event(self, subitem_name='all'):
        try:
            self.command_refresh.emit(self.button_object, self.button_config, subitem_name)
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'save_config_event')

    # 自定义槽函数
    # 下侧按钮槽函数
    # 执行按钮
    def button_exec_event(self):
        try:
            if self.save_flag:
                pass
                # 暂时定为直接打开新终端执行命令
                # for i,j in zip(self.variable_index, self.button_config['variable']):
                #     self.var_map[i] = j
                command = Template(self.button_config['command']).safe_substitute(self.var_map)
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
                try:
                    process = cmd_exec(command, ensure_success=False)
                except Exception as e:
                    print(e, 'cmd_exec')
            else:
                QMessageBox.warning(self, "操作提示", '请先保存修改！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_exec_event')

    # 快速编辑
    def button_edit_event(self):
        try:
            if self.button_edit.text() == '编辑':
                self.save_flag = False
                self.button_edit.setText('保存')
                self.button_addvariable.clicked.disconnect(self.button_addvariable_event)
                self.button_editvariable.clicked.disconnect(self.button_editvariable_event)
                self.button_delvariable.clicked.disconnect(self.button_delvariable_event)
                # 名称
                self.lineEdit_name.setReadOnly(False)
                self.button_name.clicked.disconnect(self.button_name_event)
                self.button_name.clicked.connect(self.button_name_clear_event)
                self.button_name.setIcon(self.icon_clear)
                # 命令详情
                self.lineEdit_command.setReadOnly(False)
                self.button_command.clicked.disconnect(self.button_command_event)
                self.button_command.clicked.connect(self.button_command_clear_event)
                self.button_command.setIcon(self.icon_clear)
                # 参数变量
                for i in range(self.variable_num):
                    self.list_variable.openPersistentEditor(self.list_variable.topLevelItem(i), 1)
                # 说明
                self.plainTextEdit_introduction.setReadOnly(False)
            else:
                self.save_flag = True
                self.button_edit.setText('编辑')
                self.button_addvariable.clicked.connect(self.button_addvariable_event)
                self.button_editvariable.clicked.connect(self.button_editvariable_event)
                self.button_delvariable.clicked.connect(self.button_delvariable_event)
                # 名称
                self.lineEdit_name.setReadOnly(True)
                self.button_name.clicked.disconnect(self.button_name_clear_event)
                self.button_name.clicked.connect(self.button_name_event)
                self.button_name.setIcon(self.icon_edit)
                self.button_config['name'] = self.lineEdit_name.text()
                if self.button_config['name'] == '':
                    self.button_config['name'] = '默认命令名称'
                    self.lineEdit_name.setText('默认命令名称')
                # 命令详情
                self.lineEdit_command.setReadOnly(True)
                self.button_command.clicked.disconnect(self.button_command_clear_event)
                self.button_command.clicked.connect(self.button_command_event)
                self.button_command.setIcon(self.icon_edit)
                self.button_config['command'] = self.lineEdit_command.text()
                # 参数变量
                for i in range(self.variable_num):
                    self.list_variable.closePersistentEditor(self.list_variable.topLevelItem(i), 1)
                # 说明
                self.plainTextEdit_introduction.setReadOnly(True)
                self.button_config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                # 保存配置
                self.save_config_event()
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_edit_event')

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
                    self.button_config['name'] = '默认命令名称'
                    self.lineEdit_name.setText('默认命令名称')
                self.save_config_event('name')
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_name_event')

    # 名称清空
    def button_name_clear_event(self):
        self.lineEdit_name.clear()

    # 修改命令详情
    def button_command_event(self):
        try:
            if self.lineEdit_command.isReadOnly():
                self.lineEdit_command.setReadOnly(False)
                self.button_command.setIcon(self.icon_save)
            else:
                self.lineEdit_command.setReadOnly(True)
                self.button_command.setIcon(self.icon_edit)
                self.button_config['command'] = self.lineEdit_command.text()
                self.save_config_event('command')
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_command_event')

    # 命令清空
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
            self.variable_index.append(new_variable)
            self.var_map[new_variable] = new_variable
            root.setFlags(root.flags() | Qt.ItemIsEditable)
            self.list_variable.addTopLevelItem(root)
            self.button_config['variable'].append(new_variable)
            self.lineEdit_command.setText(self.lineEdit_command.text() + ' $variable_' + str(self.variable_num))
            self.button_config['command'] = self.lineEdit_command.text()
            self.save_config_event('command')
            self.save_config_event('variable')
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_addvariable_event')

    # 编辑变量
    def button_editvariable_event(self):
        try:
            self.list_variable.editItem(self.list_variable.currentItem(), 1)
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_addvariable_event')

    # 去除变量
    def button_delvariable_event(self):
        try:
            if self.variable_num > 0:
                if self.lineEdit_command.text().endswith(' $variable_' + str(self.variable_num)):
                    self.lineEdit_command.setText(self.lineEdit_command.text().rstrip(' $variable_' + str(self.variable_num)))
                self.variable_num -= 1
                self.list_variable.takeTopLevelItem(self.variable_num)
                self.var_map.pop(self.variable_index[-1])
                self.variable_index.pop(-1)
                self.button_config['variable'].pop(-1)
                self.save_config_event('variable')
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'button_delvariable_event')

    # 变量列表变化事件
    def list_change_event(self, item, col):
        try:
            if item == self.list_variable.currentItem():
                num = re.findall(r'[0-9]+', item.text(0))
                index = int(num[0])
                self.button_config['variable'][index-1] = item.text(col)
                self.var_map[item.text(0)] = item.text(col)
                self.save_config_event('variable')
        except Exception as e:
            print(e, 'Tools_buttons_command_event', 'list_change_event')