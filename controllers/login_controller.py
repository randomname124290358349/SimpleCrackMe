from PySide6.QtCore import QObject


class LoginController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view

        # Conecta sinais
        self.view.login_requested.connect(self.process_login)

    def process_login(self, username, password):
        if not username or not password:
            self.view.show_error("Please, fill all the fields")
            return False

        success = self.model.authenticate(username, password)
        if not success:
            self.view.show_error("Wrong pass or user")
            return False

        # Show success message and user info
        user_info = self.model.get_current_user_info()
        self.view.show_success(user_info)

        return True

    def logout(self):
        self.model.logout()
        self.view.clear_fields()