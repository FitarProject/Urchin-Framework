from window.ui.works_addbutton_dialog import Ui_works_addbutton_dialog
from window.paint.button_record import Button_list

from PyQt5.Qt import *
import json


class Works_addbutton_event(QWidget, Ui_works_addbutton_dialog):
    trigger_add_func = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.func_button_list = []
        self.dict_to_button = {}
        self.func_button = {}
        self.func_checkbox = {}
        self.button_list = Button_list(10, 10, 50, 50, 40, 40, 410, 4100)
        self.setupUi(self)

    def setupUi(self, works_addbutton_dialog):
        try:
            super().setupUi(works_addbutton_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.read_config()
            for object_name in self.func_button_list:
                button_config = self.dict_to_button[object_name]
                x, y, width, height = self.button_list.add_button(object_name)
                self.func_button[object_name] = QPushButton(self.scrollAreaWidgetContents)
                self.func_button[object_name].setGeometry(QRect(x, y, width, height))
                self.func_button[object_name].setObjectName(object_name)
                self.func_button[object_name].setText(button_config['name'])
                self.func_button[object_name].setToolTip('功能名称：' + button_config['name'] + '\n功能介绍：' + button_config['introduction'])
                self.func_button[object_name].setVisible(True)
                self.func_button[object_name].clicked.connect(self.buttons_selected_event)
                self.func_checkbox[object_name] = QCheckBox(self.scrollAreaWidgetContents)
                self.func_checkbox[object_name].setGeometry(QRect(x + 26, y + 1, width - 27, height - 27))
                self.func_checkbox[object_name].setObjectName(button_config['name'] + '_checkbox')
                self.func_checkbox[object_name].raise_()
                self.func_checkbox[object_name].setVisible(True)
            self.button_select_all.clicked.connect(self.selectall_button_event)
            self.button_yes.clicked.connect(self.button_yes_event)
        except Exception as e:
            print(e, 'Works_addbutton_event', 'setupUi')

    def read_config(self):
        try:
            with open('config/mine_func_custom.json', 'r', encoding='utf-8') as f:
                self.dict_to_button = json.load(f)
                for i in self.dict_to_button.keys():
                    self.func_button_list.append(i)
            with open('config/works_buttons.json', 'r', encoding='utf-8') as f:
                func_collect = json.load(f)
            # 删除已收藏的功能
            for func_object in func_collect['func_list']:
                self.func_button_list.remove(func_object)
        except Exception as e:
            print(e, 'Works_addbutton_event', 'read_config')

    # 按钮点击事件
    def buttons_selected_event(self):
        try:
            if self.func_checkbox[self.sender().objectName()].isChecked():
                self.func_checkbox[self.sender().objectName()].setChecked(False)
            elif not self.func_checkbox[self.sender().objectName()].isChecked():
                self.func_checkbox[self.sender().objectName()].setChecked(True)
            else:
                print('按钮选中状态错误')
        except Exception as e:
            print(e, 'Works_addbutton_event', 'buttons_selected_event')

    # 全选功能
    def selectall_button_event(self):
        try:
            if self.button_select_all.text() == '全选':
                self.button_select_all.setText('取消')
                for name in self.button_list.get_button_list():
                    self.func_checkbox[name].setChecked(True)
            else:
                self.button_select_all.setText('全选')
                for name in self.button_list.get_button_list():
                    self.func_checkbox[name].setChecked(False)
        except Exception as e:
            print(e, 'Works_addbutton_event', 'selectall_button_event')

    def button_yes_event(self):
        try:
            name_list = self.button_list.get_button_list()
            for func_object_name in name_list:
                if self.func_checkbox[func_object_name].isChecked():
                    self.trigger_add_func.emit(func_object_name)
            self.close()
        except Exception as e:
            print(e, 'Works_addbutton_event', 'button_yes_event')
