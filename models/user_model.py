from random import choice

class UserModel:
    def __init__(self):
        ascii_letters_and_numbers = [_ for _ in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890']
        random_user = "".join([choice(ascii_letters_and_numbers) for _ in range(10)])
        random_pass = "".join([choice(ascii_letters_and_numbers) for _ in range(10)])
        self.users = {
            random_user: {"password": random_pass, "name": "Admin", "role": "admin"},
        }
        self.current_user = None

    def authenticate(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            return True
        return False

    def get_current_user_info(self):
        if self.current_user:
            user_info = self.users[self.current_user].copy()
            user_info["username"] = self.current_user
            del user_info["password"]
            return user_info
        return None

    def logout(self):
        self.current_user = None