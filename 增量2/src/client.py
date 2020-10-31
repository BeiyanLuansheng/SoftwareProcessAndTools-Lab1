import network
import sys
from PyQt5.QtWidgets import QApplication
from written_board import WrittenBoard

app = QApplication(sys.argv)
board = WrittenBoard()  # 新建一个主界面
board.show()  # 显示主界面
sys.exit(app.exec_())  # 进入消息循环
