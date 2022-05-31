import sys
import random
import numpy as np
from time import sleep
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import psutil
import os


class CpuThread(QThread):
    trigger = pyqtSignal(float, float)

    def __init__(self, parent=None):
        super(CpuThread, self).__init__(parent)

    def run_(self):
        # data = psutil.virtual_memory()
        # self.trigger.emit(int(psutil.cpu_percent(interval=1)), int(round(data.percent)))
        pid = os.getpid()
        p = psutil.Process(pid)
        cpu_percent = p.cpu_percent()
        mem_percent = p.memory_percent()
        print(cpu_percent, mem_percent)
        self.trigger.emit(float(cpu_percent), float(mem_percent))

    # def update(self):
    #     # print(3)
    #     # pid = os.getpid()
    #     # p = psutil.Process(pid)
    #     # self.cpu_percent = p.cpu_percent()
    #     # self.mem_percent = p.memory_percent()
    #     # self.trigger.emit(self.cpu_percent, self.mem_percent)
    #     # print("cpu:{:.2f}%,mem:{:.2f}%".format(self.cpu_percent, self.mem_percent))
    #     data = psutil.virtual_memory()
    #     # total = data.total  # 总内存,单位为byte
    #     # free = data.available  # 可以内存
    #     # memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + " "
    #     # cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
    #     print(psutil.cpu_percent(interval=1), round(data.percent))


class plotwindows(QtWidgets.QWidget):
    def __init__(self):
        super(plotwindows, self).__init__()
        layout = QFormLayout()
        self.edita3 = QLineEdit()
        self.edita4 = QLineEdit()
        self.edita5 = QLineEdit()
        layout.addRow("CPU", self.edita3)
        layout.addRow("MEM", self.edita4)
        layout.addRow("C数值", self.edita5)
        self.setLayout(layout)
        # self.getMemCpu()
        self.workThread = CpuThread()
        self.workThread.trigger.connect(self.mydata)
        self.Mytimer()

    def getMemCpu(self):
        data = psutil.virtual_memory()
        total = data.total  # 总内存,单位为byte
        free = data.available  # 可以内存
        memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + " "
        cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"
        print(memory, cpu)
        # return memory + cpu

    def mydata(self, cpu, mem):
        self.edita3.setText(str(cpu)[:4])
        self.edita4.setText(str(mem)[:4])
        # print(aaa, bbb)

    def Mytimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def update(self):
        self.workThread.run_()
        # self.edita3.setText(str(T_value))
        # self.edita4.setText(str(P_value))
        # global SUM_value
        # SUM_value = T_value + P_value
        # self.edita5.setText(str(SUM_value))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    new = plotwindows()
    new.show()
    sys.exit(app.exec_())
