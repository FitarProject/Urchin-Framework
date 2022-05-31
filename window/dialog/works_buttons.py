from window.ui.works_buttons_dialog import Ui_works_buttons_dialog

from PyQt5.Qt import *


class Works_buttons_event(QWidget, Ui_works_buttons_dialog):
    dialog_close = pyqtSignal()
    signal_add_task = pyqtSignal(str)

    def __init__(self, object_name, config):
        super().__init__()
        self.object_name = object_name
        self.config = config
        self.setupUi(self)
        self.init_list()

    def setupUi(self, works_buttons_dialog):
        try:
            super().setupUi(works_buttons_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.button_yes.clicked.connect(self.button_yes_event)
            self.button_no.clicked.connect(self.button_no_event)
        except Exception as e:
            print(e, 'Works_buttons_event', 'setupUi')

    def closeEvent(self, event):
        super().closeEvent(event)
        self.dialog_close.emit()

    def init_list(self):
        try:
            self.lineEdit_name.setText(self.config['name'])
            self.plainTextEdit_introduction.setPlainText(self.config['introduction'])
            for i in self.config['variable']:
                root = QTreeWidgetItem(self.treeWidget_variable)
                root.setText(0, i['position'])
                root.setText(1, i['widget_name'])
                root.setText(2, i['name'].lstrip('$'))
                root.setText(3, i['value'])
                self.treeWidget_variable.addTopLevelItem(root)
            self.treeWidget_variable.sortByColumn(0, Qt.AscendingOrder)
            self.listWidget_result.addItems(self.config['result'])
        except Exception as e:
            print(e, 'Works_buttons_event', 'init_list')

    def button_yes_event(self):
        try:
            self.signal_add_task.emit(self.object_name)
            self.close()
        except Exception as e:
            print(e, 'Works_buttons_event', 'button_yes_event')

    def button_no_event(self):
        self.close()

