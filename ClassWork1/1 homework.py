import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        # Окно
        self.setWindowTitle('Фокус со словами')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)
        # Строка для ввода
        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #
        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value)

        self.output_layout.addWidget(self.output_value)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_button)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        output = self.convert_button.text()
        if output == '->':
            inp = self.input_value.text()
            self.output_value.setText(inp)
            self.input_value.setText('')
            self.convert_button.setText('<-')

        else:
            impu = self.output_value.text()
            self.input_value.setText(impu)
            self.output_value.setText('')
            self.convert_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
