from window.ui.tools_tool_add_command_template_dialog import Ui_tools_tool_add_command_template_dialog

from PyQt5.Qt import *


class Tools_tool_add_command_template_event(QWidget, Ui_tools_tool_add_command_template_dialog):
    tool_add_command_template = pyqtSignal(bool, str, str, str)

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.setupUi(self)

    def setupUi(self, tools_tool_add_command_template_dialog):
        super().setupUi(tools_tool_add_command_template_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        try:
            if len(self.filename) != 0:
                new_text = self.filename + ' -xxx {input_1}'
            else:
                new_text = 'Toolname -xxx {input_1}'
            self.lineEdit_command_template.setPlaceholderText(new_text)
            # self.lineEdit_command_example.setText(new_text)
            # self.lineEdit_command_introduction.setText('Tool\'s introduction')
        except Exception as e:
            print(e, 'setupUi', 'Tools_tool_add_command_template_event')
        self.button_yes.clicked.connect(self.yes_event)
        self.button_no.clicked.connect(self.no_event)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.tool_add_command_template.emit(False, '', '', '')

    def yes_event(self):
        if self.lineEdit_command_template.text() != '':
            self.tool_add_command_template.emit(True, self.lineEdit_command_template.text(), self.lineEdit_command_introduction.text(), self.lineEdit_command_example.text())
            self.close()
        else:
            QMessageBox.warning(self, "操作提示", '命令模板不可为空！', QMessageBox.Ok)

    def no_event(self):
        self.close()
