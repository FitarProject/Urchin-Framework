from PyQt5.Qt import *
import json


class Mylist_item(QListWidget):
    config_change = pyqtSignal(dict)

    def __init__(self, parent, item_data, config_detailed, item_type):
        super(Mylist_item, self).__init__(parent)
        self.item_data = item_data
        self.config_detailed = config_detailed
        self.item_type = item_type
        self.rightmenu_curr = None
        self.create_menu()

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setFlow(QListView.LeftToRight)
        self.setWrapping(True)
        self.setResizeMode(QListView.Adjust)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setMovement(QListView.Snap)
        self.setLayoutMode(QListView.Batched)
        self.setItemAlignment(Qt.AlignCenter)
        self.setSpacing(5)
        self.setDefaultDropAction(Qt.IgnoreAction)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        size = QSize(54, 54)
        if self.item_type == 'component':
            for object_name in self.item_data['component']:
                self.makeItem(size, object_name)
        elif self.item_type == 'tunnel':
            for object_name in self.item_data['tunnel']:
                self.makeItem(size, object_name)

    def create_menu(self):
        try:
            self.menu = QMenu(self)  # 创建菜单
            self.menu.addAction(QAction(u'删除 ', self, triggered=self.button_action_delete_event))
        except Exception as e:
            print(e, 'Mylist_item', 'refresh')

    def makeItem(self, size, object_name):
        try:
            item = QListWidgetItem(self)
            item.setSizeHint(size)
            item.setData(Qt.UserRole + 1, object_name)
            # item.setData(Qt.UserRole + 2, self.config_detailed[object_name])
            tips = self.config_detailed[object_name]
            item.setText(tips['name'])
            item.setTextAlignment(Qt.AlignCenter)
            if self.item_type == 'tunnel':
                indedx = self.item_data['tunnel'].index(object_name)
                item.setData(Qt.UserRole + 3, self.item_data['input_value'][indedx])
                item.setData(Qt.UserRole + 4, self.item_data['result_name'][indedx])
                item.setToolTip('通道：'+tips['name']+'\n输入：'+str(len(tips['input']))+'个\n输出：'+str(len(tips['output']))+'个\n介绍：'+tips['introduction'])
            elif self.item_type == 'component':
                item.setToolTip('配件：'+tips['name']+'\n介绍：'+tips['introduction'])
        except Exception as e:
            print(e, 'Mylist_item', 'makeItem')

    def refresh(self):
        try:
            self.config_change.emit(self.item_data)
        except Exception as e:
            print(e, 'Mylist_item', 'refresh')

    def update_config(self, new_data):
        # self.item_data['input_value'] = new_input_value
        # self.item_data['result_name'] = new_result_name
        self.item_data = new_data
        self.clear()
        size = QSize(54, 54)
        if self.item_type == 'component':
            for object_name in self.item_data['component']:
                self.makeItem(size, object_name)
        elif self.item_type == 'tunnel':
            for object_name in self.item_data['tunnel']:
                self.makeItem(size, object_name)

    def mousePressEvent(self, event):
        try:
            super().mousePressEvent(event)
            if event.button() == Qt.RightButton and self.itemAt(event.pos()):
                self.rightmenu_curr = self.itemAt(event.pos())
                self.menu.exec(event.globalPos())
        except Exception as e:
            print(e, 'Mylist_item', 'mousePressEvent')

    def dropEvent(self, event):
        try:
            super().dropEvent(event)
            if self.item_type == 'component':
                for i in range(len(self.item_data['component'])):
                    self.item_data['component'][i] = self.item(i).data(Qt.UserRole + 1)
            elif self.item_type == 'tunnel':
                for i in range(len(self.item_data['tunnel'])):
                    self.item_data['tunnel'][i] = self.item(i).data(Qt.UserRole + 1)
                    self.item_data['input_value'][i] = self.item(i).data(Qt.UserRole + 3)
                    self.item_data['result_name'][i] = self.item(i).data(Qt.UserRole + 4)
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_item', 'dropEvent')

    def button_action_delete_event(self):
        try:
            if self.item_type == 'component':
                index = self.item_data['component'].index(self.rightmenu_curr.data(Qt.UserRole + 1))
                self.item_data['component'].pop(index)
            elif self.item_type == 'tunnel':
                index = self.item_data['tunnel'].index(self.rightmenu_curr.data(Qt.UserRole + 1))
                self.item_data['tunnel'].pop(index)
                self.item_data['input_value'].pop(index)
                self.item_data['result_name'].pop(index)
            self.takeItem(self.currentRow())
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_item', 'button_action_delete_event')