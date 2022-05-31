from window.ui.tools_tool_add_result_dialog import Ui_tools_tool_add_result_dialog

from PyQt5.Qt import *


class Tools_tool_add_result_event(QWidget, Ui_tools_tool_add_result_dialog):
    tool_add_result = pyqtSignal(bool, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, tools_tool_add_result_dialog):
        super().setupUi(tools_tool_add_result_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        self.lineEdit_result.setPlaceholderText('./output_1.txt')
        self.button_yes.clicked.connect(self.yes_event)
        self.button_no.clicked.connect(self.no_event)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.tool_add_result.emit(False, '')

    def yes_event(self):
        if self.lineEdit_result.text() != '':
            self.tool_add_result.emit(True, self.lineEdit_result.text())
            self.close()
        else:
            QMessageBox.warning(self, "操作提示", '命令模板不可为空！', QMessageBox.Ok)

    def no_event(self):
        self.close()
