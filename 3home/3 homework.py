import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QLCDNumber


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Миникалькулятор')

        self.main_layout = QHBoxLayout(self)

        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value_up = QLineEdit(self)
        self.input_value_up.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_value_down = QLineEdit(self)
        self.input_value_down.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value_sum = QLCDNumber(self)
        self.output_value_sum.setDigitCount(5)
        self.output_value_sum.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value_razn = QLCDNumber(self)
        self.output_value_razn.setDigitCount(5)
        self.output_value_razn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value_proizv = QLCDNumber(self)
        self.output_value_proizv.setDigitCount(5)
        self.output_value_proizv.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value_chast = QLCDNumber(self)
        self.output_value_chast.setDigitCount(5)
        self.output_value_chast.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button = QPushButton(self)
        self.button.clicked.connect(self.calk)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value_up)
        self.input_layout.addWidget(self.input_value_down)

        self.output_layout.addWidget(self.output_value_sum)
        self.output_layout.addWidget(self.output_value_chast)
        self.output_layout.addWidget(self.output_value_proizv)
        self.output_layout.addWidget(self.output_value_razn)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.button)
        self.main_layout.addLayout(self.output_layout)
        self.setLayout(self.main_layout)

    def calk(self):
        first = self.input_value_up.text()
        second = self.input_value_down.text()
        self.output_value_sum.setText(str(first + second))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
