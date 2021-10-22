import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLCDNumber, QLabel


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Миникалькулятор')
        self.setFixedSize(500, 130)

        # ------------------------Размер и положение готово----------------------------
        self.input_value_up = QLineEdit(self)
        self.input_value_up.resize(100, 25)
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
        # ------------------------Размер и положение готов-----------------------------
        self.output_value_summ = QLCDNumber(self)
        self.output_value_summ.resize(100, 25)
        self.output_value_summ.move(370, 15)

        self.output_value_summ_t = QLabel('Сумма:', self)
        self.output_value_summ_t.setBuddy(self.output_value_summ)
        self.output_value_summ_t.move(320, 20)

        # ------------------Размер и положение готов-----------------------------------

        self.output_value_razn = QLCDNumber(self)
        self.output_value_razn.resize(100, 25)
        self.output_value_razn.move(370, 41)

        self.output_value_razn_t = QLabel('Разность:', self)
        self.output_value_razn_t.setBuddy(self.output_value_razn)
        self.output_value_razn_t.move(305, 45)

        # --------------------------Размер и положение готов---------------------------

        self.output_value_proizv = QLCDNumber(self)
        self.output_value_proizv.resize(100, 25)
        self.output_value_proizv.move(370, 67)

        self.output_value_proizv_t = QLabel('Произведение:', self)
        self.output_value_proizv_t.setBuddy(self.output_value_razn)
        self.output_value_proizv_t.move(278, 72)

        # ---------------------------Размер и положение готов---------------------------------

        self.output_value_chast = QLCDNumber(self)
        self.output_value_chast.resize(100, 25)
        self.output_value_chast.move(370, 93)

        self.output_value_chast_t = QLabel('Частное:', self)
        self.output_value_chast_t.move(309, 99)

    def calk(self):
        first = self.input_value_up.text()
        second = self.input_value_down.text()
        # print(type(first), type(second))
        self.output_value_summ.display(int(first) + int(second))
        self.output_value_razn.display(int(first) - int(second))
        self.output_value_proizv.display(int(first) * int(second))
        if int(second) == 0:
            self.output_value_chast.display('Error')
        else:
            self.output_value_chast.display(int(first) / int(second))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
