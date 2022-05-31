from window.ui.combine_func_detatil_dialog import Ui_combine_func_detatil_dialog

from PyQt5.Qt import *
import json


class Combine_func_detatil_event(QWidget, Ui_combine_func_detatil_dialog):
    dialog_close = pyqtSignal()
    signal_add_task = pyqtSignal(dict)
    signal_add_func = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.config = None
        self.setupUi(self)
        self.read_config()
        self.init_list()

    def setupUi(self, combine_func_detatil_dialog):
        try:
            super().setupUi(combine_func_detatil_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.button_combine.clicked.connect(self.button_combine_event)
            self.button_test.clicked.connect(self.button_test_event)
        except Exception as e:
            print(e, 'Combine_func_event', 'setupUi')

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.dialog_close.emit()

    def read_config(self):
        with open('config/combine_variable.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def save_config(self):
        with open('config/combine_variable.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f)

    def init_list(self):
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

    def refresh_list(self):
        self.read_config()
        self.treeWidget_variable.clear()
        self.init_list()

    def button_combine_event(self):
        flag = True
        for i in range(len(self.config['variable'])):
            item = self.treeWidget_variable.topLevelItem(i)
            if item.text(3) == '':
                flag = False
        if self.lineEdit_name.text() == '':
            QMessageBox.warning(self, "操作提示", '请设置功能名称！', QMessageBox.Ok)
        elif not flag:
            QMessageBox.warning(self, "操作提示", '存在空变量值！', QMessageBox.Ok)
        else:
            self.config['name'] = self.lineEdit_name.text()
            self.config['introduction'] = self.plainTextEdit_introduction.toPlainText()
            self.save_config()
            self.signal_add_func.emit(self.config)
            self.close()

    def button_test_event(self):
        flag = True
        for i in range(len(self.config['variable'])):
            item = self.treeWidget_variable.topLevelItem(i)
            if item.text(3) == '':
                flag = False
        if self.lineEdit_name.text() == '':
            QMessageBox.warning(self, "操作提示", '请设置功能名称！', QMessageBox.Ok)
        elif not flag:
            QMessageBox.warning(self, "操作提示", '存在空变量值！', QMessageBox.Ok)
        else:
            self.config['name'] = self.lineEdit_name.text()
            self.config['introduction'] = self.plainTextEdit_introduction.toPlainText()
            self.save_config()
            self.signal_add_task.emit(self.config)
            self.close()
