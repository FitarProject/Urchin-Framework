from PyQt5.Qt import *
import json


class Mylist_selected(QListWidget):
    def __init__(self, parent, property_name: str, config_file: str):
        super(Mylist_selected, self).__init__(parent)
        self.config = None
        self.config_detailed = None
        self.rightmenu_curr = None
        # 数据名称，用于筛选拖拽数据类型
        self.property_name = property_name
        self.config_file = config_file

        self.read_config()

        # self.resize(400, 400)
        # 无边框
        # self.setFrameShape(QFrame.NoFrame)
        # 隐藏横向滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 不能编辑
        self.setEditTriggers(self.NoEditTriggers)
        # 开启拖功能
        self.setDragEnabled(True)
        # 只能往外拖
        self.setDragDropMode(self.DragOnly)
        # 忽略放
        self.setDefaultDropAction(Qt.IgnoreAction)
        # ****重要的一句（作用是可以单选，多选。Ctrl、Shift多选，可从空白位置框选）****
        # ****不能用ExtendedSelection,因为它可以在选中item后继续框选会和拖拽冲突****
        # self.setSelectionMode(self.ContiguousSelection)
        self.setSelectionMode(self.SingleSelection)
        # 设置从左到右、自动换行、依次排列
        self.setFlow(self.LeftToRight)
        self.setWrapping(True)
        self.setResizeMode(self.Adjust)
        # 设置滚轮
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        # item的间隔
        self.setSpacing(5)
        # 橡皮筋(用于框选效果)
        self._rubberPos = None
        self._rubberBand = QRubberBand(QRubberBand.Rectangle, self)

        self.initItems()

    def read_config(self):
        # '../../config/'
        with open('config/' + self.config_file + '.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        # '../../config/tools_buttons_'
        with open('config/tools_buttons_' + self.config_file.split('_')[-1] + '.json', 'r', encoding='utf-8') as f:
            self.config_detailed = json.load(f)

    def save_config(self):
        with open('config/' + self.config_file + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f)

    def initItems(self):
        size = QSize(47, 57)
        for mydata in self.config[self.config_file]:
            self.makeItem(size, mydata)

    # 重绘所有item
    def refresh(self):
        self.clear()
        # self.config[self.config_file].clear()
        self.read_config()
        self.initItems()

    # 实现拖拽的时候预览效果图
    # 这里演示拼接所有的item截图(也可以自己写算法实现堆叠效果)
    def startDrag(self, supportedActions):
        items = self.selectedItems()
        drag = QDrag(self)
        mimeData = self.mimeData(items)
        # 由于QMimeData只能设置image、urls、str、bytes等等不方便
        # 这里添加一个额外的属性直接把item放进去,后面可以根据item取出数据
        mimeData.setProperty(self.property_name, items)
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

    def mousePressEvent(self, event):
        # 列表框点击事件,用于设置框选工具的开始位置
        super(Mylist_selected, self).mousePressEvent(event)
        if event.buttons() != Qt.LeftButton or self.itemAt(event.pos()):
            return
        self._rubberPos = event.pos()
        self._rubberBand.setGeometry(QRect(self._rubberPos, QSize()))
        self._rubberBand.show()

    def mouseReleaseEvent(self, event):
        # 列表框点击释放事件,用于隐藏框选工具
        super(Mylist_selected, self).mouseReleaseEvent(event)
        self._rubberPos = None
        self._rubberBand.hide()

    def mouseMoveEvent(self, event):
        # 列表框鼠标移动事件,用于设置框选工具的矩形范围
        super(Mylist_selected, self).mouseMoveEvent(event)
        if self._rubberPos:
            pos = event.pos()
            lx, ly = self._rubberPos.x(), self._rubberPos.y()
            rx, ry = pos.x(), pos.y()
            size = QSize(abs(rx - lx), abs(ry - ly))
            self._rubberBand.setGeometry(
                QRect(QPoint(min(lx, rx), min(ly, ry)), size))

    def makeItem(self, size, mydata):
        try:
            item = QListWidgetItem(self)
            item.setData(Qt.UserRole + 1, mydata)  # 把颜色放进自定义的data里面
            item.setSizeHint(size)
            item.setData(0, mydata)
            # print(item.data(0))
            widget = QWidget(self)
            layout = QVBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            label = QLabel(widget)  # 自定义控件
            label.setMargin(2)  # 往内缩进2
            # label.resize(size)
            label_name = QLabel(widget)
            label_name.setText(mydata['name'])
            label_name.setMargin(2)
            label_name.setScaledContents(True)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setWordWrap(True)
            layout.addWidget(label)
            layout.addWidget(label_name)
            # pixmap = QPixmap(size.scaled(96, 96, Qt.IgnoreAspectRatio))  # 调整尺寸
            # pixmap.fill(QColor(0, 170, 255))
            # label.setPixmap(pixmap)
            object_name = mydata['button_num']
            if mydata['name'] != self.config_detailed[object_name]['name']:
                if self.config_file.split('_')[-1] != 'tool':
                    self.read_config()
                    print('按钮"%s"配置改变' % mydata['name'])
                else:
                    if mydata['name'] != self.config_detailed[object_name]['simple_name']:
                        self.read_config()
                        print('按钮"%s"配置改变' % mydata['name'])
            tips = self.config_detailed[object_name]
            if self.config_file.split('_')[-1] == 'tool':
                label_name.setText(mydata['name'] + '(' + str(mydata['command_num']) + ')')
                label.setToolTip('工具：'+tips['name'] + '(' + str(mydata['command_num']) + ')' + '\n命令：'+self.config_detailed[object_name]['command_template'][mydata['command_num']]+'\n介绍：'+tips['introduction'])
                label.setPixmap(QPixmap("resource/image/selected_tool.png"))
                # label.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                #                "selection-color: rgb(255, 0, 0);\n"
                #                "selection-background-color: rgb(255, 0, 255);")
            elif self.config_file.split('_')[-1] == 'tunnel':
                label.setToolTip('通道：'+tips['name']+'\n输入：'+str(len(tips['input']))+'个\n输出：'+str(len(tips['output']))+'个\n介绍：'+tips['introduction'])
                label.setPixmap(QPixmap("resource/image/selected_tunnel.png"))
                # label.setStyleSheet("background-color: rgb(170, 170, 255);")
            elif self.config_file.split('_')[-1] == 'component':
                label.setToolTip('配件：'+tips['name']+'\n介绍：'+tips['introduction'])
                label.setPixmap(QPixmap("resource/image/selected_component.png"))
                # label.setStyleSheet("background-color: rgb(255, 170, 0);")
            label.setScaledContents(True)
            label.setContextMenuPolicy(Qt.CustomContextMenu)
            label.customContextMenuRequested.connect(self.rightmenu_event)
            self.setItemWidget(item, widget)
            label.setProperty('item', self.indexFromItem(item))
        except Exception as e:
            print(e, 'Mylist_selected', 'makeItem selected')

    def rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().property('item').row()
            self.rightmenu = QMenu(self)
            # self.button_action_edit = QAction(QIcon('resource/image/edit.png'), u'编辑', self)
            self.button_action_delete = QAction(QIcon('resource/image/delete.png'), u'删除', self)
            # self.rightmenu.addAction(self.button_action_edit)
            self.rightmenu.addAction(self.button_action_delete)
            # self.button_action_edit.triggered.connect(self.button_action_edit_event)
            self.button_action_delete.triggered.connect(self.button_action_delete_event)

            self.rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'Mylist_selected', 'rightmenu')

    def button_action_delete_event(self):
        try:
            # print(self.rightmenu_curr)
            # print(self.config[self.config_file])
            self.itemWidget(self.item(self.rightmenu_curr)).deleteLater()
            self.config[self.config_file].pop(self.rightmenu_curr)
            self.takeItem(self.rightmenu_curr)
            self.save_config()
            self.refresh()
        except Exception as e:
            print(e, 'Mylist_selected', 'button_action_delete_event')
