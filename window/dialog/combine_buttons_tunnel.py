from window.ui.combine_buttons_tunnel_dialog import Ui_combine_buttons_tunnel_dialog

from PyQt5.Qt import *
from window.func.mylist_item import Mylist_item


class Combine_buttons_tunnel_event(QWidget, Ui_combine_buttons_tunnel_dialog):
    config_change = pyqtSignal(dict)
    dialog_close = pyqtSignal()

    def __init__(self, mydata, tunnel_config, selectable_result):
        super().__init__()
        self.flag_change_input_value = False
        self.mydata = mydata
        self.tunnel_config = tunnel_config
        self.selectable_result = selectable_result
        self.selectable_result_extend = []

        self.setupUi(self)

    def setupUi(self, combine_buttons_tunnel_dialog):
        try:
            super().setupUi(combine_buttons_tunnel_dialog)
            self.setWindowIcon(QIcon('resource/image/urchin.png'))
            self.set_icon()
            # 绘制配件详情栏
            self.init_tunnel_list()
            # 填充内容
            tunnel_list = []
            for i in self.mydata['tunnel']:
                tunnel_list.append(self.tunnel_config[i]['name'])
            self.comboBox_tunnel.addItems(tunnel_list)
            if len(self.mydata['tunnel']) > 0:
                tunnel_one = self.mydata['tunnel'][0]
                self.comboBox_input.addItems(self.tunnel_config[tunnel_one]['input'])
                self.comboBox_output.addItems(self.tunnel_config[tunnel_one]['output'])
                self.plainTextEdit_introduction.setPlainText(self.tunnel_config[tunnel_one]['introduction'])
            if len(self.mydata['input_value']) != 0 and len(self.mydata['input_value'][0]) != 0:
                self.lineEdit_input_value.setText(self.mydata['input_value'][0][0])
                self.lineEdit_result_name.setText(self.mydata['result_name'][0][0])
            # 设置按钮菜单
            menus = QMenu(self.toolButton_input_value)
            action_list = {}
            for i in self.selectable_result:
                action_list[i] = QAction(self.icon_select_text, i, self)
                action_list[i].setData(i)
                menus.addAction(action_list[i])
                action_list[i].triggered.connect(self.select_input_value_event)
            self.toolButton_input_value.setMenu(menus)
            self.toolButton_input_value.setPopupMode(QToolButton.InstantPopup)
            # 去角标
            self.setStyleSheet('QToolButton::menu-indicator{image: none;}')
            # 连接命令选择信号
            self.comboBox_tunnel.currentIndexChanged[int].connect(self.change_tunnel_event)
            self.comboBox_input.currentIndexChanged[int].connect(self.change_input_event)
            self.comboBox_output.currentIndexChanged[int].connect(self.change_output_event)
            # 连接信号
            self.toolButton_result_name.clicked.connect(self.toolButton_result_name_event)
            self.lineEdit_input_value.textChanged.connect(self.change_input_value_event)
            self.lineEdit_result_name.textChanged.connect(self.change_result_name_event)
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'setupUi')

    def init_tunnel_list(self):
        layout = QGridLayout()
        self.tunnels = Mylist_item(self.widget_tunnel, self.mydata, self.tunnel_config, 'tunnel')
        layout.addWidget(self.tunnels)
        self.widget_tunnel.setLayout(layout)
        self.tunnels.config_change.connect(self.refresh_tunnel)

    def set_icon(self):
        self.icon_select_line = QIcon("resource/image/select_line.png")
        self.icon_edit = QIcon("resource/image/edit.png")
        self.icon_save = QIcon("resource/image/save.png")
        self.icon_select_text = QIcon("resource/image/select_text.png")
        self.toolButton_input_value.setIcon(self.icon_select_line)
        self.toolButton_result_name.setIcon(self.icon_edit)

    def refresh_tunnel(self, new_tunnel):
        try:
            self.mydata = new_tunnel
            self.refresh()
            self.comboBox_tunnel.clear()
            tunnel_list = []
            for i in self.mydata['tunnel']:
                tunnel_list.append(self.tunnel_config[i]['name'])
            self.comboBox_tunnel.addItems(tunnel_list)
            self.change_tunnel_event(0)

            # self.comboBox_tunnel.setCurrentIndex(0)
            # self.comboBox_input.setCurrentIndex(0)
            # self.comboBox_output.setCurrentIndex(0)
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'refresh_tunnel')

    def refresh(self):
        try:
            self.config_change.emit(self.mydata)
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'refresh_tunnel')

    # 更换所选通道
    def change_tunnel_event(self, index):
        try:
            object_name = self.mydata['tunnel'][index]
            self.comboBox_tunnel.setCurrentIndex(index)
            self.comboBox_input.clear()
            self.comboBox_output.clear()
            self.comboBox_input.addItems(self.tunnel_config[object_name]['input'])
            self.comboBox_output.addItems(self.tunnel_config[object_name]['output'])
            # 重设编辑按钮
            self.lineEdit_result_name.setReadOnly(True)
            self.toolButton_result_name.setIcon(self.icon_edit)
            # 重设按钮菜单
            menus = QMenu(self.toolButton_input_value)
            action_list = {}
            all_result = self.selectable_result
            for i in range(index):
                for j in self.mydata['result_name'][i]:
                    if j != '':
                        all_result.extend(j)
            for i in all_result:
                action_list[i] = QAction(self.icon_select_text, i, self)
                action_list[i].setData(i)
                menus.addAction(action_list[i])
                action_list[i].triggered.connect(self.select_input_value_event)
            self.toolButton_input_value.setMenu(menus)
            self.toolButton_input_value.setPopupMode(QToolButton.InstantPopup)
            if len(self.tunnel_config[object_name]['input']) > 0:
                self.lineEdit_input_value.setText(self.mydata['input_value'][index][0])
            else:
                self.lineEdit_input_value.setText('')
            if len(self.tunnel_config[object_name]['output']) > 0:
                self.lineEdit_result_name.setText(self.mydata['result_name'][index][0])
            else:
                self.lineEdit_result_name.setText('')
            self.plainTextEdit_introduction.setPlainText(self.tunnel_config[object_name]['introduction'])
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'change_tunnel_event')

    # 输入变量更换所选行
    def change_input_event(self, index):
        try:
            if index >= 0 and self.comboBox_tunnel.currentIndex() >= 0:
                # print('input_value', self.comboBox_tunnel.currentIndex(), index, self.mydata['input_value'][self.comboBox_tunnel.currentIndex()])
                input_value = self.mydata['input_value'][self.comboBox_tunnel.currentIndex()][index]
                self.lineEdit_input_value.setText(input_value)
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'change_input_event')

    # 输出变量更换所选行
    def change_output_event(self, index):
        try:
            if index >= 0 and self.comboBox_tunnel.currentIndex() >= 0:
                self.lineEdit_result_name.setReadOnly(True)
                self.toolButton_result_name.setIcon(self.icon_edit)
                # print('input_value', self.comboBox_tunnel.currentIndex(), index, self.mydata['result_name'][self.comboBox_tunnel.currentIndex()])
                self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][index])
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'change_output_event')

    # 变量值更改文本
    def change_input_value_event(self, new_text):
        try:
            if self.flag_change_input_value:
                self.mydata['input_value'][self.comboBox_tunnel.currentIndex()][self.comboBox_input.currentIndex()] = new_text
                index = self.comboBox_tunnel.currentIndex()
                all_result = self.selectable_result
                for i in range(index):
                    for j in self.mydata['result_name'][i]:
                        if j != '':
                            all_result.extend(j)
                # !!!!!!!!!!!!!!! 待调整结果失效措施
                if self.lineEdit_input_value.text() not in all_result and self.lineEdit_input_value.text() != '':
                    # self.lineEdit_input_value.setText(self.lineEdit_input_value.text() + '(失效结果)')
                    self.lineEdit_input_value.setText('')
                    self.mydata['input_value'][self.comboBox_tunnel.currentIndex()][self.comboBox_input.currentIndex()] = ''
                #     self.lineEdit_input_value.setStyleSheet('color: rgb(255, 0, 0);')
                # else:
                #     self.lineEdit_input_value.setStyleSheet('')
                self.refresh()
                # self.tunnels.update_config(self.mydata)
            self.flag_change_input_value = False
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'change_input_value_event')

    # 结果变量更改文本
    def change_result_name_event(self, new_text):
        try:
            if len(new_text) == 0:
                self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][self.comboBox_output.currentIndex()] = ''
                self.refresh()
                # self.tunnels.update_config(self.mydata)
            elif len(new_text) > 1 and new_text[0] == '$' and new_text[1] != '$':
                if new_text not in self.selectable_result and new_text not in self.selectable_result_extend:
                    self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][self.comboBox_output.currentIndex()] = new_text
                    self.refresh()
                    # self.tunnels.update_config(self.mydata)
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'change_result_name_event')

    #  右侧按钮槽函数
    def toolButton_result_name_event(self):
        try:
            if self.lineEdit_result_name.isReadOnly():
                self.lineEdit_result_name.setReadOnly(False)
                self.toolButton_result_name.setIcon(self.icon_save)
            else:
                self.lineEdit_result_name.setReadOnly(True)
                self.toolButton_result_name.setIcon(self.icon_edit)
                new_text = self.lineEdit_result_name.text()
                if len(new_text) == 1:
                    QMessageBox.warning(self, "操作提示", '请注意变量格式！变量以\'$\'开头。', QMessageBox.Ok)
                    self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][self.comboBox_output.currentIndex()])
                elif len(new_text) > 1:
                    if new_text[0] != '$' or new_text[1] == '$':
                        QMessageBox.warning(self, "操作提示", '请注意变量格式！变量以\'$\'开头。', QMessageBox.Ok)
                        self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][self.comboBox_output.currentIndex()])
                if new_text in self.selectable_result or new_text in self.selectable_result_extend:
                    QMessageBox.warning(self, "操作提示", '请勿使用重复变量名称！', QMessageBox.Ok)
                    self.lineEdit_result_name.setText(self.mydata['result_name'][self.comboBox_tunnel.currentIndex()][self.comboBox_output.currentIndex()])
                self.refresh()
        except Exception as e:
            print(e, 'Combine_buttons_tunnel_event', 'toolButton_result_name_event')

    def select_input_value_event(self):
        self.flag_change_input_value = True
        self.lineEdit_input_value.setText(self.sender().data())
        self.mydata['input_value'][self.comboBox_tunnel.currentIndex()][self.comboBox_input.currentIndex()] = self.sender().data()
