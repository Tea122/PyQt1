import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Вычисление выражений')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)

        self.button = QPushButton(self)
        self.button.setText('->')
        self.button.clicked.connect(self.calculations)

        self.output_value = QLineEdit(self)
        self.output_value.setText('')

        self.input_layout.addWidget(self.input_value)

        self.output_layout.addWidget(self.output_value)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.button)
        self.main_layout.addLayout(self.output_layout)

    def calculations(self):
        input = self.input_value.text()
        znach = eval(input)
        self.output_value.setText(str(znach))  # Написано str(zhach) потому что он не воспринимает числа как int().
                                               # Не знаю почему это так, но путь к решению я нашел именно такой.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
