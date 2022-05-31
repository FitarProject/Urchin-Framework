from window.ui.works_window import Ui_works_window
from window.paint.button_record import Button_list
from window.dialog.works_buttons import Works_buttons_event
from window.dialog.works_addbutton import Works_addbutton_event
from window.dialog.works_task_input import Works_task_input_event
from window.dialog.works_task_result import Works_task_result
from window.func.task_thread import TaskThread
# from window.func.task_thread_2 import TaskThread
from window.func.exec_command import LogThread
from window.func.refresh_cpu_mem import CpuThread

from PyQt5.Qt import *
# from multiprocessing import Process
# from string import Template
import json, psutil, time, os


class Works(QWidget, Ui_works_window):
    def __init__(self):
        super().__init__()
        self.childwindow_flag_task_input = False
        self.childwindow_flag_func_detatil = False
        self.childwindow_flag_task_result = False
        # 初始化按钮信息
        self.func_list = []
        self.page1_button = {}
        self.page2_button = {}
        self.page2_checkbox = {}
        self.dict_to_button = {}
        self.tabs = {}
        self.log_browser = {}
        self.tasks = {}
        self.task_status = {}
        self.workThread = CpuThread(self)

        # self.setupUi(self)

    def setupUi(self, works_window):
        super().setupUi(works_window)
        self.workThread.start()
        with open('qss/widget_label.qss', 'r', encoding='UTF-8') as f:
            my_qss = f.read()
            self.widget_2.setStyleSheet(my_qss)
        with open('qss/scroll_buttons.qss', 'r', encoding='UTF-8') as f:
            my_qss = f.read()
            self.scrollAreaWidgetContents_page1.setStyleSheet(my_qss)
            self.scrollAreaWidgetContents_page2.setStyleSheet(my_qss)
        with open('qss/tabs.qss', 'r', encoding='UTF-8') as f:
            self.tabWidget.setStyleSheet(f.read())
        with open('qss/tree_widget.qss', 'r', encoding='UTF-8') as f:
            my_qss = f.read()
            self.treeWidget.setStyleSheet(my_qss)
        self.button_list = Button_list(10, 10, 50, 50, 40, 40, 314, 3140)
        # 读取所有按钮信息并绘制
        self.read_config()
        self.task_init()
        self.buttons_paint()
        # 读取笔记
        with open('config/works_note.txt', 'r', encoding='utf-8') as f:
            self.note_text.setText(f.read())
        # 设置最初展示界面
        self.stackedWidget.setCurrentIndex(0)
        self.selectall_button.hide()
        self.delete_button.hide()
        # 设置右键菜单
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested[QPoint].connect(self.tree_right_menu)
        # 连接信号与槽函数
        self.workThread.trigger.connect(self.refresh_cpu_event)
        self.manage_button.clicked.connect(self.manage_button_event)
        self.selectall_button.clicked.connect(self.selectall_button_event)
        self.delete_button.clicked.connect(self.delete_button_event)

    # 窗口关闭，结束所有任务
    def close_tasks(self):
        try:
            flag = False
            for task_name in self.task_status.keys():
                if self.task_status[task_name]['status'] == '进行中' or self.task_status[task_name]['status'] == '暂停中':
                    flag = True
            if flag:
                if QMessageBox.warning(self, "操作确认", '有正在进行中的任务，是否终止？', QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
                    for task_name in self.task_status.keys():
                        if self.task_status[task_name]['status'] == '进行中' or self.task_status[task_name]['status'] == '暂停中':
                            self.task_status[task_name]['process'].process.terminate()
                            self.task_status[task_name]['process'].terminate()
                            self.task_status[task_name]['log_thread'].terminate()
                            self.task_status[task_name]['status'] = '异常终止'
                            print('异常终止：' + task_name)
                            self.save_task_log(task_name)
                            self.save_task_list()
                    return True
                else:
                    return False
            return True
        except Exception as e:
            print(e, 'Works', 'close_tasks')

    # 初始化任务列表
    def task_init(self):
        try:
            with open('config/works_task_list.json', 'r', encoding='utf-8') as f:
                self.task_list = json.load(f)
            disable_task_list = []
            for task_dict in self.task_list['task_list']:
                if os.path.exists('logs/' + task_dict['dir']):
                    # 任务列表添加根节点
                    task_name = task_dict['name']
                    self.tasks[task_name] = QTreeWidgetItem(self.treeWidget)
                    # self.tasks[task_name].setData(0, 0, task_name)
                    self.tasks[task_name].setText(0, task_name)
                    self.tasks[task_name].setText(1, task_dict['mode'])
                    self.tasks[task_name].setText(2, task_dict['schedule'])
                    self.tasks[task_name].setText(3, task_dict['status'])
                    self.treeWidget.addTopLevelItem(self.tasks[task_name])
                    # 添加日志页
                    self.tabs[task_name] = QWidget()
                    self.tabs[task_name].setObjectName(task_name + "_tab")
                    self.log_browser[task_name] = QTextBrowser(self.tabs[task_name])
                    self.log_browser[task_name].setGeometry(QRect(0, 0, 578, 147))
                    self.log_browser[task_name].setFrameShape(QFrame.NoFrame)
                    self.log_browser[task_name].setObjectName(task_name + "_log")
                    self.tabWidget.addTab(self.tabs[task_name], task_name)
                    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[task_name]), task_name)
                    self.tabWidget.setCurrentWidget(self.tabs[task_name])
                    # 添加任务状态
                    self.task_status[task_name] = task_dict
                    # 填充日志
                    with open('logs/' + task_dict['dir'] + '/log_all', 'r', encoding='utf-8') as f:
                        self.log_browser[task_name].setPlainText(f.read())
                else:
                    disable_task_list.append(task_dict)
            for task_dict in disable_task_list:
                self.task_list['task_list'].remove(task_dict)
            with open('config/works_task_list.json', 'w', encoding='utf-8') as f:
                json.dump(self.task_list, f)
        except Exception as e:
            print(e, 'Works', 'task_init')

    # 保存已完成任务列表
    def save_task_list(self):
        try:
            with open('config/works_task_list.json', 'w', encoding='utf-8') as f:
                json.dump(self.task_list, f)
        except Exception as e:
            print(e, 'Works', 'save_task_list')

    # 保存任务日志并添加至任务列表
    def save_task_log(self, task_name):
        with open('logs/' + self.task_status[task_name]['dir'] + '/log_all', 'w', encoding='utf-8') as f:
            f.write(self.log_browser[task_name].toPlainText())
        self.task_status[task_name]['process'].terminate()
        del self.task_status[task_name]['process']
        self.task_status[task_name]['log_thread'].terminate()
        del self.task_status[task_name]['log_thread']
        self.task_status[task_name]['name'] = task_name
        self.task_list['task_list'].append(self.task_status[task_name])

    # 绘制按钮
    def buttons_paint(self):
        for button_object_name in self.func_list:
            button_config = self.dict_to_button[button_object_name]
            # 绘制第一页的按钮
            try:
                x, y, width, height = self.button_list.add_button(button_object_name)
                self.page1_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_page1)
                self.page1_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page1_button[button_object_name].setObjectName(button_object_name)
                self.page1_button[button_object_name].setText(button_config['name'])
                self.page1_button[button_object_name].setToolTip('功能名称：' + button_config['name'] + '\n功能介绍：' + button_config['introduction'])
                self.page1_button[button_object_name].setVisible(True)
                self.page1_button[button_object_name].clicked.connect(self.buttons_clicked_event)
            except Exception as e:
                print(e, 'Works', 'buttons_page1')
            # 绘制第二页的按钮
            try:
                self.page2_button[button_object_name] = QPushButton(self.scrollAreaWidgetContents_page2)
                self.page2_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page2_button[button_object_name].setObjectName(button_object_name)
                self.page2_button[button_object_name].setText(button_config['name'])
                self.page2_button[button_object_name].setToolTip('功能名称：' + button_config['name'] + '\n功能介绍：' + button_config['introduction'])
                self.page2_button[button_object_name].setVisible(True)
                self.page2_button[button_object_name].clicked.connect(self.buttons_selected_event)
                self.page2_checkbox[button_object_name] = QCheckBox(self.scrollAreaWidgetContents_page2)
                self.page2_checkbox[button_object_name].setGeometry(QRect(x+26, y+1, width-27, height-27))
                self.page2_checkbox[button_object_name].setObjectName(button_config['name'] + '_checkbox')
                self.page2_checkbox[button_object_name].raise_()
                self.page2_checkbox[button_object_name].setVisible(True)
            except Exception as e:
                print(e, 'Works', 'buttons_page2')
        # 绘制添加按钮
        try:
            x, y, width, height = self.button_list.add_button('button_add')
            self.page1_button['button_add'] = QPushButton(self.scrollAreaWidgetContents_page1)
            self.page1_button['button_add'].setGeometry(QRect(x, y, width, height))
            self.page1_button['button_add'].setObjectName('button_add')
            self.page1_button['button_add'].setText('添加')
            self.page1_button['button_add'].setToolTip('添加功能')
            self.page1_button['button_add'].setVisible(True)
            self.page1_button['button_add'].clicked.connect(self.buttons_add_event)
        except Exception as e:
            print(e, 'Works', 'buttons_add')

    def buttons_repaint(self):
        try:
            self.save_config()
            width, height = self.button_list.width, self.button_list.height
            for button_object_name in self.func_list:
                x, y = self.button_list.get_button_position(button_object_name)
                self.page1_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page2_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page2_checkbox[button_object_name].setGeometry(QRect(x + 26, y + 1, width - 27, height - 27))
            x, y = self.button_list.get_button_position('button_add')
            self.page1_button['button_add'].setGeometry(QRect(x, y, width, height))
            self.update()
        except Exception as e:
            print(e, 'Works', 'buttons_repaint')

    def read_config(self):
        with open('config/works_buttons.json', 'r', encoding='utf-8') as f:
            func_dict = json.load(f)
            self.func_list = func_dict['func_list']
        with open('config/mine_func_custom.json', 'r', encoding='utf-8') as f:
            self.dict_to_button = json.load(f)

    def save_config(self):
        try:
            func_dict = {"func_list": self.func_list}
            with open('config/works_buttons.json', 'w') as f:
                json.dump(func_dict, f)
        except Exception as e:
            print(e, 'Works', 'save_config')

    # 显示cpu
    def refresh_cpu_event(self, cpu, mem):
        # print(os.cpu_count())
        # print(psutil.cpu_percent())
        # print(psutil.virtual_memory())
        # print(cpu, mem, type(mem))
        self.progressBar_cpu.setValue(int(cpu))
        self.progressBar_mem.setValue(int(mem))

    def add_task_event(self, func_detatil: dict, test=False):
        try:
            self.mode = '自动'
            if test:
                self.mode = '测试'
            else:
                for variable in func_detatil['variable']:
                    if variable['value'] == '交互输入':
                        self.mode = '交互'
                        break
            self.func_detatil = func_detatil
            self.childwindow_flag_task_input = True
            # print(func_detatil['variable'])
            self.task_input = Works_task_input_event(func_detatil['variable'], self.task_list)
            self.task_input.dialog_close.connect(self.task_input_close_event)
            self.task_input.signal_add_task.connect(self.task_input_event)
            self.task_input.show()
        except Exception as e:
            print(e, 'Works', 'add_task_event')

    def task_input_close_event(self):
        self.childwindow_flag_task_input = False

    # 输入必要参数后开始任务执行
    def task_input_event(self, task_input_dict):
        try:
            # self.task_input = task_input
            # self.func_detatil['variable'] = task_input['variable']
            self.func_exec(task_input_dict)
            self.add_tab(task_input_dict['task_name'])
        except Exception as e:
            print(e, 'Works', 'task_input_event')

    # 任务执行函数
    def func_exec(self, task_input_dict):
        try:
            task_name = task_input_dict['task_name']
            self.task_status[task_name] = {
                            "process": None,
                            "status": "",
                            "schedule": "",
                            "mode": "",
                            "remain_time": 0,
                        }
            try:
                self.task_status[task_name]['log_thread'] = LogThread(self)
                self.task_status[task_name]['process'] = TaskThread(self, task_input_dict, self.func_detatil, self.task_status[task_name]['log_thread'])
                self.task_status[task_name]['process'].trigger_log.connect(self.print_logs)
                self.task_status[task_name]['process'].trigger_status.connect(self.status_change_event)
                self.task_status[task_name]['process'].trigger_section.connect(self.status_section_event)
                self.task_status[task_name]['process'].trigger_timer.connect(self.timer_event)
                self.task_status[task_name]['process'].start()
                # pid = self.task_status[task_name]['process'].pid
                # self.pause = psutil.Process(pid)
                # 初始化任务状态
                self.task_status[task_name]['mode'] = self.mode
                self.task_status[task_name]['dir'] = self.task_status[task_name]['process'].task_dir
                if task_input_dict['set_timer']:
                    self.task_status[task_name]['schedule'] = '0' + '/' + str(len(self.func_detatil['config']))
                    self.task_status[task_name]['status'] = '定时任务'
                else:
                    self.task_status[task_name]['schedule'] = '1' + '/' + str(len(self.func_detatil['config']))
                    self.task_status[task_name]['status'] = '进行中'
            except Exception as e:
                print(e)
            self.add_tree_root(task_input_dict)
        except Exception as e:
            print(e, 'Works', 'func_exec')

    # 任务列表添加根节点
    def add_tree_root(self, task_input_dict):
        try:
            task_name = task_input_dict['task_name']
            self.tasks[task_name] = QTreeWidgetItem(self.treeWidget)
            # ???
            self.tasks[task_name].setData(0, 0, self.task_status[task_name]['process'])
            self.tasks[task_name].setText(0, task_name)
            self.tasks[task_name].setText(1, self.task_status[task_name]['mode'])
            self.tasks[task_name].setText(2, self.task_status[task_name]['schedule'])
            self.tasks[task_name].setText(3, self.task_status[task_name]['status'])
            self.treeWidget.addTopLevelItem(self.tasks[task_name])
        except Exception as e:
            print(e, 'Works', 'add_tree_root')

    # 添加任务日志窗口
    def add_tab(self, task_object):
        try:
            self.tabs[task_object] = QWidget()
            self.tabs[task_object].setObjectName(task_object + "_tab")
            self.log_browser[task_object] = QTextBrowser(self.tabs[task_object])
            self.log_browser[task_object].setGeometry(QRect(0, 0, 578, 147))
            self.log_browser[task_object].setFrameShape(QFrame.NoFrame)
            self.log_browser[task_object].setObjectName(task_object + "_log")
            self.tabWidget.addTab(self.tabs[task_object], task_object)
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs[task_object]), task_object)
            self.tabWidget.setCurrentWidget(self.tabs[task_object])
        except Exception as e:
            print(e, 'Works', 'add_tab')

    # 自定义槽函数
    # 管理常用功能按钮
    def manage_button_event(self):
        try:
            if self.stackedWidget.currentIndex():
                self.stackedWidget.setCurrentIndex(0)
                self.selectall_button.hide()
                self.delete_button.hide()
                self.manage_button.setText('管理')
            else:
                self.stackedWidget.setCurrentIndex(1)
                self.selectall_button.show()
                self.delete_button.show()
                self.manage_button.setText('返回')
                self.selectall_button.setText('全选')
                for name in self.button_list.get_button_list()[:-1]:
                    self.page2_checkbox[name].setChecked(False)
        except Exception as e:
            print(e, 'Works', 'add_tab')

    # 全选常用功能
    def selectall_button_event(self):
        try:
            if self.selectall_button.text() == '全选':
                self.selectall_button.setText('取消')
                for name in self.button_list.get_button_list()[:-1]:
                    self.page2_checkbox[name].setChecked(True)
            else:
                self.selectall_button.setText('全选')
                for name in self.button_list.get_button_list()[:-1]:
                    self.page2_checkbox[name].setChecked(False)
        except Exception as e:
            print(e, 'Works', 'selectall_button_event')

    # 删除常用功能
    def delete_button_event(self):
        count = 0
        name_list = self.button_list.get_button_list()[:-1]
        for name in name_list:
            if self.page2_checkbox[name].isChecked():
                count += 1
        try:
            if count != 0:
                if QMessageBox.warning(self, "操作确认", '是否删除这%s个功能？' % count, QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                    for name in name_list:
                        if self.page2_checkbox[name].isChecked():
                            self.button_list.remove_button(name)
                            self.func_list.pop(self.func_list.index(name))
                            self.page1_button[name].deleteLater()
                            self.page2_button[name].deleteLater()
                            self.page2_checkbox[name].deleteLater()
                    try:
                        self.buttons_repaint()
                    except Exception as e:
                        print(e, 'Works')
        except Exception as e:
            print(e, 'Works', 'delete_button_event')

    # 查看常用功能详情
    def buttons_clicked_event(self):
        object_name = self.sender().objectName()
        if self.childwindow_flag_func_detatil:
            self.works_button.close()
        self.childwindow_flag_func_detatil = True
        self.works_button = Works_buttons_event(object_name, self.dict_to_button[object_name])
        self.works_button.dialog_close.connect(self.func_detatil_close_event)
        self.works_button.signal_add_task.connect(self.func_detatil_add_task_event)
        self.works_button.show()

    # 从功能库中选择功能
    def buttons_add_event(self):
        self.works_addbutton = Works_addbutton_event()
        self.works_addbutton.trigger_add_func.connect(self.add_func)
        self.works_addbutton.show()

    # 外部添加常用功能
    def add_func(self, object_name):
        try:
            if object_name not in self.func_list:
                self.func_list.append(object_name)
                self.button_list.remove_button('button_add')
                button_config = self.dict_to_button[object_name]
                x, y, width, height = self.button_list.add_button(object_name)
                self.page1_button[object_name] = QPushButton(self.scrollAreaWidgetContents_page1)
                self.page1_button[object_name].setGeometry(QRect(x, y, width, height))
                self.page1_button[object_name].setObjectName(object_name)
                self.page1_button[object_name].setText(button_config['name'])
                self.page1_button[object_name].setToolTip('功能名称：' + button_config['name'] + '\n功能介绍：' + button_config['introduction'])
                self.page1_button[object_name].setVisible(True)
                self.page1_button[object_name].clicked.connect(self.buttons_clicked_event)
                self.page2_button[object_name] = QPushButton(self.scrollAreaWidgetContents_page2)
                self.page2_button[object_name].setGeometry(QRect(x, y, width, height))
                self.page2_button[object_name].setObjectName(object_name)
                self.page2_button[object_name].setText(button_config['name'])
                self.page2_button[object_name].setToolTip('功能名称：' + button_config['name'] + '\n功能介绍：' + button_config['introduction'])
                self.page2_button[object_name].setVisible(True)
                self.page2_button[object_name].clicked.connect(self.buttons_selected_event)
                self.page2_checkbox[object_name] = QCheckBox(self.scrollAreaWidgetContents_page2)
                self.page2_checkbox[object_name].setGeometry(QRect(x + 26, y + 1, width - 27, height - 27))
                self.page2_checkbox[object_name].setObjectName(button_config['name'] + '_checkbox')
                self.page2_checkbox[object_name].raise_()
                self.page2_checkbox[object_name].setVisible(True)
                # 重设添加按钮的位置
                x, y, width, height = self.button_list.add_button('button_add')
                self.page1_button['button_add'].setGeometry(QRect(x, y, width, height))
                self.save_config()
            else:
                QMessageBox.warning(self, "操作提示", '该功能已经是常用功能！', QMessageBox.Ok)
        except Exception as e:
            print(e, 'Works', 'add_func')

    # 外部删除常用功能
    def delete_func(self, object_name):
        try:
            if object_name in self.func_list:
                self.button_list.remove_button(object_name)
                self.func_list.pop(self.func_list.index(object_name))
                self.page1_button[object_name].deleteLater()
                self.page2_button[object_name].deleteLater()
                self.page2_checkbox[object_name].deleteLater()
                self.buttons_repaint()
        except Exception as e:
            print(e, 'Works', 'delete_func')

    # 管理界面多选按钮
    def buttons_selected_event(self):
        try:
            if self.page2_checkbox[self.sender().objectName()].isChecked():
                self.page2_checkbox[self.sender().objectName()].setChecked(False)
            elif not self.page2_checkbox[self.sender().objectName()].isChecked():
                self.page2_checkbox[self.sender().objectName()].setChecked(True)
            else:
                print('按钮选中状态错误')
        except Exception as e:
            print(e, 'Works', 'buttons_selected_event')

    # 常用功能执行
    def func_detatil_add_task_event(self, object_name):
        self.add_task_event(self.dict_to_button[object_name])

    # 子窗口关闭
    def func_detatil_close_event(self):
        self.childwindow_flag_func_detatil = False

    # 任务列表右键菜单
    def tree_right_menu(self, point):
        try:
            self.curr_item = self.treeWidget.itemAt(point)
            if self.curr_item:
                task_name = self.curr_item.text(0)
                popMenu = QMenu()
                if self.task_status[task_name]['status'] == '定时任务':
                    startAct = QAction(u'开始', self)
                    popMenu.addAction(startAct)
                    startAct.triggered.connect(self.start_task_event)
                elif self.task_status[task_name]['status'] == '进行中':
                    pauseAct = QAction(u'暂停', self)
                    popMenu.addAction(pauseAct)
                    pauseAct.triggered.connect(self.pause_task_event)
                    stopAct = QAction(u'终止', self)
                    popMenu.addAction(stopAct)
                    stopAct.triggered.connect(self.stop_task_event)
                    checkAct = QAction(u'查看结果', self)
                    popMenu.addAction(checkAct)
                    checkAct.triggered.connect(self.check_task_event)
                elif self.task_status[task_name]['status'] == '暂停中':
                    continueAct = QAction(u'继续', self)
                    popMenu.addAction(continueAct)
                    continueAct.triggered.connect(self.continue_task_event)
                    stopAct = QAction(u'终止', self)
                    popMenu.addAction(stopAct)
                    stopAct.triggered.connect(self.stop_task_event)
                    checkAct = QAction(u'查看结果', self)
                    popMenu.addAction(checkAct)
                    checkAct.triggered.connect(self.check_task_event)
                elif self.task_status[task_name]['status'] == '已终止':
                    deleteAct = QAction(u'删除', self)
                    popMenu.addAction(deleteAct)
                    deleteAct.triggered.connect(self.delete_task_event)
                    checkAct = QAction(u'查看结果', self)
                    popMenu.addAction(checkAct)
                    checkAct.triggered.connect(self.check_task_event)
                elif self.task_status[task_name]['status'] == '已完成' or self.task_status[task_name]['status'] == '异常终止':
                    deleteAct = QAction(u'删除', self)
                    popMenu.addAction(deleteAct)
                    deleteAct.triggered.connect(self.delete_task_event)
                    checkAct = QAction(u'查看结果', self)
                    popMenu.addAction(checkAct)
                    checkAct.triggered.connect(self.check_task_event)
                elif self.task_status[task_name]['status'] == '等待交互':
                    inputAct = QAction(u'交互', self)
                    popMenu.addAction(inputAct)
                    inputAct.triggered.connect(self.input_task_event)
                    stopAct = QAction(u'终止', self)
                    popMenu.addAction(stopAct)
                    stopAct.triggered.connect(self.stop_task_event)
                    checkAct = QAction(u'查看结果', self)
                    popMenu.addAction(checkAct)
                    checkAct.triggered.connect(self.check_task_event)
                popMenu.exec_(QCursor.pos())
        except Exception as e:
            print(e, 'Works', 'tree_right_menu')

    # 右键菜单按钮槽函数
    # 开始任务
    def start_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            self.task_status[task_name]['process'].stop_timer()
        except Exception as e:
            print(e, 'Works', 'start_task_event')

    # 暂停任务
    def pause_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            task_pid = self.task_status[task_name]['process'].pid
            self.task_status[task_name]['process'].task_suspend()
            # pause = psutil.Process(task_pid)
            # print(task_pid, pause)
            # pause.suspend()
            # print(task_pid, pause)
            pass
        except Exception as e:
            print(e, 'Works', 'pause_task_event')

    # 继续任务
    def continue_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            task_pid = self.task_status[task_name]['process'].pid
            self.task_status[task_name]['process'].task_continue()
            # pause = psutil.Process(task_pid)
            # print(task_pid, pause)
            # pause.resume()
            pass
        except Exception as e:
            print(e, 'Works', 'continue_task_event')

    # 终止任务
    def stop_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            self.task_status[task_name]['process'].terminate()
            self.task_status[task_name]['log_thread'].terminate()
            self.task_status[task_name]['status'] = '已终止'
            self.tasks[task_name].setText(3, '已终止')
            self.save_task_log(task_name)
            self.save_task_list()
        except Exception as e:
            print(e, 'Works', 'stop_task_event')

    # 删除任务
    def delete_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            self.tabWidget.removeTab(self.tabWidget.indexOf(self.tabs[task_name]))
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(self.tasks[task_name]))
            del self.task_status[task_name]
            for i in self.task_list['task_list']:
                if i['name'] == task_name:
                    self.task_list['task_list'].remove(i)
                    break
            self.save_task_list()
        except Exception as e:
            print(e, 'Works', 'delete_task_event')

    # 查看结果
    def check_task_event(self):
        try:
            if self.childwindow_flag_task_result:
                self.task_result.close()
            self.childwindow_flag_task_result = True
            task_name = self.curr_item.data(0, 0)
            self.task_result = Works_task_result(task_name, self.task_status[task_name], self.log_browser[task_name].toPlainText())
            self.task_result.trigger_refresh.connect(self.task_result_refresh_event)
            self.task_result.trigger_close.connect(self.task_result_close_event)
            self.task_result.show()
        except Exception as e:
            print(e, 'Works', 'check_task_event')

    # 任务结果界面关闭事件
    def task_result_close_event(self):
        self.childwindow_flag_task_result = False

    # 任务结果界面刷新事件
    def task_result_refresh_event(self, task_name):
        self.task_result.logs_repaint(self.task_status[task_name], self.log_browser[task_name].toPlainText())

    # 分析结果并输入变量
    def input_task_event(self):
        try:
            task_name = self.curr_item.data(0, 0)
            pass
        except Exception as e:
            print(e, 'Works', 'input_task_event')

    # 打印日志
    def print_logs(self, task_name, message):
        try:
            self.log_browser[task_name].append(message)
        except Exception as e:
            print(e, 'Works', 'print_logs')

    # 任务状态变更
    def status_change_event(self, task_name, new_status):
        try:
            self.task_status[task_name]['status'] = new_status
            self.tasks[task_name].setText(3, new_status)
            if new_status == '已完成' or new_status == '异常终止' or new_status == '已终止':
                self.save_task_log(task_name)
                self.save_task_list()
        except Exception as e:
            print(e, 'Works', 'status_change_event')

    # 任务阶段变更
    def status_section_event(self, task_name, new_section):
        try:
            self.task_status[task_name]['schedule'] = new_section
            self.tasks[task_name].setText(2, new_section)
        except Exception as e:
            print(e, 'Works', 'status_section_event')

    # 剩余倒计时时间
    def timer_event(self, task_name, remain_time):
        try:
            self.task_status[task_name]['remain_time'] = remain_time
        except Exception as e:
            print(e, 'Works', 'timer_event')

