from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt, Signal

from models.user_model import UserModel
from controllers.login_controller import LoginController
from controllers.test_controller import TestController


class MainWindow(QMainWindow):
    login_requested = Signal(str, str)
    test_controller_signal = Signal(bool)

    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("SimpleCrackMe")

        # Min Size
        self.setMinimumSize(400, 300)

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Header label
        header_label = QLabel("Login")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setStyleSheet("font-size: 50px; font-weight: bold; margin-bottom: 15px;")
        main_layout.addWidget(header_label)

        # Username field
        username_layout = QHBoxLayout()
        username_label = QLabel("User:")
        username_label.setFixedWidth(60)
        username_label.setStyleSheet("font-size: 15px;")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        main_layout.addLayout(username_layout)

        # Password field
        password_layout = QHBoxLayout()
        password_label = QLabel("Pass:")
        password_label.setFixedWidth(60)
        password_label.setStyleSheet("font-size: 15px;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        main_layout.addLayout(password_layout)

        # Login button
        login_button_layout = QHBoxLayout()
        login_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_button = QPushButton("Press to Login")
        self.login_button.setFixedWidth(150)
        self.login_button.setStyleSheet("font-weight: bold; padding: 15px;")
        self.login_button.clicked.connect(self._on_login_clicked)
        login_button_layout.addWidget(self.login_button)
        main_layout.addLayout(login_button_layout)

        # Test connector button
        test_button_layout = QHBoxLayout()
        test_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.test_button = QPushButton("Test Controller")
        self.test_button.setFixedWidth(150)
        self.test_button.setStyleSheet("font-weight: bold; padding: 15px;")
        self.test_button.clicked.connect(self._on_test_clicked)
        test_button_layout.addWidget(self.test_button)
        main_layout.addLayout(test_button_layout)

        # Add some vertical space
        main_layout.addStretch()

        # Import user model
        self.user_model = UserModel()

        # Initiate login controller
        self.login_controller = LoginController(self.user_model, self)

        # Initiate test controller
        self.test_controller = TestController(self)

    def _on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.login_requested.emit(username, password)

    def _on_test_clicked(self):
        self.test_controller_signal.emit(True)

    def clear_fields(self):
        self.username_input.clear()
        self.password_input.clear()
        self.username_input.setFocus()

    def show_error(self, message):
        QMessageBox.warning(self, "Error", message)

    def show_test(self, message):
        QMessageBox.information(self, "Test", message)

    def show_success(self, user_info):
        QMessageBox.information(self, "Success", f"Welcome {user_info['name']}!")