from PySide6.QtCore import QObject


class TestController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view

        self.view.test_controller_signal.connect(self.process_test)

    def process_test(self, true_or_false):
        self.view.show_test(f"The controller is well connected!! -> {true_or_false}")