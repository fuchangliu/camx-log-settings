from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class CamX:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('camx-log-setting.ui')

        # 设置UI标题
        self.ui.setWindowTitle('CamX Log Settings')




app = QApplication([])
camx = CamX()
camx.ui.show()
app.exec_()
