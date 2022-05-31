from window.ui.combine_openvariable_dialog import Ui_combine_openvariable_dialog

from PyQt5.Qt import *
import re, json


class Combine_openvariable_event(QWidget, Ui_combine_openvariable_dialog):
    dialog_close = pyqtSignal()
    signal_variable_change = pyqtSignal(list)
    signal_result_change = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.listmodel_variable = QStringListModel()
        self.listmodel_result = QStringListModel()
        self.oldname_record = ''
        self.variable = []
        self.result_variable = []
        self.variable_num = 1
        self.result_variable_num = 1

        self.setupUi(self)
        self.init_list()

    def setupUi(self, combine_openvariable_dialog):
        super().setupUi(combine_openvariable_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        # 设置右键菜单
        # self.listWidget_variable.customContextMenuRequested[QPoint].connect(self.variable_right_menu)
        # self.listWidget_result.customContextMenuRequested[QPoint].connect(self.result_right_menu)
        self.add_variable.hide()
        self.add_result.hide()
        # 连接信号与槽函数
        # self.add_variable.clicked.connect(self.add_variable_event)
        # self.add_result.clicked.connect(self.add_result_event)
        # self.listWidget_variable.clicked.connect(self.onClickedListView)
        # self.listWidget_result.clicked.connect(self.onClickedListView)
        #
        # self.listWidget_variable.itemChanged.connect(self.match_str)
        # self.listWidget_result.itemChanged.connect(self.match_str)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.dialog_close.emit()

    def init_list(self):
        with open('config/combine_variable.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        for i in config['variable']:
            if i['value'] == '手动输入' or i['value'] == '交互输入':
                new_item = QListWidgetItem(self.listWidget_variable)
                if i['name'][0] != '$':
                    new_item.setText('$' + i['name'] + ' (' + i['position'] + ' ' + i['widget_name'] + ')')
                else:
                    new_item.setText(i['name'] + '(' + i['position'] + ' ' + i['widget_name'] + ')')
                # self.listWidget_variable.addItem(i['name'])
        for i in config['result']:
            new_item = QListWidgetItem(self.listWidget_result)
            new_item.setText(i)
            # self.listWidget_result.addItem(i)

    def refresh_list(self):
        self.listWidget_variable.clear()
        self.listWidget_result.clear()
        self.init_list()

    def return_variable(self):
        self.signal_variable_change.emit(self.refresh_variable)

    def return_result(self):
        self.signal_result_change.emit(self.refresh_result)

    def refresh_variable(self):
        self.variable = []
        count = self.listWidget_variable.count()
        for i in range(count):
            self.variable.append(self.listWidget_variable.item(i).text())
        return self.variable

    def refresh_result(self):
        self.result_variable = []
        count = self.listWidget_result.count()
        for i in range(count):
            self.result_variable.append(self.listWidget_result.item(i).text())
        return self.result_variable

    # 自定义槽函数
    def add_variable_event(self):
        self.variable_num += 1
        variable_str = 'variable_' + str(self.variable_num)
        self.listWidget_variable.addItem(variable_str)
        self.return_variable()

    def add_result_event(self):
        self.result_variable_num += 1
        result_variable_str = 'result_' + str(self.result_variable_num)
        self.listWidget_result.addItem(result_variable_str)
        self.return_result()

    def edit_variable_event(self):
        item = self.listWidget_variable.item(self.listWidget_variable.currentRow())
        self.oldname_record = item.text()[:20]
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.listWidget_variable.editItem(item)

    def edit_result_event(self):
        item = self.listWidget_result.item(self.listWidget_result.currentRow())
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.listWidget_result.editItem(item)

    def insert_variable_event(self):
        self.variable_num += 1
        variable_str = 'variable_' + str(self.variable_num)
        self.listWidget_variable.insertItem(self.listWidget_variable.currentIndex().row() + 1, variable_str)
        self.return_variable()

    def insert_result_event(self):
        self.variable_num += 1
        result_variable_str = 'result_' + str(self.variable_num)
        self.listWidget_result.insertItem(self.listWidget_result.currentIndex().row() + 1, result_variable_str)
        self.return_result()

    def delete_variable_event(self):
        self.listWidget_variable.takeItem(self.listWidget_variable.currentIndex().row())
        self.return_variable()

    def delete_result_event(self, index):
        self.listWidget_result.takeItem(self.listWidget_result.currentIndex().row())
        self.return_result()

    def onClickedListView(self, item):
        # print(item.row())
        pass

    def match_str(self, new_item):
        try:
            new = new_item.text()[:20]
            if self.oldname_record != new:
                temp = ''
                for i in new:
                    temp_str = re.findall(r"^[a-zA-Z1-9_]{1,15}$", i)
                    if len(temp_str):
                        temp += temp_str[0]
                if len(temp) != 0:
                    new_item.setText(temp)
                else:
                    new_item.setText(self.oldname_record)
                if new_item.listWidget() == self.listWidget_variable:
                    self.return_variable()
                elif new_item.listWidget() == self.listWidget_result:
                    self.return_result()
        except Exception as e:
            print(e, 'match_str', 'Combine_openvariable_event')

    def variable_right_menu(self, point):
        try:
            popMenu = QMenu()
            editAct = QAction(u'编辑', self)
            insertAct = QAction(u'插入', self)
            delAct = QAction(u'删除', self)
            popMenu.addAction(editAct)
            popMenu.addAction(insertAct)
            popMenu.addAction(delAct)
            editAct.triggered.connect(self.edit_variable_event)
            insertAct.triggered.connect(self.insert_variable_event)
            delAct.triggered.connect(self.delete_variable_event)
            popMenu.exec_(QCursor.pos())
        except Exception as e:
            print(e, 'variable_right_menu', 'Combine_openvariable_event')

    def result_right_menu(self, point):
        try:
            popMenu = QMenu()
            editAct = QAction(u'编辑', self)
            insertAct = QAction(u'插入', self)
            delAct = QAction(u'删除', self)
            popMenu.addAction(editAct)
            popMenu.addAction(insertAct)
            popMenu.addAction(delAct)
            editAct.triggered.connect(self.edit_result_event)
            insertAct.triggered.connect(self.insert_result_event)
            delAct.triggered.connect(self.delete_result_event)
            popMenu.exec_(QCursor.pos())
        except Exception as e:
            print(e, 'result_right_menu', 'Combine_openvariable_event')