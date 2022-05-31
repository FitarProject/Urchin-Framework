from window.ui.mine_func_detatil_dialog import Ui_mine_func_detatil_dialog

from PyQt5.Qt import *


class Mine_func_detatil_event(QWidget, Ui_mine_func_detatil_dialog):
    dialog_close = pyqtSignal()
    signal_add_task = pyqtSignal(str, str)
    signal_edit_func = pyqtSignal(str, dict, str)

    def __init__(self, object_name, config, func_type):
        super().__init__()
        self.object_name = object_name
        self.config = config
        self.func_type = func_type
        self.setupUi(self)
        self.init_list()

    def setupUi(self, mine_func_detatil_dialog):
        try:
            super().setupUi(mine_func_detatil_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.set_icon()
            self.button_yes.clicked.connect(self.button_yes_event)
            self.button_no.clicked.connect(self.button_no_event)
            self.button_edit.clicked.connect(self.button_edit_event)
        except Exception as e:
            print(e, 'Combine_func_event', 'setupUi')

    def closeEvent(self, event):
        super().closeEvent(event)
        self.dialog_close.emit()

    def set_icon(self):
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.button_edit.setIcon(self.icon_edit)

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
                # root.setFlags(root.flags() | Qt.ItemIsEditable)
                self.treeWidget_variable.addTopLevelItem(root)
            self.treeWidget_variable.sortByColumn(0, Qt.AscendingOrder)
            self.listWidget_result.addItems(self.config['result'])
        except Exception as e:
            print(e, 'Combine_func_event', 'init_list')

    def button_yes_event(self):
        try:
            self.signal_add_task.emit(self.object_name, self.func_type)
            self.close()
        except Exception as e:
            print(e, 'Combine_func_event', 'button_yes_event')

    def button_no_event(self):
        self.close()

    def button_edit_event(self):
        try:
            if self.lineEdit_name.isReadOnly():
                self.button_edit.setIcon(self.icon_save)
                self.lineEdit_name.setReadOnly(False)
                self.plainTextEdit_introduction.setReadOnly(False)
            else:
                if self.lineEdit_name.text() != '':
                    self.button_edit.setIcon(self.icon_edit)
                    self.lineEdit_name.setReadOnly(True)
                    self.plainTextEdit_introduction.setReadOnly(True)
                    self.config['name'] = self.lineEdit_name.text()
                    self.config['introduction'] = self.plainTextEdit_introduction.toPlainText()
                    self.signal_edit_func.emit(self.object_name, self.config, self.func_type)
                else:
                    QMessageBox.warning(self, "操作警告", '功能名称不可为空！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Combine_func_event', 'button_edit_event')
