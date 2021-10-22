import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QLCDNumber, QLabel, QRadioButton


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Крестики-нолики')
        self.setFixedSize(400, 500)

        self.radiobutton = QRadioButton('dwewe',self)
        self.radiobutton.toggled.connect(self.conv)
        self.radiobutton.resize(20, 30)
        self.radiobutton.move(50, 50)

        self.first_button = QPushButton(self)
        self.first_button.setText('')

        self.second_button = QPushButton(self)

    def conv(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
