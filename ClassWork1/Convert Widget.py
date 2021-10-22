import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy

EXCHANGE_RATES = {
    'Рубль': 1,
    'Доллар': 70,
    'Евро': 80,
    'Турбик': 30
}


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        # Окно
        self.setWindowTitle('Конвертор валют')

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)
        # Строка для ввода
        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Кнопка с выпадающим списком
        self.input_type = QComboBox(self)
        self.input_type.addItems(EXCHANGE_RATES.keys())
        self.input_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #
        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.clicked.connect(self.convert)
        self.convert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_type = QComboBox(self)
        self.output_type.addItems(EXCHANGE_RATES.keys())
        self.output_type.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_button)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
