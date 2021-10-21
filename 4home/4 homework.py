import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QLCDNumber, QLabel, QCheckBox


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.setWindowTitle('Кью ЧекБокс')
        self.setFixedSize(250, 120)

        self.checkBox = QCheckBox(self)
        self.checkBox.move(30, 20)
        self.checkBox.resize(30, 20)
        self.checkBox.clicked.connect(self.checkboxm)

        self.checkBox_t = QLabel('1 edit', self)
        self.checkBox_t.move(50, 22)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.hide()
        self.lineEdit.setText('Кью лайн йедит адин')
        self.lineEdit.resize(130, 20)
        self.lineEdit.move(90, 20)

        self.checkBox2 = QCheckBox(self)
        self.checkBox2.clicked.connect(self.checkboxm)
        self.checkBox2.move(30, 40)
        self.checkBox2.resize(30, 20)

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.hide()
        self.lineEdit2.setText('Кью лайн йедит два')
        self.lineEdit2.resize(130, 20)
        self.lineEdit2.move(90, 37)

        self.checkBox2_t = QLabel('2 edit', self)
        self.checkBox2_t.move(50, 42)

        self.checkBox3 = QCheckBox(self)
        self.checkBox3.clicked.connect(self.checkboxm)
        self.checkBox3.move(30, 60)
        self.checkBox3.resize(30, 20)

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.hide()
        self.lineEdit3.setText('Кью лайн йедит три')
        self.lineEdit3.resize(130, 20)
        self.lineEdit3.move(90, 57)

        self.checkBox3_t = QLabel('3 edit', self)
        self.checkBox3_t.move(50, 62)

        self.checkBox4 = QCheckBox(self)
        self.checkBox4.clicked.connect(self.checkboxm)
        self.checkBox4.move(30, 80)
        self.checkBox4.resize(30, 20)

        self.lineEdit4 = QLineEdit(self)
        self.lineEdit4.hide()
        self.lineEdit4.setText('Кью лайн йедит читыри')
        self.lineEdit4.resize(130, 20)
        self.lineEdit4.move(90, 78)

        self.checkBox4_t = QLabel('4 edit', self)
        self.checkBox4_t.move(50, 82)

    def checkboxm(self):
        if self.checkBox.isChecked() == True:
            self.lineEdit.show()
        else:
            self.lineEdit.hide()

        if self.checkBox2.isChecked() == True:
            self.lineEdit2.show()
        elif self.checkBox2.isChecked() == False:
            self.lineEdit2.hide()

        if self.checkBox3.isChecked() == True:
            self.lineEdit3.show()
        elif self.checkBox3.isChecked() == False:
            self.lineEdit3.hide()

        if self.checkBox4.isChecked() == True:
            self.lineEdit4.show()
        elif self.checkBox4.isChecked() == False:
            self.lineEdit4.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ConvertWidget()
    wnd.show()
    sys.exit(app.exec())
