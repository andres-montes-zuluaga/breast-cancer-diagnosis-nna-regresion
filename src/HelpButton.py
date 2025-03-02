from PyQt5.QtWidgets import (QPushButton, QMessageBox)

class HelpButton(QPushButton):
    def __init__(self, help_text, parent=None):
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
        QMessageBox.information(self, "Ayuda", self.help_text)