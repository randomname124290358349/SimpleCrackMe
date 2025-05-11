import sys
import os
import traceback

from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtGui import QIcon

from views.main_window import MainWindow


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and PyInstaller
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Handler for unhandled exceptions
def exception_hook(exctype, value, tb):
    """
    Captures unhandled exceptions to prevent the application from closing silently
    """
    traceback_str = ''.join(traceback.format_exception(exctype, value, tb))

    # Show a message to the user
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText("An unexpected error occurred")
    msg.setInformativeText(str(value))
    msg.setDetailedText(traceback_str)
    msg.setWindowTitle("Error")
    msg.exec()

    # Call the default handler to maintain normal error logging behavior
    sys.__excepthook__(exctype, value, tb)


def main():
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    app.setApplicationName("SimpleCrackMe")
    app.setStyle("Fusion")

    icon_path = resource_path("resources/icons/icon.ico")
    app_icon = QIcon(icon_path)
    app.setWindowIcon(app_icon)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)