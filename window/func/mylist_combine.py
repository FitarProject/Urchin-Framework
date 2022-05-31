from PyQt5.Qt import *
import json

from window.func.mylist_combine_selected import Mylist_selected
from window.func.dropbutton import DropButton
from window.dialog.combine_buttons_tool import Combine_buttons_tool_event
from window.dialog.combine_buttons_tunnel import Combine_buttons_tunnel_event


class Mylist_combine(QListWidget):
    config_change = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Mylist_combine, self).__init__(*args, **kwargs)
        self.button_list = []
        self.variable_config = {}
        self.tool_config = {}
        self.tunnel_config = {}
        self.component_config = {}
        self.rightmenu_curr = None
        self.mouse_pos = None
        self.button_edit = 'button_1'
        self.select_row = -1
        self.drop_row = -1
        self.childwindow_flag_tool = False
        self.childwindow_flag_tunnel = False
        self.childwindow_flag_editbutton = False
        # self.icon_tool = QIcon("resource/image/tool.png")
        # self.icon_tunnel = QIcon("resource/image/tunnel.png")

        self.setAcceptDrops(True)
        self.setFlow(QListView.LeftToRight)
        self.setWrapping(True)
        self.setResizeMode(QListView.Adjust)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setMovement(QListView.Snap)
        self.setLayoutMode(QListView.Batched)
        self.setItemAlignment(Qt.AlignCenter)
        self.setSpacing(10)

        self.setDragEnabled(False)
        # self.setDefaultDropAction(Qt.TargetMoveAction)
        self.setDefaultDropAction(Qt.IgnoreAction)
        # self.setDropIndicatorShown(False)

        self.read_config()
        self.get_tool_config()
        self.get_tunnel_config()
        self.get_component_config()
        self.get_variable_config()
        self.init_variable_config()
        for data in self.button_list:
            self.makeItem(QSize(57, 57), data)
        # self.setTabKeyNavigation(True)
        # self.setDragEnabled(True)
        # self.setDragDropMode(QAbstractItemView.DropOnly)
        # self.setDefaultDropAction(Qt.CopyAction)
        # self.setGridSize(QSize(80, 80))
        # self.setViewMode(QListView.IconMode)
        # self.setSelectionRectVisible(True)

    def read_config(self):
        try:
            with open('config/combine.txt', 'r', encoding='utf-8') as f:
                tmp = f.readlines()
                for i in tmp:
                    self.button_list.append(eval(i))
        except FileNotFoundError:
            with open('config/combine.txt', 'w', encoding='utf-8') as f:
                f.write('')
            self.button_list = []

    def get_variable_config(self):
        with open('config/combine_variable.json', 'r', encoding='utf-8') as f:
            self.variable_config = json.load(f)

    def get_tool_config(self):
        with open('config/tools_buttons_tool.json', 'r', encoding='utf-8') as f:
            self.tool_config = json.load(f)

    def get_tunnel_config(self):
        with open('config/tools_buttons_tunnel.json', 'r', encoding='utf-8') as f:
            self.tunnel_config = json.load(f)

    def get_component_config(self):
        with open('config/tools_buttons_component.json', 'r', encoding='utf-8') as f:
            self.component_config = json.load(f)

    def save_config(self):
        try:
            # print(self.button_list)
            with open('config/combine.txt', 'w', encoding='utf-8') as f:
                for data in self.button_list:
                    f.write(str(data) + '\n')
            with open('config/combine_variable.json', 'w', encoding='utf-8') as f:
                json.dump(self.variable_config, f)
            self.init_variable_config()
            self.config_change.emit()
        except Exception as e:
            print(e, 'Mylist_combine', 'save_config')

    # 重绘所有item
    def refresh(self):
        try:
            self.clear()
            self.button_list.clear()
            self.read_config()
            self.get_tool_config()
            self.get_tunnel_config()
            self.get_component_config()
            for data in self.button_list:
                self.makeItem(QSize(57, 57), data)
        except Exception as e:
            print(e, 'Mylist_combine', 'refresh')

    # 初始化变量配置，从部件列表中读取
    def init_variable_config(self):
        try:
            name = self.variable_config['name']
            introduction = self.variable_config['introduction']
            self.variable_config = {
                "name": name,
                "variable": [],
                "result": [],
                "introduction": introduction,
                "config": self.button_list
            }
            button_index = 1
            for i in self.button_list:
                if i['type'] == 0:
                    for j in i['variable']:
                        # print(self.tool_config)
                        # print(self.tool_config[i['button_num']]['name'])
                        # print(i['variable_value'][i['variable'].index(j)])
                        self.variable_config['variable'].append({"name": j, "position": str(button_index), "widget_name": self.tool_config[i['button_num']]['name'], "value": i['variable_value'][i['variable'].index(j)]})
                    for j in i['result_name']:
                        if j != '':
                            self.variable_config['result'].append(j)
                elif i['type'] == 1:
                    index = 0
                    for j in i['tunnel']:
                        input_index = 0
                        for k in i['input_value'][index]:
                            self.variable_config['variable'].append({"name": self.tunnel_config[j]['input'][input_index], "position": str(button_index)+'-'+str(index+1), "widget_name": self.tunnel_config[j]['name'], "value": k})
                            input_index += 1
                        for k in i['result_name'][index]:
                            if k != '':
                                self.variable_config['result'].append(k)
                        index += 1
                button_index += 1
            with open('config/combine_variable.json', 'w', encoding='utf-8') as f:
                json.dump(self.variable_config, f)
        except Exception as e:
            print(e, 'Mylist_combine', 'init_variable_config')

    def refresh_tool(self, button):
        try:
            data = button.property('data')
            object_name = data['button_num']
            component_num = len(data['component'])
            command_num = data['command_num']
            component_list = ''
            command = self.tool_config[object_name]['command_template'][command_num]
            for component_object in data['component']:
                component_list += self.component_config[component_object]['name'] + ','
            # 初始化命令中的变量
            if len(data['result_name']) == 0:
                variable = []
                variable_value = []
                result_name = []
                for i in command.split(' '):
                    if i[0] == '$':
                        variable.append(i)
                        variable_value.append('')
                for i in range(len(self.tool_config[object_name]['result'])):
                    result_name.append('')
                data['variable'] = variable
                data['variable_value'] = variable_value
                data['result_name'] = result_name
            button.setText(self.tool_config[object_name]['simple_name'] + '\n' + '配件 * %d' % component_num)
            button.setToolTip('工具：' + self.tool_config[object_name]['name'] + '\n' + '命令：' + self.tool_config[object_name]['command_template'][command_num] + '\n' + '配件：' + component_list.rstrip(','))
            button.setProperty('data', data)
            item = self.itemFromIndex(button.property('item'))
            index = self.row(item)
            self.button_list[index] = data
            self.save_config()
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_combine', 'refresh_tool')
        # for index in range(len(self.button_list)):
        #     button = self.itemWidget(self.itemFromIndex(index))
        #     print(button)

    def refresh_tunnel(self, button, flag=False):
        try:
            data = button.property('data')
            tunnel = data['tunnel']
            tunnel_list = '      '
            for tunnel_object in tunnel:
                tunnel_list += self.tunnel_config[tunnel_object]['name'] + '\n      '
            if flag:
                input_value = [''] * len(self.tunnel_config[tunnel[-1]]['input'])
                result_name = [''] * len(self.tunnel_config[tunnel[-1]]['output'])
                data['input_value'].append(input_value)
                data['result_name'].append(result_name)
            # 纠正输入输出变量数量
            pass
            button.setText('通道 * %d' % len(tunnel))
            button.setToolTip('通道列表：\n' + tunnel_list.rstrip('\n '))
            button.setProperty('data', data)
            item = self.itemFromIndex(button.property('item'))
            index = self.row(item)
            self.button_list[index] = data
            self.save_config()
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_combine', 'refresh_tunnel')

    def makeItem(self, size, mydata):
        if mydata['type'] == 0:
            object_name = mydata['button_num']
            component_list = ''
            for component_object in mydata['component']:
                component_list += self.component_config[component_object]['name'] + ','
            item = QListWidgetItem(self)
            item.setData(Qt.UserRole + 1, mydata)
            item.setSizeHint(size)
            button = DropButton(self, 0)
            button.setContextMenuPolicy(Qt.CustomContextMenu)
            if object_name != '空工具':
                button.setText(self.tool_config[object_name]['simple_name'] + '\n' + '配件 * %d' % len(mydata['component']))
                button.setToolTip('工具：' + self.tool_config[object_name]['name'] + '\n' + '命令：' + self.tool_config[object_name]['command_template'][mydata['command_num']] + '\n' + '配件：' + component_list.rstrip(','))
            else:
                button.setText('空工具\n配件 * 0')
                button.setToolTip('工具：无\n命令：无\n配件： ')
            button.setProperty('type', mydata['type'])
            # button.setProperty('object_name', mydata['button_num'])
            # button.setProperty('command_num', mydata['command_num'])
            # button.setProperty('component', mydata['component'])
            button.setProperty('data', mydata)
            # button.setProperty('data', self.tool_config[object_name])
            # button.clicked.connect(lambda : print(button.property('data')))
            button.refresh_tool.connect(self.refresh_tool)
            button.customContextMenuRequested.connect(self.button_rightmenu_event)
            self.setItemWidget(item, button)
            button.setProperty('item', self.indexFromItem(item))
        elif mydata['type'] == 1:
            tunnel_list = '      '
            for tunnel_object in mydata['tunnel']:
                tunnel_list += self.tunnel_config[tunnel_object]['name'] + '\n      '
            item = QListWidgetItem(self)
            item.setData(Qt.UserRole + 1, mydata)
            item.setSizeHint(size)
            button = DropButton(self, 1)
            button.setContextMenuPolicy(Qt.CustomContextMenu)
            button.setText('通道 * %d' % len(mydata['tunnel']))
            button.setToolTip('通道列表：\n' + tunnel_list.rstrip('\n '))
            button.setProperty('type', mydata['type'])
            # button.setProperty('tunnel_list', mydata['tunnel'])
            button.setProperty('data', mydata)
            # button.clicked.connect(lambda : print(button.property('tunnel_list')))
            button.refresh_tunnel.connect(self.refresh_tunnel)
            button.customContextMenuRequested.connect(self.button_rightmenu_event)
            self.setItemWidget(item, button)
            button.setProperty('item', self.indexFromItem(item))

    def dragEnterEvent(self, event):
        try:
            if self.dragDropMode() == QAbstractItemView.DropOnly:
                mimeData = event.mimeData()
                if mimeData.property('mytool') or mimeData.property('mytunnel') or mimeData.property('mycomponent'):
                    event.acceptProposedAction()
                else:
                    event.ignore()
            else:
                super().dragEnterEvent(event)
        except Exception as e:
            print(e, 'Mylist_combine', 'dragEnterEvent')

    def dropEvent(self, event):
        if self.dragDropMode() == QAbstractItemView.DropOnly:
            try:
                pass
            except Exception as e:
                print(e, 'Mylist_combine', 'dropEvent')
        else:
            super().dropEvent(event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.select_row = self.row(self.itemAt(event.pos()))

    def startDrag(self, supportedActions):
        if self.dragDropMode() == QAbstractItemView.DropOnly:
            try:
                items = self.selectedItems()
                drag = QDrag(self)
                mimeData = self.mimeData(items)
                drag.setMimeData(mimeData)
                pixmap = QPixmap(self.viewport().visibleRegion().boundingRect().size())
                pixmap.fill(Qt.transparent)
                painter = QPainter()
                painter.begin(pixmap)
                for item in items:
                    rect = self.visualRect(self.indexFromItem(item))
                    painter.drawPixmap(rect, self.viewport().grab(rect))
                painter.end()
                drag.setPixmap(pixmap)
                drag.setHotSpot(self.viewport().mapFromGlobal(QCursor.pos()))
                drag.exec_(supportedActions)
            except Exception as e:
                print(e, 'Mylist_combine', 'startDrag')
        else:
            try:
                super().startDrag(supportedActions)
                self.drop_row = self.indexFromItem(self.selectedItems()[0]).row()
                # 根据拖拽情况更改列表顺序
                if self.select_row != -1 and self.drop_row != -1:
                    if self.select_row < self.drop_row:
                        tmp = self.button_list[self.select_row]
                        self.button_list.insert(self.drop_row + 1, tmp)
                        self.button_list.pop(self.select_row)
                        self.save_config()
                    elif self.select_row > self.drop_row:
                        tmp = self.button_list[self.select_row]
                        self.button_list.pop(self.select_row)
                        self.button_list.insert(self.drop_row, tmp)
                        self.save_config()
                    self.save_config()
                    self.refresh()
                print(self.select_row, '->', self.drop_row)
            except Exception as e:
                print(e, 'Mylist_combine', 'startDrag')

    # 按钮右键菜单
    def button_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().property('item').row()
            self.button_rightmenu = QMenu(self)
            self.button_action_edit = QAction(QIcon('resource/image/edit.png'), u'编辑', self)
            self.button_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            self.button_rightmenu.addAction(self.button_action_edit)
            self.button_rightmenu.addAction(self.button_action_delete)
            self.button_action_edit.triggered.connect(self.button_action_edit_event)
            self.button_action_delete.triggered.connect(self.button_action_delete_event)

            self.button_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'Mylist_combine', 'button_rightmenu')

    def button_action_edit_event(self):
        try:
            # print(self.rightmenu_curr)
            widget = self.itemWidget(self.item(self.rightmenu_curr))
            mytype = widget.property('type')
            mydata = widget.property('data')
            selectable_result = ['手动输入', '交互输入']
            if mytype == 0:
                if mydata['button_num'] == '空工具':
                    return
            if mytype == 1:
                if not mydata['tunnel']:
                    return
            for i in range(self.rightmenu_curr):
                but = self.itemWidget(self.item(i))
                if but.property('type') == 0:
                    for j in but.property('data')['result_name']:
                        if len(j) != 0:
                            selectable_result.append(j)
                elif but.property('type') == 1:
                    for j in but.property('data')['result_name']:
                        for k in j:
                            if len(k) != 0:
                                selectable_result.extend(j)
            if self.childwindow_flag_editbutton:
                self.buttons_event.close()
            if mytype == 0:
                self.childwindow_flag_editbutton = True
                self.buttons_event = Combine_buttons_tool_event(mydata, self.tool_config[mydata['button_num']], self.component_config, selectable_result)
                self.buttons_event.dialog_close.connect(self.buttons_dialog_close)
                self.buttons_event.config_change.connect(self.buttons_config_change)
                self.buttons_event.show()
            elif mytype == 1:
                self.childwindow_flag_editbutton = True
                self.buttons_event = Combine_buttons_tunnel_event(mydata, self.tunnel_config, selectable_result)
                self.buttons_event.dialog_close.connect(self.buttons_dialog_close)
                self.buttons_event.config_change.connect(self.buttons_config_change)
                self.buttons_event.show()
        except Exception as e:
            print(e, 'Mylist_combine', 'button_action_edit_event')

    def button_action_delete_event(self):
        try:
            self.button_list.pop(self.rightmenu_curr)
            self.itemWidget(self.item(self.rightmenu_curr)).deleteLater()
            self.takeItem(self.rightmenu_curr)
            self.save_config()
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_combine', 'button_action_delete_event')

    def buttons_config_change(self, new_data):
        try:
            self.button_list[self.rightmenu_curr] = new_data
            button = self.itemWidget(self.item(self.rightmenu_curr))
            button.setProperty('data', new_data)
            if new_data['type'] == 0:
                self.refresh_tool(button)
            elif new_data['type'] == 1:
                self.refresh_tunnel(button)
            # print(new_data)
        except Exception as e:
            print(e, 'Mylist_combine', 'buttons_config_change')

    def buttons_dialog_close(self):
        self.childwindow_flag_editbutton = False

