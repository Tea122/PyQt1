import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QLCDNumber, QLabel


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Арифмометр')
        self.setFixedSize(340, 100)

        self.first_input = QLineEdit(self)
        self.first_input.resize(60, 30)
        self.first_input.move(30, 30)

        self.button_summ = QPushButton(self)
        self.button_summ.setText('+')
        self.button_summ.clicked.connect(self.convertor_summ)
        self.button_summ.resize(30, 30)
        self.button_summ.move(90, 30)

        self.button_razn = QPushButton(self)
        self.button_razn.setText('-')
        self.button_razn.clicked.connect(self.convertor_razn)
        self.button_razn.resize(30, 30)
        self.button_razn.move(120, 30)

        self.button_proizv = QPushButton(self)
        self.button_proizv.setText('*')
        self.button_proizv.clicked.connect(self.convertor_proizv)
        self.button_proizv.resize(30, 30)
        self.button_proizv.move(150, 30)

        self.second_input = QLineEdit(self)
        self.second_input.resize(60, 30)
        self.second_input.move(180, 30)

        self.input_text = QLabel(self)
        self.input_text.setText('=')
        self.input_text.resize(60, 30)
        self.input_text.move(241, 30)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.resize(60, 30)
        self.output_value.move(250, 30)

    def convertor_summ(self):
        first = int(self.first_input.text())
        second = int(self.second_input.text())
        self.output_value.setText(str(first + second))

    def convertor_razn(self):
        first = int(self.first_input.text())
        second = int(self.second_input.text())
        self.output_value.setText(str(first - second))

    def convertor_proizv(self):
        first = int(self.first_input.text())
        second = int(self.second_input.text())
        self.output_value.setText(str(first * second))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
