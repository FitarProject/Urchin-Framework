from window.ui.tools_tool_add_command_built_in_dialog import Ui_tools_tool_add_command_built_in_dialog

from PyQt5.Qt import *


class Tools_tool_add_command_built_in_event(QWidget, Ui_tools_tool_add_command_built_in_dialog):
    tool_add_command_built_in = pyqtSignal(bool, str)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.setupUi(self)

    def setupUi(self, tools_tool_add_command_built_in_dialog):
        super().setupUi(tools_tool_add_command_built_in_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            if len(self.filename) != 0:
                new_text = self.filename + ' -h'
            else:
                new_text = 'Toolname -h'
            self.lineEdit_command_built_in.setPlaceholderText(new_text)
        except Exception as e:
            print(e)
        self.button_yes.clicked.connect(self.yes_event)
        self.button_no.clicked.connect(self.no_event)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.tool_add_command_built_in.emit(False, '')

    def yes_event(self):
        if self.lineEdit_command_built_in.text() != '':
            self.tool_add_command_built_in.emit(True, self.lineEdit_command_built_in.text())
            self.close()
        else:
            QMessageBox.warning(self, "操作提示", '固定命令不可为空！', QMessageBox.Ok)

    def no_event(self):
        self.close()
