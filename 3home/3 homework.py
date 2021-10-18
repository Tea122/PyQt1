import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Миникалькулятор')

        self.input_value_up = QLineEdit(self)

        self.input_value_down = QLineEdit(self)

        self.output_value_sum = QLineEdit(self)

        self.output_value_razn = QLineEdit(self)

        self.output_value_proizv = QLineEdit(self)

        self.output_value_chast = QLineEdit(self)

        self.button = QPushButton


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
