from window.ui.tools_tunnel_edit_script_dialog import Ui_tools_tunnel_edit_script_dialog

from PyQt5.Qt import *


class Tools_tunnel_edit_script_event(QWidget, Ui_tools_tunnel_edit_script_dialog):
    script_close = pyqtSignal()
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.script = []
        self.script_encode = '#!/usr/bin/env python3\n# -*- coding=utf-8 -*-\n'
        self.script_import = ''
        self.script_def = ''
        self.script_head = ''
        self.script_body = ''
        self.script_tail = ''
        self.temp_top = '\n###########################上面不要动###########################\n'
        self.temp_botton = '\n###########################下面不要动###########################\n'
        self.setupUi(self)

    def setupUi(self, tools_tunnel_edit_script_dialog):
        super().setupUi(tools_tunnel_edit_script_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        self.read_script()
        self.lineEdit_position.setText(self.position)
        self.lineEdit_package.setText(self.script_import)
        # print('self.script_head:\n'+self.script_head+'self.script_body:\n'+self.script_body+'self.script_tail:\n'+self.script_tail)
        self.plainTextEdit_head.setPlainText(self.script_encode + 'import ' + self.script_import + '\n' + self.script_def)
        self.plainTextEdit_body.setPlainText(self.script_body)
        self.plainTextEdit_tail.setPlainText(self.script_tail)

        self.button_edit.clicked.connect(self.button_edit_event)

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            self.script_close.emit()
        except Exception as e:
            print(e, 'Tools_tunnel_edit_script_event', 'closeEvent')

    def read_script(self):
        try:
            with open(self.position, 'r', encoding='utf-8') as f:
                self.script = f.readlines()
            index = 0
            for i in self.script:
                if i.startswith('import'):
                    self.script_import = i[7:].rstrip('\n')
                if i.startswith('def'):
                    self.script_def = i.rstrip('\n')
                    index = self.script.index(i)
                    break
            for i in self.script[index+1:]:
                if i.startswith('    return'):
                    self.script_tail = i.rstrip('\n')
                    break
                if i.startswith('###########################上'):
                    continue
                if i.startswith('###########################下'):
                    continue
                self.script_body += i
            self.script_head = self.script_encode + '\nimport ' + self.script_import + '\n\n' + self.script_def
        except Exception as e:
            print(e, 'Tools_tunnel_edit_script_event', 'read_script')

    def save_script(self):
        try:
            if self.script_import.isspace():
                self.script_head = self.script_encode + '\n' + self.script_def
            else:
                self.script_head = self.script_encode + '\nimport ' + self.script_import + '\n\n' + self.script_def
            with open(self.position, 'w', encoding='utf-8') as f:
                f.write(self.script_head + self.temp_top)
                f.write(self.script_body)
                f.write(self.temp_botton + self.script_tail + '\n')
        except Exception as e:
            print(e, 'Tools_tunnel_edit_script_event', 'save_script')

    def button_edit_event(self):
        try:
            if self.lineEdit_package.isReadOnly():
                self.lineEdit_package.setReadOnly(False)
                self.plainTextEdit_body.setReadOnly(False)
                self.lineEdit_package.textChanged.connect(self.change_package_event)
                self.button_edit.setText('保存\n脚本')
            else:
                self.lineEdit_package.setReadOnly(True)
                self.plainTextEdit_body.setReadOnly(True)
                self.lineEdit_package.textChanged.disconnect(self.change_package_event)
                self.button_edit.setText('编辑\n脚本')
                self.script_import = self.lineEdit_package.text()
                # 替换制表符，很重要！
                self.script_body = self.plainTextEdit_body.toPlainText().replace('\t', '    ')
                self.save_script()
        except Exception as e:
            print(e, 'Tools_tunnel_edit_script_event', 'button_edit_event')

    def change_package_event(self, new_text):
        self.plainTextEdit_head.setPlainText(self.script_encode + 'import ' + new_text + '\n' + self.script_def)
