from PyQt5.QtWidgets import (QPushButton, QMessageBox)

class HelpButton(QPushButton):
    """
    Clase para crear un botón de ayuda que muestra un mensaje informativo.

    Esta clase hereda de QPushButton y muestra un cuadro de mensaje con texto de ayuda
    cuando se hace clic en el botón.
    """
    def __init__(self, help_text, parent=None):
        """
        Inicializa el botón de ayuda.

        Parámetros:
        - help_text (str): Texto de ayuda que se mostrará en el cuadro de mensaje.
        - parent (QWidget, opcional): Widget padre del botón.
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
        Muestra un cuadro de mensaje con el texto de ayuda.
        """
        QMessageBox.information(self, "Ayuda", self.help_text)