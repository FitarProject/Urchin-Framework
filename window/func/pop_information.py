from PyQt5.QtWidgets import QWidget, QApplication, QDialog
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# 创建静态变量的装饰器，参考 https://www.jianshu.com/p/3ed1037b7c18
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


class TipUi(QDialog):
    def __init__(self, text: str, parent=None):
        # 设置ui
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # 设置定时器，用于动态调节窗口透明度
        self.timer = QTimer()
        # 设置气泡在屏幕上的位置，水平居中，垂直屏幕80%位置
        desktop = QApplication.desktop()
        self.setGeometry(QRect(int(desktop.width() / 2 - 75), int(desktop.height() * 0.8), 152, 50))
        # 显示的文本
        self.ui.pushButton.setText(text)
        # 设置隐藏标题栏、无边框、隐藏任务栏图标、始终置顶
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        # 设置窗口透明背景
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 窗口关闭自动退出，一定要加，否则无法退出
        self.setAttribute(Qt.WA_QuitOnClose, True)
        # 用来计数的参数
        self.windosAlpha = 0
        # 设置定时器25ms，1600ms记64个数
        self.timer.timeout.connect(self.hide_windows)
        self.timer.start(25)

    # 槽函数
    def hide_windows(self):
        self.timer.start(25)
        # 前750ms设置透明度不变，后850ms透明度线性变化
        if self.windosAlpha <= 30:
            self.setWindowOpacity(1.0)
        else:
            self.setWindowOpacity(1.882 - 0.0294 * self.windosAlpha)
        self.windosAlpha += 1
        # 差不多3秒自动退出
        if self.windosAlpha >= 63:
            self.close()

    # 静态方法创建气泡提示
    # @staticmethod
    @static_vars(tip=None)
    def show_tip(text):
        TipUi.show_tip.tip = TipUi(text)
        TipUi.show_tip.tip.show()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(150, 54)
        Dialog.setStyleSheet("background: transparent;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setAutoFillBackground(False)
        # 在这里设置气泡的stylesheet
        self.pushButton.setStyleSheet("background-color:rgb(250, 255, 213);\n"
                                      "border-style:none;\n"
                                      "padding:8px;\n"
                                      "border-radius:25px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "提示框"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TipUi.show_tip('复制成功')
    sys.exit(app.exec_())
