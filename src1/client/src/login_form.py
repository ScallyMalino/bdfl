import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from client.ui.ui_login_form import Ui_MainWindow as Ui_LoginForm
from client.src.main_form import MainForm
from client.src.base_worker import BaseWorker, Login, User
from Server.db_manager import base_manager

class LoginForm(QMainWindow, Ui_LoginForm):

    login_correct = pyqtSignal(int, int)
    main_window: QMainWindow


    def __init__(self, base_worker: BaseWorker):
        super().__init__()
        self.base_worker = base_worker

        self.setupUi(self)
        self.button_enter.clicked.connect(self.check_login)
        self.push_cancel.clicked.connect(self.exit)

    def check_login(self):
        user = User(Email=self.line_login.text(), password=self.line_password.text())
        if LoginForm.check_user_credentials:
            self.start_main_window(user)
        else:
            self.lbl_error.setVisible(True)

    def start_main_window(self, login: Login):
        if login.Role == 1:
            self.main_window = MainForm(self.base_worker, login)
        else:
            self.main_window = MainForm(self.base_worker, login)
        self.main_window.show()
        self.close()
    def exit(self):
        self.close()

    def check_user_credentials(self, user: "User") -> bool:
        res = base_manager.execute("SELECT COUNT(*) FROM users WHERE Email = ? AND Password = ?",
                                   args=(user.Email, user.password), many=False)

        return res['data'][0] == 1

