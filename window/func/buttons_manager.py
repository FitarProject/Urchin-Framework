from PyQt5.Qt import *
import json
# 待调试，无法使用！！！

# 用于管理按钮组
class Buttons_manager(object):
    def __init__(self, qtobject_page1, qtobject_page2, button_list, config_filename='works_buttons.json'):
        self.page1_button = {}
        self.page2_button = {}
        self.page2_checkbox = {}
        self.dict_to_button = {}

        self.qtobject_page1 = qtobject_page1
        self.qtobject_page2 = qtobject_page2
        self.button_list = button_list
        self.config_file = 'config/' + config_filename

        self.read_config()
        self.buttons_paint()

    # 读取配置文件
    def read_config(self):
        with open(self.config_file, 'r') as f:
            self.dict_to_button = json.load(f)
            self.dict_to_button['button_add'] = {
            'name': '添加',
            'command': '',
            'example': [],
        }

    def save_config(self):
        try:
            del self.dict_to_button['button_add']
            with open('config/works_buttons.json', 'w') as f:
                json.dump(self.dict_to_button, f)
            self.dict_to_button['button_add'] = {
                'name': '添加',
                'command': '',
                'example': [],
            }
        except Exception as e:
            print(e, 'Buttons_manager')

    # 绘制按钮
    def buttons_paint(self):
        for button_object_name, button_config in self.dict_to_button.items():
            # 绘制第一页的按钮
            try:
                x, y, width, height = self.button_list.add_button(button_object_name)
                self.page1_button[button_object_name] = QPushButton(qtobject_page1)
                self.page1_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page1_button[button_object_name].setObjectName(button_object_name)
                self.page1_button[button_object_name].setText(button_config['name'])
                self.page1_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                # self.page1_button[button_object_name].show()
                self.page1_button[button_object_name].setVisible(True)
                self.page1_button[button_object_name].clicked.connect(self.buttons_clicked_event)
            except Exception as e:
                print(e, 'Buttons_manager')
            # 绘制第二页的按钮
            try:
                if button_object_name == 'button_add':
                    continue
                self.page2_button[button_object_name] = QPushButton(qtobject_page2)
                self.page2_button[button_object_name].setGeometry(QRect(x, y, width, height))
                self.page2_button[button_object_name].setObjectName(button_object_name)
                self.page2_button[button_object_name].setText(button_config['name'])
                self.page2_button[button_object_name].setToolTip('<html><head/><body><p>' + button_config['name'] + '</p></body></html>')
                # self.page2_button[button_object_name].show()
                self.page2_button[button_object_name].setVisible(True)
                self.page2_checkbox[button_object_name] = QCheckBox(qtobject_page2)
                self.page2_checkbox[button_object_name].setGeometry(QRect(x+26, y+1, width-27, height-27))
                self.page2_checkbox[button_object_name].setObjectName(button_config['name'] + '_checkbox')
                self.page2_checkbox[button_object_name].raise_()
                self.page2_checkbox[button_object_name].setVisible(True)
            except Exception as e:
                print(e, 'Buttons_manager')

    def buttons_repaint(self):
        self.save_config()
        self.buttons_reset_position()
        self.repaint()

    def buttons_reset_position(self):
        for button_object_name in self.dict_to_button.keys():
            x, y = self.button_list.get_button_position(button_object_name)
            width, height = self.button_list.width, self.button_list.height
            self.page1_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.page2_button[button_object_name].setGeometry(QRect(x, y, width, height))
            self.page2_checkbox[button_object_name].setGeometry(QRect(x + 26, y + 1, width - 27, height - 27))
            print(x, y, button_object_name)

    def buttons_clear(self):
        pass








'''
from PyQt5.Qt import *
import json

from window.works_window import Ui_works_window
from window.paint.button_record import Button_list
from window.dialog.works_buttons import Works_buttons_event
from window.func.buttons_manager import Buttons_manager


class Works(QWidget, Ui_works_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.func_list()

    def setupUi(self, works_window):
        super().setupUi(works_window)
        self.buttons_manager = Buttons_manager(self.scrollAreaWidgetContents_page1, self.scrollAreaWidgetContents_page2, Button_list(10, 10, 50, 50, 40, 40, 314, 3140), 'works_buttons.json')
        # 设置最初展示界面
        self.stackedWidget.setCurrentIndex(0)
        self.selectall_button.hide()
        self.delete_button.hide()
        # 连接信号与槽函数
        self.manage_button.clicked.connect(self.manage_button_event)
        self.selectall_button.clicked.connect(self.selectall_button_event)
        self.delete_button.clicked.connect(self.delete_button_event)

    # 初始化执行的函数列表
    def func_list(self):
        print(self.buttons_manager.page2_checkbox.keys())
        pass

    # 自定义槽函数
    def manage_button_event(self):
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
            for name in self.buttons_manager.button_list.get_button_list()[:-1]:
                self.buttons_manager.page2_checkbox[name].setChecked(False)

    def selectall_button_event(self):
        try:
            if self.selectall_button.text() == '全选':
                self.selectall_button.setText('取消')
                for name in self.buttons_manager.button_list.get_button_list()[:-1]:
                    self.buttons_manager.page2_checkbox[name].setChecked(True)
            else:
                self.selectall_button.setText('全选')
                for name in self.buttons_manager.button_list.get_button_list()[:-1]:
                    self.buttons_manager.page2_checkbox[name].setChecked(False)
        except Exception as e:
            print('selectall_button_event', e)

    def delete_button_event(self):
        count = 0
        name_list = self.buttons_manager.button_list.get_button_list()[:-1]
        for name in name_list:
            if self.buttons_manager.page2_checkbox[name].isChecked():
                count += 1
        try:
            if count != 0:
                if QMessageBox.warning(self, "操作确认", '是否删除这%s个功能？' % count, QMessageBox.Ok | QMessageBox.Close) == QMessageBox.Ok:
                    for name in name_list:
                        if self.buttons_manager.page2_checkbox[name].isChecked():
                            self.buttons_manager.button_list.remove_button(name)
                            del self.buttons_manager.dict_to_button[name]
                            self.buttons_manager.page1_button[name].deleteLater()
                            self.buttons_manager.page2_button[name].deleteLater()
                            self.buttons_manager.page2_checkbox[name].deleteLater()
                    try:
                        self.buttons_manager.buttons_repaint()
                    except Exception as e:
                        print(e)
        except Exception as e:
            pass

    def buttons_clicked_event(self, str):
        works_button = Works_buttons_event()
        works_button.show()
        pass

'''