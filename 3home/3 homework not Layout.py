import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLCDNumber, QLabel


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Миникалькулятор')
        self.setFixedSize(500, 150)

        # ------------------------Размер и положение готово------------------------------------
        self.input_value_up = QLineEdit(self)
        self.input_value_up.resize(100, 22)
        self.input_value_up.move(50, 30)

        self.input_value_up_t = QLabel('Первое число(целое):', self)
        self.input_value_up_t.setBuddy(self.input_value_up)
        self.input_value_up_t.move(52, 17)

        self.input_value_down = QLineEdit(self)
        self.input_value_down.resize(100, 22)
        self.input_value_down.move(50, 85)

        self.input_value_down_t = QLabel('Второе число(целое):', self)
        self.input_value_down_t.setBuddy(self.input_value_down)
        self.input_value_down_t.move(52, 71)

        # -----------------------Размер и положение готов------------------------------
        self.button = QPushButton(self)
        self.button.setText('->')
        self.button.clicked.connect(self.calk)
        self.button.resize(75, 22)
        self.button.move(175, 50)
        # ------------------------------
        self.output_value_summ = QLCDNumber(self)
        self.output_value_summ.setDigitCount(5)
        self.output_value_summ.resize(100, 20)
        self.output_value_summ.move(370, 25)

        self.input_value_summ_t = QLabel('Сумма:', self)
        self.input_value_summ_t.setBuddy(self.output_value_summ)
        self.input_value_summ_t.move(320, 30)

        # self.phoneEdit = QLineEdit(self)
        # self.phoneLabel = QLabel("&Phone:", self)
        # self.phoneLabel.setBuddy(self.phoneEdit)

        # -------

        # self.output_value_razn = QLCDNumber(self)
        # self.output_value_razn.setDigitCount(5)
        # self.output_value_razn.resize(150, 20)
        # self.output_value_razn.move(120, 100)

        # self.output_value_proizv = QLCDNumber(self)
        # self.output_value_proizv.setDigitCount(5)
        # self.output_value_proizv.resize(140, 20)
        # self.output_value_proizv.move(140, 100)

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
