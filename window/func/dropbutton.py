from PyQt5.Qt import *


class DropButton(QLabel):
    refresh_tool = pyqtSignal(object)
    refresh_tunnel = pyqtSignal(object, bool)

    def __init__(self, parent, button_type: int):
        super().__init__(parent)
        self.type = button_type
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("background-color: rgb(225, 225, 225);")

    def dragEnterEvent(self, event):
        if event.mimeData().property('mytool') or event.mimeData().property('mycomponent') or event.mimeData().property('mytunnel'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if self.type == 0:
                if event.mimeData().property('mytool'):
                    items = event.mimeData().property('mytool')
                    event.accept()
                    object_name = items[0].data(0)['button_num']
                    data = self.property('data')
                    data['button_num'] = object_name
                    data['command_num'] = items[0].data(0)['command_num']
                    self.setProperty('data', data)
                    self.refresh_tool.emit(self)
                    # print(items[0].data(0))
                elif event.mimeData().property('mycomponent'):
                    items = event.mimeData().property('mycomponent')
                    event.accept()
                    component_list = self.property('data')['component']
                    component_list.append(items[0].data(0)['button_num'])
                    data = self.property('data')
                    data['component'] = component_list
                    self.setProperty('data', data)
                    self.refresh_tool.emit(self)
            elif self.type == 1:
                if event.mimeData().property('mytunnel'):
                    event.accept()
                    items = event.mimeData().property('mytunnel')
                    data = self.property('data')
                    data['tunnel'].append(items[0].data(0)['button_num'])
                    self.setProperty('data', data)
                    self.refresh_tunnel.emit(self, True)
        except Exception as e:
            print(e, 'dropEvent', 'DropButton')
        # self.setText(event.mimeData().text())
        # print(event.mimeData().property('mytool'))