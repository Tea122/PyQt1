import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QLCDNumber, QLabel, QRadioButton


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Крестики-нолики')
        self.setFixedSize(400, 400)

        # ------------------------------------------------------
        self.radiobutton_X = QRadioButton('x', self)
        self.radiobutton_X.toggled.connect(self.conv)
        self.radiobutton_X.resize(20, 30)
        self.radiobutton_X.move(50, 50)

        self.radiobutton_0 = QRadioButton('x', self)
        self.radiobutton_0.toggled.connect(self.conv)
        self.radiobutton_0.resize(20, 30)
        self.radiobutton_0.move(50, 50)
        # --------------------------------------------------------

        self.buttons = []
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                self.buttons[i].append(QPushButton(self))
                self.buttons[i][j].resize(100, 100)
                self.buttons[i][j].move(110 * (i + 1), 110 * (i +0 1))
                self.buttons[i][j].setText('')
                self.buttons[i][j].clicked.connect(self.conv)

    def conv(self):
        if self.radiobutton_0:
            print('df')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
