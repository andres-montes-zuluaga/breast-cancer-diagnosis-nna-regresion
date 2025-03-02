from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QTextEdit, QTabWidget)
from .HelpButton import HelpButton
from .DatasetInfo import DatasetInfo
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

class ResultsWindow(QMainWindow):
    """
    Class to display the breast cancer analysis results.

    This class creates a main window that shows the model results,
    including accuracy, classification report, and confusion matrix.
    It also provides a tab with dataset information.
    """
    def __init__(self, y_test, y_pred, accuracy, classification_rep, breast_cancer):
        """
        Initializes the results window.

        Parameters:
        - y_test (ndarray): True labels of the test set.
        - y_pred (ndarray): Predicted labels by the model.
        - accuracy (float): Model accuracy.
        - classification_rep (str): Model classification report.
        - breast_cancer (Bunch): Original breast cancer dataset object.
        """
        super().__init__()
        self.setup_ui(y_test, y_pred, accuracy, classification_rep, breast_cancer)
        
    def setup_ui(self, y_test, y_pred, accuracy, classification_rep, breast_cancer):
        """
        Sets up the user interface of the results window.

        Parameters:
        - y_test (ndarray): True labels of the test set.
        - y_pred (ndarray): Predicted labels by the model.
        - accuracy (float): Model accuracy.
        - classification_rep (str): Model classification report.
        - breast_cancer (Bunch): Original breast cancer dataset object.
        """
        self.setWindowTitle("Breast Cancer Analysis")
        self.setGeometry(100, 100, 1200, 600)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        tabs = QTabWidget()
        
        results_tab = QWidget()
        results_layout = QHBoxLayout(results_tab)
        
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        title_layout = QHBoxLayout()
        title = QLabel("Analysis Results")
        title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        title_layout.addWidget(title)
        
        help_btn = HelpButton(
            "This panel shows the analysis results:\n"
            "- Accuracy: Percentage of correct predictions\n"
            "- Classification report: Detailed metrics per class"
        )
        title_layout.addWidget(help_btn)
        title_layout.addStretch()
        
        left_layout.addLayout(title_layout)

        text_results = QTextEdit()
        text_results.setReadOnly(True)
        text_results.setStyleSheet("""
            QTextEdit {
                font-family: Courier;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)
        
        results_text = f"""Model results:
Accuracy: {accuracy:.2%}

Classification report:
{classification_rep}
"""
        text_results.setText(results_text)
        left_layout.addWidget(text_results)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        matrix_title = QLabel("Confusion Matrix")
        matrix_title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        right_layout.addWidget(matrix_title)

        fig = Figure(figsize=(8, 6))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Malignant', 'Benign'],
                    yticklabels=['Malignant', 'Benign'],
                    ax=ax)
        ax.set_title('Confusion Matrix')
        ax.set_ylabel('True')
        ax.set_xlabel('Predicted')
        
        right_layout.addWidget(canvas)

        results_layout.addWidget(left_panel, 40)
        results_layout.addWidget(right_panel, 60)

        tabs.addTab(results_tab, "Results")
        tabs.addTab(DatasetInfo(breast_cancer), "Dataset Information")
        
        main_layout.addWidget(tabs)

        self.statusBar().showMessage("Analysis completed successfully")

        self.setStyleSheet("""
            QMainWindow {background: #f0f0f0;}
        """)