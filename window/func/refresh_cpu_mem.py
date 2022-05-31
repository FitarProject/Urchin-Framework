import time
from PyQt5.QtCore import *

import psutil
import os


class CpuThread(QThread):
    trigger = pyqtSignal(float, float)

    def __init__(self, parent=None):
        super(CpuThread, self).__init__(parent)

    def run(self):
        while True:
            time.sleep(1)
            self.trigger.emit(psutil.cpu_percent(), psutil.virtual_memory().percent)
            # pid = os.getpid()
            # p = psutil.Process(pid)
            # cpu_percent = p.cpu_percent()
            # mem_percent = p.memory_percent()
            # print(cpu_percent, mem_percent)
            # self.trigger.emit(float(cpu_percent), float(mem_percent))


