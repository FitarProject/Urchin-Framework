from window.ui.works_task_input_dialog import Ui_works_task_input_dialog
from window.dialog.works_task_set_timer import Works_task_set_timer_event

from PyQt5.Qt import *


class Works_task_input_event(QWidget, Ui_works_task_input_dialog):
    dialog_close = pyqtSignal()
    signal_add_task = pyqtSignal(dict)

    def __init__(self, input_variable, alive_task_list):
        super().__init__()
        self.task_input = {'set_timer': False, 'variable': [], 'task_name': ""}
        self.input_variable = input_variable
        self.alive_task_list = alive_task_list
        self.item_list = []
        self.index_list = []
        self.childwindow_flag_set_timer = False

        self.setupUi(self)

    def setupUi(self, works_task_input_dialog):
        try:
            super().setupUi(works_task_input_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.task_name.setFocus()
            for i in self.input_variable:
                if i['value'] == '手动输入':
                    root = QTreeWidgetItem(self.treeWidget)
                    root.setText(0, i['name'].lstrip('$'))
                    root.setText(1, i['position'])
                    root.setText(2, i['widget_name'])
                    # root.setText(3, i['value'])
                    root.setFlags(root.flags() | Qt.ItemIsEditable)
                    self.treeWidget.addTopLevelItem(root)
                    # 记录item列表
                    self.item_list.append(root)
                    # 记录输入变量的位置
                    self.index_list.append(self.input_variable.index(i))
            # self.treeWidget.sortByColumn(1, Qt.AscendingOrder)
            self.treeWidget.itemDoubleClicked.connect(self.setEditable)
            self.button_yes.clicked.connect(self.button_yes_event)
            self.button_no.clicked.connect(self.button_no_event)
            self.button_set_timer.clicked.connect(self.button_set_timer_event)
        except Exception as e:
            print(e, 'Works_task_input_event', 'setupUi')

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.dialog_close.emit()
        if self.childwindow_flag_set_timer:
            self.task_timer.close()

    def setEditable(self, item, column):
        try:
            if column == 3:
                self.treeWidget.editItem(item, 3)
        except Exception as e:
            print(e, 'Works_task_input_event', 'setEditable')

    def button_yes_event(self):
        try:
            flag = True
            if self.task_name.text().strip() == '':
                QMessageBox.warning(self, "操作提示", '任务名称不可为空！', QMessageBox.Ok)
            else:
                flag_name = True
                task_name = self.task_name.text()
                for alive_task_name in self.alive_task_list['task_list']:
                    if task_name == alive_task_name['name']:
                        flag_name = False
                        QMessageBox.warning(self, "操作提示", '任务名称已存在，请重新输入！', QMessageBox.Ok)
                        break
                if flag_name:
                    self.task_input['task_name'] = self.task_name.text()
                    for item in self.item_list:
                        if item.text(3).strip() == '':
                            flag = False
                        else:
                            self.input_variable[self.index_list[self.item_list.index(item)]]['value'] = item.text(3)
                            self.task_input['variable'].append(self.input_variable[self.index_list[self.item_list.index(item)]])
                    if flag:
                        self.signal_add_task.emit(self.task_input)
                        self.close()
                    else:
                        QMessageBox.warning(self, "操作提示", '请双击输入所有待填变量值！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Works_task_input_event', 'button_yes_event')

    def button_no_event(self):
        self.close()
        self.childwindow_flag_set_timer = False

    # 定时任务弹窗
    def button_set_timer_event(self):
        try:
            self.childwindow_flag_set_timer = True
            self.task_timer = QDialog(self)
            self.set_timer = Works_task_set_timer_event()
            self.set_timer.dialog_close.connect(self.set_timer_close_event)
            self.set_timer.signal_set_timer.connect(self.set_timer_event)
            self.set_timer.setParent(self.task_timer)
            self.task_timer.setModal(True)
            self.task_timer.setWindowModality(Qt.WindowModal)
            self.task_timer.show()
        except Exception as e:
            print(e, 'Works_task_input_event', 'button_set_timer_event')

    def set_timer_close_event(self):
        self.task_timer.close()

    def set_timer_event(self, hour, minute, second):
        if hour == 0 and minute == 0 and second == 0:
            self.task_input['set_timer'] = False
        else:
            self.task_input['set_timer'] = True
        self.task_input['time'] = hour * 360 + minute * 60 + second
        self.task_timer.close()
        self.childwindow_flag_set_timer = False
