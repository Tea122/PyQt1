import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLCDNumber, QLabel


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Миникалькулятор')
        self.setFixedSize(500, 150)

        # ------------------------------------------------------------
        self.input_value_up = QLineEdit(self)
        self.input_value_up.resize(100, 20)
        self.input_value_up.move(50, 50)

        self.input_value_down = QLineEdit(self)
        self.input_value_down.setGeometry(70, 70, 50, 50)
        self.input_value_down.setSizePolicy(55, 20)
        # ------------------------------------------------------------
        self.output_value_sum = QLCDNumber(self)
        self.output_value_sum.setDigitCount(5)
        self.output_value_sum.setGeometry(70, 70, 50, 50)
        self.output_value_sum.setSizePolicy(80, 20)

        self.output_value_sum_t = QLabel('Первое число(целое):', self)
        self.output_value_sum_t.setGeometry(70, 70, 50, 50)
        self.output_value_sum_t.setSizePolicy(105, 50)

        self.output_value_sum_t.setBuddy(self.output_value_sum)
        # self.phoneEdit = QLineEdit(self)
        # self.phoneLabel = QLabel("&Phone:", self)
        # self.phoneLabel.setBuddy(self.phoneEdit)

        # -------

        self.output_value_razn = QLCDNumber(self)
        self.output_value_razn.setDigitCount(5)
        self.output_value_razn.setGeometry(70, 70, 50, 50)
        self.output_value_razn.setSizePolicy(130, 20)

        self.output_value_proizv = QLCDNumber(self)
        self.output_value_proizv.setDigitCount(5)
        self.output_value_proizv.setGeometry(370, 70, 50, 50)
        self.output_value_proizv.setSizePolicy(155, 20)

        self.output_value_chast = QLCDNumber(self)
        self.output_value_chast.setDigitCount(5)
        self.output_value_chast.setGeometry(70, 70, 50, 50)
        self.output_value_chast.setSizePolicy(180, 20)
        # ------------------------------------------------------------
        self.button = QPushButton(self)
        self.button.clicked.connect(self.calk)
        self.button.setGeometry(100, 100, 100, 100)
        self.button.setSizePolicy(500, 105)

    # ------------------------------------------------------------

    def calk(self):
        first = self.input_value_up.text()
        second = self.input_value_down.text()
        self.output_value_sum.setText(str(first + second))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
