import sys
from main import run
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore


class MainInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.number = None

    def init_ui(self):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(330, 285)
        self.setWindowTitle('spmr')

        self.phonenumber_line = QLineEdit(self)
        self.phonenumber_line.setGeometry(10, 30, 200, 20)
        self.phonenumber_line.setMaxLength(12)
        self.phonenumber_line.setPlaceholderText("Phone number")
        self.button_input = QPushButton('Run', self)
        self.button_input.setGeometry(220, 30, 100, 20)
        self.button_input.clicked.connect(self.on_push_button)

        self.checkbox_sms = QCheckBox('SMS', self)
        self.checkbox_sms.setGeometry(10, 60, 200, 20)
        self.checkbox_sms.setChecked(True)
        self.checkbox_calls = QCheckBox('CALLS', self)
        self.checkbox_calls.setGeometry(55, 60, 200, 20)
        self.checkbox_calls.setChecked(True)

        self.show()

    def get_number(self):
        """
        Get correct number
        :return: string number
        """
        number = self.phonenumber_line.text()
        if len(number) < 10:
            return ''

        while len(number) != 10:
            number = number[1:]

        return number

    @pyqtSlot()
    def on_push_button(self):
        self.number = self.get_number()
        run(self.number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = MainInterface()
    sys.exit(app.exec_())
