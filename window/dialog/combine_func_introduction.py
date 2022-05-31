from window.ui.combine_func_introduction_dialog import Ui_combine_func_introduction_dialog

from PyQt5.Qt import *
import json


class Combine_func_introduction_event(QWidget, Ui_combine_func_introduction_dialog):
    dialog_close = pyqtSignal()
    signal_yes = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.config = None
        self.read_config()
        self.setupUi(self)

    def setupUi(self, combine_func_introduction_dialog):
        super().setupUi(combine_func_introduction_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        self.lineEdit.setText(self.config['name'])
        self.plainTextEdit.setPlainText(self.config['introduction'])
        self.button_yes.clicked.connect(self.button_yes_event)
        self.button_no.clicked.connect(self.button_no_event)

    def read_config(self):
        with open('config/combine_variable.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def save_config(self):
        with open('config/combine_variable.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.dialog_close.emit()

    def button_yes_event(self):
        self.config['name'] = self.lineEdit.text()
        self.config['introduction'] = self.plainTextEdit.toPlainText()
        self.save_config()
        self.signal_yes.emit()
        self.close()

    def button_no_event(self):
        self.close()
