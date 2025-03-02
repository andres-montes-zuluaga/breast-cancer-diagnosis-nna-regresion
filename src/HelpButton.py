from PyQt5.QtWidgets import (QPushButton, QMessageBox)

class HelpButton(QPushButton):
    """
    Class to create a help button that shows an informative message.

    This class inherits from QPushButton and displays a message box with help text
    when the button is clicked.
    """
    def __init__(self, help_text, parent=None):
        """
        Initializes the help button.

        Parameters:
        - help_text (str): Help text to be displayed in the message box.
        - parent (QWidget, optional): Parent widget of the button.
        """
        super().__init__("?", parent)
        self.help_text = help_text
        self.setFixedSize(20, 20)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.clicked.connect(self.show_help)

    def show_help(self):
        """
        Displays a message box with the help text.
        """
        QMessageBox.information(self, "Help", self.help_text)