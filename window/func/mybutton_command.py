from PyQt5.Qt import *


class Mybutton_command(QPushButton):
    double_clicked = pyqtSignal(str)

    def mouseDoubleClickEvent(self, QShowEvent):
        self.double_clicked.emit(self.objectName())
