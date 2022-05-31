from PyQt5.Qt import *
import json, re, requests

from window.ui.community_window import Ui_community_window
from window.func.community_crawler import Community_spider
from window.paint.button_record import Button_list
from window.func.pop_information import TipUi


class Community(QWidget, Ui_community_window):
    def __init__(self):
        super().__init__()
        self.config_dict = {}
        self.community_button = {}
        self.dict_to_button = {}
        self.server_ip = '8.131.57.209'
        self.server_port = '5555'
        self.server = Community_spider(self, self.server_ip, self.server_port)
        self.button_list = Button_list(10, 10, 90, 90, 80, 80, 560, 5800)

        # self.setupUi(self)

    def setupUi(self, community_window):
        try:
            super().setupUi(community_window)
            with open('qss/community_window.qss', 'r', encoding='UTF-8') as f:
                self.widget.setStyleSheet(f.read())
            with open('qss/community_frame.qss', 'r', encoding='UTF-8') as f:
                self.scrollArea.setStyleSheet(f.read())
            self.share_func.hide()
            self.share_tool.hide()
            self.share_command.hide()
            self.share_part.hide()
            self.init_list()
            self.label_addr.setText('addr：  ' + self.server.url)
            self.button_change_server.clicked.connect(self.button_change_server_event)
            self.button_refresh.clicked.connect(self.button_refresh_event)
            self.share_tunnel.clicked.connect(self.share_tunnel_event)
        except Exception as e:
            print(e, 'Community', 'setupUi')

    def init_list(self):
        try:
            self.button_list.clear()
            for widget_name in self.community_button.keys():
                self.community_button[widget_name].deleteLater()
            self.config_dict = self.server.get_list()
            if isinstance(self.config_dict, dict):
                self.label_status.setText('状态：正常')
                for widget_name in self.config_dict.keys():
                    widget_config = json.loads(self.config_dict[widget_name])
                    x, y, width, height = self.button_list.add_button(widget_name)
                    self.community_button[widget_name] = QPushButton(self.button_list_widget)
                    self.community_button[widget_name].setGeometry(QRect(x, y, width, height))
                    self.community_button[widget_name].setObjectName(widget_name)
                    button_name = ''
                    tmp = re.findall('.{'+str(12)+'}', widget_name)
                    tmp.append(widget_name[(len(tmp) * 12):])
                    for i in tmp:
                        button_name += i + '\n'
                    self.community_button[widget_name].setText(button_name.rstrip('\n'))
                    if 'widget_introduction' in widget_config.keys():
                        self.community_button[widget_name].setToolTip('名称：' + widget_name + '\n说明：' + widget_config['widget_introduction'])
                    else:
                        self.community_button[widget_name].setToolTip('名称：' + widget_name + '\n说明：无')
                    self.community_button[widget_name].setVisible(True)
                    # 右键菜单
                    self.community_button[widget_name].setContextMenuPolicy(Qt.CustomContextMenu)
                    self.community_button[widget_name].clicked.connect(self.community_buttons_clicked_event)
                    self.community_button[widget_name].customContextMenuRequested.connect(self.button_rightmenu_event)
            else:
                self.label_status.setText('状态：异常')
        except Exception as e:
            print(e, 'Community', 'init_list')

    def community_buttons_clicked_event(self):
        pass

    def button_rightmenu_event(self):
        try:
            self.rightmenu_curr = self.sender().objectName()
            self.button_rightmenu = QMenu(self)
            self.button_action_download = QAction(QIcon('resource/image/download.png'), u'下载', self)
            self.button_rightmenu.addAction(self.button_action_download)
            self.button_action_download.triggered.connect(self.button_action_download_event)

            self.button_rightmenu.popup(QCursor.pos())
        except Exception as e:
            print(e, 'Community', 'button_rightmenu_event')

    def button_action_download_event(self):
        try:
            result = self.server.download_file(self.rightmenu_curr)
            if result:
                config = json.loads(result)
                # del config['widget_introduction']
                with open('logs/tmp/' + self.rightmenu_curr + '.json', 'w', encoding='utf-8') as f:
                    json.dump(config, f)
                TipUi.show_tip('保存成功!')
                print('已保存到：.logs/tmp/' + self.rightmenu_curr + '.json')
            else:
                print('下载失败！')
        except Exception as e:
            print(e, 'Community', 'button_rightmenu_event')

    def button_change_server_event(self):
        QMessageBox.warning(self, "操作确认", '暂不支持该功能', QMessageBox.Ok)

    def button_refresh_event(self):
        self.init_list()

    def share_tunnel_event(self):
        pass