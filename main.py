from PyQt5.Qt import *
import sys, os, io

from window.ui.main_window import Ui_main_widget
from window.works import Works
from window.tools import Tools
from window.combine import Combine
from window.community import Community
from window.mine import Mine
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")



class Window(QWidget, Ui_main_widget):
    def __init__(self):
        super().__init__()
        # 创建子窗口对象
        self.works_window = Works()
        self.tools_window = Tools()
        self.combine_window = Combine()
        self.community_window = Community()
        self.mine_window = Mine()

        self.setupUi(self)
        self.func_list()

    def setupUi(self, main_widget):
        super().setupUi(main_widget)
        # font = QFont()
        # font.setPointSize(18)
        # self.main_window_button_works.setFont(font)

        self.button_fold.setText('已折叠')
        self.button_fold.clicked.connect(self.button_fold_event)

        self.tools_window.refresh_selected_tool.connect(self.refresh_selected_tool_event)
        self.tools_window.refresh_selected_tunnel.connect(self.refresh_selected_tunnel_event)
        self.tools_window.del_selected_tool.connect(self.del_selected_tool_event)
        self.combine_window.signal_add_func.connect(self.add_func_event)
        self.combine_window.signal_add_task.connect(self.add_test_task_event)
        self.mine_window.signal_add_task.connect(self.add_task_event)
        self.mine_window.signal_refresh_combine.connect(self.refresh_combine_event)
        self.mine_window.signal_add_collect.connect(self.add_collect_event)
        self.mine_window.signal_del_collect.connect(self.del_collect_event)

    # 初始化执行的函数列表
    def func_list(self):
        self.reset_main_window()
        self.set_qss()
        self.set_icon()
        self.create_child_window()

    # 调整主窗口界面
    def reset_main_window(self):
        pass

    # 调整工作台窗口界面
    def reset_works_window(self):
        pass

    # 调整工具库窗口界面
    def reset_tools_window(self):
        pass

    # 重写close事件，关闭一切子窗口
    def closeEvent(self, event):
        try:
            # 终止所有任务，修改任务状态并保存
            flag = self.works_window.close_tasks()
            if flag:
                super().closeEvent(event)
                # 关闭后台线程
                self.works_window.workThread.terminate()
                # 关闭所有子窗口
                if self.works_window.childwindow_flag_task_input:
                    self.works_window.task_input.close()
                if self.works_window.childwindow_flag_func_detatil:
                    self.works_window.works_button.close()
                if self.works_window.childwindow_flag_task_result:
                    self.works_window.task_result.close()
                if self.tools_window.childwindow_flag_toolbutton:
                    self.tools_window.tool_buttons.close()
                if self.tools_window.childwindow_flag_addtoolbutton:
                    self.tools_window.tool_addbuttons.close()
                if self.tools_window.childwindow_flag_tunnelbutton:
                    self.tools_window.tunnel_buttons.close()
                if self.tools_window.childwindow_flag_addtunnelbutton:
                    self.tools_window.tunnel_addbuttons.close()
                if self.tools_window.childwindow_flag_tunnel_script:
                    self.tools_window.tunnel_edit_script.close()
                if self.tools_window.childwindow_flag_commandbutton:
                    self.tools_window.command_buttons.close()
                if self.tools_window.childwindow_flag_addcommandbutton:
                    self.tools_window.command_addbuttons.close()
                if self.combine_window.listWidget.childwindow_flag_editbutton:
                    self.combine_window.listWidget.buttons_event.close()
                if self.combine_window.childwindow_flag_variable:
                    self.combine_window.variable_and_result.close()
                if self.combine_window.childwindow_flag_func_detatil:
                    self.combine_window.func_detatil.close()
                if self.combine_window.childwindow_flag_func_introduction:
                    self.combine_window.func_introduction.close()
                if self.mine_window.childwindow_flag_func_detatil:
                    self.mine_window.func_detatil.close()
                pass
                # 保存笔记
                with open('config/works_note.txt', 'w', encoding='utf-8') as f:
                    f.write(self.works_window.note_text.toPlainText())
            else:
                event.ignore()
        except Exception as e:
            print(e, 'closeEvent Main')

    # 设置qss
    def set_qss(self):
        with open('qss/menu_list.qss', 'r', encoding='UTF-8') as f:
            self.menu_list.setStyleSheet(f.read())
        # with open('qss/works.qss', 'r', encoding='UTF-8') as f:
        #     self.works_window.setStyleSheet(f.read())
        self.main_window_logo.setStyleSheet('background-color:hsl(210, 42%, 95%);')
        self.setStyleSheet("""QListWidget {
            outline: 0px;
            background-color: transparent;
        }
        QListWidget::item:selected {
            border-radius: 2px;
            border: 1px solid rgb(0, 170, 255);
        }
        QListWidget::item:selected:!active {
            border-radius: 2px;
            border: 1px solid transparent;
        }
        QListWidget::item:selected:active {
            border-radius: 2px;
            border: 1px solid rgb(0, 170, 255);
        }
        QListWidget::item:hover {
            border-radius: 2px;
            border: 1px solid rgb(0, 170, 255);
        }""")

    # 设置图标
    def set_icon(self):
        self.icon_fold = QIcon("resource/image/fold.png")
        self.icon_unfold = QIcon("resource/image/unfold.png")
        self.button_fold.setIcon(self.icon_unfold)
        # self.main_window_logo.setPixmap(QPixmap("resource/image/urchin.png"))
        self.main_window_button_works.setIcon(QIcon("resource/image/works.png"))
        self.main_window_button_tools.setIcon(QIcon("resource/image/tools.png"))
        self.main_window_button_combine.setIcon(QIcon("resource/image/combine.png"))
        self.main_window_button_community.setIcon(QIcon("resource/image/community.png"))
        self.main_window_button_mine.setIcon(QIcon("resource/image/mine.png"))

    # 主界面左侧按钮切换设置
    def create_child_window(self):
        # 将子窗口对象替换为子界面
        self.works_window.setupUi(self.page_works)
        self.tools_window.setupUi(self.page_tools)
        self.combine_window.setupUi(self.page_combine)
        self.community_window.setupUi(self.page_community)
        self.mine_window.setupUi(self.page_mine)
        # 连接信号
        self.main_window_button_works.clicked.connect(self.show_child_window)
        self.main_window_button_tools.clicked.connect(self.show_child_window)
        self.main_window_button_combine.clicked.connect(self.show_child_window)
        self.main_window_button_community.clicked.connect(self.show_child_window)
        self.main_window_button_mine.clicked.connect(self.show_child_window)

    # 点击左侧按钮切换界面信号
    def show_child_window(self):
        dic = {
            "main_window_button_works": 0,
            "main_window_button_tools": 1,
            "main_window_button_combine": 2,
            "main_window_button_community": 3,
            "main_window_button_mine": 4,
        }
        index = dic[self.sender().objectName()]
        self.stackedWidget.setCurrentIndex(index)

    def refresh(self, index):
        if index == 0:
            self.works_window.repaint()
        elif index == 1:
            self.tools_window.repaint()
        elif index == 2:
            self.combine_window.repaint()
        elif index == 3:
            self.community_window.repaint()
        elif index == 4:
            self.mine_window.repaint()
        else:
            print("index error!")

    # 右边框按钮槽函数
    def button_fold_event(self):
        try:
            if self.button_fold.text() == '已展开':
                self.button_fold.setIcon(self.icon_unfold)
                self.button_fold.setText('已折叠')
                # self.right_widget.setVisible(False)
                self.setMinimumSize(QSize(771, 541))
                self.setMaximumSize(QSize(771, 541))
            elif self.button_fold.text() == '已折叠':
                self.button_fold.setIcon(self.icon_fold)
                self.button_fold.setText('已展开')
                # self.right_widget.setVisible(True)
                self.setMinimumSize(QSize(801, 541))
                self.setMaximumSize(QSize(801, 541))
        except Exception as e:
            print(e, 'button_fold_event')

    # 其他槽函数
    # 添加测试任务
    def add_test_task_event(self, config):
        self.stackedWidget.setCurrentIndex(0)
        self.works_window.add_task_event(config, test=True)

    # 添加任务
    def add_task_event(self, config):
        self.stackedWidget.setCurrentIndex(0)
        self.works_window.add_task_event(config, test=False)

    # 功能炼金重塑，刷新合成栏
    def refresh_combine_event(self):
        self.combine_window.listWidget.refresh()

    # 添加常用功能
    def add_collect_event(self, button_object):
        self.works_window.add_func(button_object)

    # 删除常用功能
    def del_collect_event(self, button_object):
        self.works_window.delete_func(button_object)

    # 添加自定义功能
    def add_func_event(self, config):
        self.mine_window.addcustom_add_event(config)

    # 预选区域刷新：工具
    def refresh_selected_tool_event(self):
        self.combine_window.selected_tools.refresh()

    # 预选区域刷新：通道
    def refresh_selected_tunnel_event(self):
        self.combine_window.selected_tunnels.refresh()

    # 预选区域刷新：配件
    def refresh_selected_components_event(self):
        self.combine_window.selected_components.refresh()

    # 预选区域删除：工具
    def del_selected_tool_event(self, object_name):
        self.combine_window.delete_selected_tool(object_name)

    # 预选区域删除：通道
    def del_selected_tunnel_event(self, object_name):
        self.combine_window.delete_selected_tunnel(object_name)

    # 预选区域删除：配件
    def del_selected_component_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # splash = QSplashScreen(QPixmap('resource/image/wait.png'))  # 启动界面图片地址
    # splash.show()  # 展示启动图片
    # app.processEvents()  # 防止进程卡死

    # 创建启动界面，支持png透明图片
    splash = QSplashScreen(QPixmap('resource/image/urchin.png'))
    splash.show()
    # 可以显示启动信息
    # splash.showMessage('正在加载……')
    # # 关闭启动画面
    # splash.close()

    window = Window()
    window.setWindowIcon(QIcon('resource/image/urchin.png'))
    window.show()

    splash.finish(window)
    # print(platform.system())
    # print(os.getpid())

    sys.exit(app.exec_())
