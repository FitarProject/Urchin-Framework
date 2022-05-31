from multiprocessing import Process, Queue
import sys, time, subprocess, shlex, threading, psutil, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from test_ui import Ui_MainWindow


class ReadQueueThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, start_RealSignal, stop_RealSignal, queue):
        super().__init__()
        self.start_RealSignal = start_RealSignal
        self.stop_RealSignal = stop_RealSignal
        self.queue = queue

    def run(self):
        try:
            while True:
                if self.stop_RealSignal.is_set():
                    time.sleep(0.01)
                    while self.start_RealSignal.is_set():
                        time.sleep(0.0001)
                    else:
                        if self.stop_RealSignal.is_set():
                            # self.queue = self.number + 1
                            self.trigger.emit(self.queue.get())
                            # print('get ', self.queue.get())
                else:
                    return
            print(22)
        except Exception as e:
            print(e, 'ReadQueueThread', 'run')


class LogThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, parent=None):
        super(LogThread, self).__init__(parent)

    def run_(self, message):
        self.trigger.emit(message)


class ReadPipeThread(threading.Thread):
    def __init__(self, readline, callback, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self.readline = readline
        self.callback = callback

    def run(self):
        for line in iter(self.readline, ""):
            if len(line) == 0:
                break
            self.callback(line)


def fun_exec(queue_out, queue_err, command):
    try:
        cmd = shlex.split(command)

        process = subprocess.Popen(
            cmd,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        def log_warp(func):
            def _wrapper(line: str):
                return func(line.strip())

            return _wrapper

        def to_out(line):
            queue_out.put(line)
            print('put ', line)

        def to_err(line):
            queue_err.put(line)

        read_stdout = ReadPipeThread(process.stdout.readline, log_warp(to_out))
        read_stderr = ReadPipeThread(process.stderr.readline, log_warp(to_err))
        read_stdout.start()
        read_stderr.start()
        read_stdout.join()
        read_stderr.join()

        try:
            outs, errs = process.communicate(timeout=15)
            # print(outs, errs)
        except subprocess.CalledProcessError:
            process.kill()
            outs, errs = process.communicate()
            read_stdout.terminate()
            read_stderr.terminate()
            # print(outs, errs)
        process.wait()
    except Exception as e:
        print(e, 'fun_exec')


class ExecThread(threading.Thread):
    def __init__(self, parent, queue_out, queue_err, command, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self.parent_ = parent
        self.queue_out = queue_out
        self.queue_err = queue_err
        self.command = command
        self.pid = None

    def run(self):
        try:
            p = Process(target=fun_exec, args=(self.queue_out, self.queue_err, self.command,))
            p.start()
            self.pid = p.pid
            p.join()
            print(11)
        except Exception as e:
            print(e, 'ExecThread', 'run')

    def get_pid(self):
        return self.pid


# class ExecThread(QThread):
#     # trigger_out = pyqtSignal(str)
#     # trigger_err = pyqtSignal(str)
#
#     # trigger_pid = pyqtSignal(int)
#
#     def __init__(self, parent, queue_out, queue_err, command) -> None:
#         super(QThread, self).__init__(parent)
#         self.parent_ = parent
#         self.queue_out = queue_out
#         self.queue_err = queue_err
#         self.command = command
#         self.pid = None
#
#     def run(self):
#         try:
#             p = Process(target=fun_exec, args=(self.queue_out, self.queue_err, self.command,))
#             p.start()
#             self.pid = p.pid
#             p.join()
#             print(11)
#         except Exception as e:
#             print(e, 'ExecThread', 'run')
#
#     def get_pid(self):
#         return self.pid


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.start_RealSignal = threading.Event()  # 动态信号
        self.stop_RealSignal = threading.Event()  # 动态信号
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

        self.threads = LogThread(self)  # 自定义线程类
        self.threads.trigger.connect(self.update_text)  # 当信号接收到消息时，更新数据

        self.thread_no = 0  # 序号

    def to_out(self, line):
        self.thread_no += 1
        self.threads.run_(line)

    def to_err(self, line):
        self.thread_no += 1
        self.threads.run_(line)

    def refresh_pid(self, pid):
        print(pid)
        self.pause = psutil.Process(pid)

    def start(self):
        '''
        当点击start按键时日志栏中应显示start:序号
        '''
        # self.thread_no += 1
        # message = "start:{0}".format(self.thread_no)
        # self.threads.run_(message)  # start the thread
        queue_out = Queue()
        queue_err = Queue()
        command = 'ping 127.0.0.1'
        exec_cmd = ExecThread(self, queue_out, queue_err, command)
        exec_cmd.trigger_out.connect(self.to_out)
        exec_cmd.trigger_err.connect(self.to_err)
        # exec_cmd.trigger_pid.connect(self.refresh_pid)
        self.pause = psutil.Process(exec_cmd.get_pid())
        exec_cmd.start()

        self.Thread = ReadQueueThread(self.start_RealSignal, self.stop_RealSignal, queue_out)
        self.Thread.trigger.connect(self.label_trigger)
        self.stop_RealSignal.set()
        self.start_RealSignal.clear()
        self.Thread.start()
        self.Thread.exit()

    def stop(self):
        try:
            '''
            当点击stop按键时日志栏中应显示stop:序号
            '''
            # self.thread_no += 1
            # message = "stop:{0}".format(self.thread_no)
            # self.threads.run_(message)  # start the thread
            self.pause.suspend()
            self.pushButton_2.clicked.disconnect()
            self.pushButton_2.clicked.connect(self.restart)
        except Exception as e:
            print(e)

    def restart(self):
        self.pause.resume()
        self.pushButton_2.clicked.disconnect()
        self.pushButton_2.clicked.connect(self.stop)

    def update_text(self, message):
        '''
        添加信息到日志栏中(即控件QTextBrowser中)
        '''
        self.textBrowser.append(message)

    def thread_start_first(self):
        self.stop_RealSignal.set()
        self.start_RealSignal.clear()
        self.Thread.start()
        self.Thread.exit()
        # self.pushButton.clicked.disconnect()
        # self.pushButton.clicked.connect(self.start)

    def thread_start(self):
        self.start_RealSignal.clear()

    def thread_suspend(self):
        self.start_RealSignal.set()

    def thread_stop(self):
        # self.label.setText(str(0))
        # self.Thread.input_conf(0)
        self.stop_RealSignal.clear()
        # self.pushButton.clicked.disconnect()
        # self.pushButton.clicked.connect(self.start_first)

    def label_trigger(self, line):
        self.to_out(line)
        print('get ' + line)



if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        mainWindow = Main()
        mainWindow.show()

        sys.exit(app.exec_())
    except Exception as e:
        print(e)