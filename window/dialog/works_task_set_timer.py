from window.ui.works_task_set_timer_dialog import Ui_works_task_set_timer_dialog

from PyQt5.Qt import *


class Works_task_set_timer_event(QWidget, Ui_works_task_set_timer_dialog):
    dialog_close = pyqtSignal()
    signal_set_timer = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, works_task_set_timer_dialog):
        super().setupUi(works_task_set_timer_dialog)
        self.setWindowIcon(QIcon('resource/image/urchin.png'))
        self.button_yes.clicked.connect(self.yes_event)
        self.button_no.clicked.connect(self.no_event)

    # def closeEvent(self, event):
    #     super().closeEvent(event)
    #     self.dialog_close.emit()

    def yes_event(self):
        # print(int(self.spinBox_hour.text()), int(self.spinBox_minute.text()), int(self.spinBox_second.text()))
        self.signal_set_timer.emit(int(self.spinBox_hour.text()), int(self.spinBox_minute.text()), int(self.spinBox_second.text()))
        # if self.lineEdit_command_template.text() != '':
        #     self.tool_add_command_template.emit(True, self.lineEdit_command_template.text(), self.lineEdit_command_introduction.text(), self.lineEdit_command_example.text())
        #     self.close()
        # else:
        #     QMessageBox.warning(self, "操作提示", '命令模板不可为空！', QMessageBox.Ok)

    def no_event(self):
        # self.close()
        self.dialog_close.emit()
