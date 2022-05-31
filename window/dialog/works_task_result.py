from window.ui.works_task_result_dialog import Ui_works_task_result_dialog

from PyQt5.Qt import *
import os


class Works_task_result(QWidget, Ui_works_task_result_dialog):
    trigger_close = pyqtSignal()
    trigger_refresh = pyqtSignal(str)

    def __init__(self, task_name, task_status, cmd_log):
        super().__init__()
        self.task_time = ''
        self.tabs = {}
        self.log_browser = {}
        self.gridLayout_ = {}
        self.result_list = []
        self.task_name = task_name
        self.task_status = task_status
        self.cmd_log = cmd_log

        self.setupUi(self)

    def setupUi(self, works_task_result_dialog):
        try:
            super().setupUi(works_task_result_dialog)
            self.button_download_result.hide()
            self.button_collect_result.hide()
            # 填充任务详情
            task_time_tmp = self.task_status['dir'].lstrip(self.task_name + '_').split('_')
            self.task_time = task_time_tmp[0] + '/' + task_time_tmp[1] + '/' + task_time_tmp[2] + ' ' + task_time_tmp[3] + ':' + task_time_tmp[4] + ':' + task_time_tmp[5]
            self.log_browser_task_information.append('任务名称：    ' + self.task_name + '\n')
            self.log_browser_task_information.append('任务模式：    ' + self.task_status['mode'])
            self.log_browser_task_information.append('当前进度：    ' + self.task_status['schedule'])
            self.log_browser_task_information.append('执行时间：    ' + self.task_time)
            self.log_browser_task_information.append('日志路径：    ' + os.getcwd().replace('\\\\', '/') + '/logs/' + self.task_status['dir'] + '\n')
            # self.log_browser_task_information.append('输入参数：' + )
            # self.log_browser_task_information.append('结果列表：' + )
            # 填充命令行输出
            self.log_browser_task_cmd_out.setText(self.cmd_log)
            # 初始化结果列表
            self.result_list = os.listdir('./logs/' + self.task_status['dir'])
            if 'log_all' in self.result_list:
                self.result_list.remove('log_all')
            for result in self.result_list:
                self.tabs[result] = QWidget()
                self.tabs[result].setObjectName(result + "_tab")
                self.gridLayout_[result] = QGridLayout(self.tabs[result])
                self.gridLayout_[result].setContentsMargins(0, 0, 0, 0)
                self.log_browser[result] = QTextBrowser(self.tabs[result])
                self.log_browser[result].setGeometry(QRect(0, 0, 578, 147))
                self.log_browser[result].setFrameShape(QFrame.NoFrame)
                self.log_browser[result].setObjectName(result + "_log")
                self.gridLayout_[result].addWidget(self.log_browser[result], 0, 0, 1, 1)
                self.tabWidget.addTab(self.tabs[result], result)
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[result]), result.rstrip('.txt'))
                with open('logs/' + self.task_status['dir'] + '/' + result, 'r', encoding='utf-8') as f:
                    self.log_browser[result].setText(f.read())
            self.button_refresh.clicked.connect(self.button_refresh_event)
        except Exception as e:
            print(e, 'Works_task_result', 'setupUi')

    def button_refresh_event(self):
        self.trigger_refresh.emit(self.task_name)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.trigger_close.emit()

    def logs_repaint(self, task_status, cmd_log):
        try:
            self.task_status = task_status
            self.cmd_log = cmd_log
            # 销毁控件
            for result in self.result_list:
                self.tabWidget.removeTab(self.tabWidget.indexOf(self.tabs[result]))
                self.log_browser[result].deleteLater()
                self.gridLayout_[result].deleteLater()
                self.tabs[result].deleteLater()
            self.tabs = {}
            self.log_browser = {}
            self.gridLayout_ = {}
            self.log_browser_task_information.clear()
            self.log_browser_task_cmd_out.clear()
            # 重绘任务详情
            self.log_browser_task_information.append('任务名称：    ' + self.task_name + '\n')
            self.log_browser_task_information.append('任务模式：    ' + self.task_status['mode'])
            self.log_browser_task_information.append('当前进度：    ' + self.task_status['schedule'])
            self.log_browser_task_information.append('执行时间：    ' + self.task_time)
            self.log_browser_task_information.append('日志路径：    ' + os.getcwd().replace('\\', '/') + '/logs/' + self.task_status['dir'] + '\n')
            # self.log_browser_task_information.append('输入参数：' + )
            # self.log_browser_task_information.append('结果列表：' + )
            # 重绘命令行输出
            self.log_browser_task_cmd_out.setText(self.cmd_log)
            # 重绘结果
            self.result_list = os.listdir('./logs/' + self.task_status['dir'])
            if 'log_all' in self.result_list:
                self.result_list.remove('log_all')
            for result in self.result_list:
                self.tabs[result] = QWidget()
                self.tabs[result].setObjectName(result + "_tab")
                self.gridLayout_[result] = QGridLayout(self.tabs[result])
                self.gridLayout_[result].setContentsMargins(0, 0, 0, 0)
                self.log_browser[result] = QTextBrowser(self.tabs[result])
                self.log_browser[result].setGeometry(QRect(0, 0, 578, 147))
                self.log_browser[result].setFrameShape(QFrame.NoFrame)
                self.log_browser[result].setObjectName(result + "_log")
                self.gridLayout_[result].addWidget(self.log_browser[result], 0, 0, 1, 1)
                self.tabWidget.addTab(self.tabs[result], result)
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[result]), result)
                with open('logs/' + self.task_status['dir'] + '/' + result, 'r', encoding='utf-8') as f:
                    self.log_browser[result].setText(f.read())
        except Exception as e:
            print(e, 'Works_task_result', 'logs_repaint')




