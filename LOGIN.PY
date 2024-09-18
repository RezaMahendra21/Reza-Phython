import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simple Login Form")
        self.resize(500, 120)

        # set layout
        layout = QGridLayout()

        # set layout display for username
        label_name = QLabel('<font size="4"> Username: ')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Masukan Username: ")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # set layout display for password
        label_password = QLabel('<font size="4"> Password: ')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Masukan Password: ")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # set button login
        button_login = QPushButton('Login')
        button_login.clicked.connect(self.password_checker)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    # password valudator
    def password_checker(self):
        message = QMessageBox()

        if self.lineEdit_username.text() == "pesonainformatika" and self.lineEdit_password.text() == "secret":
            message.setText("Berhasil Login")
            message.exec_()
            app.quit()

        else:
            message.setText("Password anda salah")
            message.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())