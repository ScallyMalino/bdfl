from PyQt6.QtCore import pyqtSignal
import sys
from PyQt6.QtWidgets import QMainWindow
from client.ui.ui_main_form import Ui_MainWindow as Ui_MainForm
from client.src.base_worker import BaseWorker, User, Login

class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker
        self.show()