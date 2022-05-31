from window.ui.tools_tunnel_edit_customscript_dialog import Ui_tools_tunnel_edit_customscript_dialog

from PyQt5.Qt import *


class Tools_tunnel_edit_customscript_event(QWidget, Ui_tools_tunnel_edit_customscript_dialog):
    script_close = pyqtSignal()
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.script = []
        self.script_body = ''
        self.setupUi(self)

    def setupUi(self, tools_tunnel_edit_customscript_dialog):
        super().setupUi(tools_tunnel_edit_customscript_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        self.read_script()
        self.lineEdit_position.setText(self.position)
        self.plainTextEdit_body.setPlainText(self.script_body)
        self.button_edit.clicked.connect(self.button_edit_event)

    def closeEvent(self, QCloseEvent):
        try:
            super().closeEvent(QCloseEvent)
            self.script_close.emit()
        except Exception as e:
            print(e, 'Tools_tunnel_edit_customscript_event', 'closeEvent')

    def read_script(self):
        try:
            with open(self.position, 'r', encoding='utf-8') as f:
                self.script = f.readlines()
            for i in self.script:
                self.script_body += i
        except Exception as e:
            print(e, 'Tools_tunnel_edit_customscript_event', 'read_script')

    def save_script(self):
        try:
            with open(self.position, 'w', encoding='utf-8') as f:
                f.write(self.script_body)
        except Exception as e:
            print(e, 'Tools_tunnel_edit_customscript_event', 'save_script')

    def button_edit_event(self):
        try:
            if self.plainTextEdit_body.isReadOnly():
                self.plainTextEdit_body.setReadOnly(False)
                self.button_edit.setText('保存\n脚本')
            else:
                self.plainTextEdit_body.setReadOnly(True)
                self.button_edit.setText('编辑\n脚本')
                # 替换制表符，很重要！
                self.script_body = self.plainTextEdit_body.toPlainText().replace('\t', '    ')
                self.save_script()
        except Exception as e:
            print(e, 'Tools_tunnel_edit_customscript_event', 'button_edit_event')
