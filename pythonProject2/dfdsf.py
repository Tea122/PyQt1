import sys

import self as self
from PyQt5.QtWidgets import QLabel, QFrame, QApplication


class Windows(self):
    def __init__(self):
        super(Windows, self).__init__()
        self.setWindowTitle('Миникалькулятор')

        label = QLabel(self)
        label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label.setText("first line\nsecond line")
        label.setAlignment(Qt.AlignBottom, )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Windows()
    wnd.show()
    sys.exit(app.exec())
