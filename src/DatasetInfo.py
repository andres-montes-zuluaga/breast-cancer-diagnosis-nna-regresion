from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit)

class DatasetInfo(QWidget):
    """
    Class to display information about the breast cancer dataset.

    This class creates a graphical interface that shows general information and
    features of the Wisconsin breast cancer dataset (diagnosis).
    """
    def __init__(self, breast_cancer):
        """
        Initializes the dataset information interface.

        Parameters:
        - breast_cancer: Object containing the breast cancer dataset.
        """
        super().__init__()
        layout = QVBoxLayout(self)
        
        title = QLabel("Dataset Information")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)
        
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setStyleSheet("""
            QTextEdit {
                font-family: Arial;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)

        dataset_info = f"""
WISCONSIN BREAST CANCER DATASET (DIAGNOSIS)
===========================================

General Information:
--------------------
- Total number of samples: {breast_cancer.data.shape[0]}
- Number of features: {breast_cancer.data.shape[1]}
- Classes: {', '.join(breast_cancer.target_names)}

Description:
------------
This dataset contains features computed from digitized images
of fine needle aspirates (FNA) of breast masses. These features
describe the characteristics of the cell nuclei present in the images.

Features used in the analysis:
------------------------------
The features are grouped into three main categories, and for each feature,
the mean, standard error, and "worst" value (mean of the three largest values) are calculated:

1. RADIUS: Mean distance from center to points on the perimeter
2. TEXTURE: Standard deviation of gray-scale values
3. PERIMETER: Size of the core nucleus
4. AREA: Area of the core nucleus
5. SMOOTHNESS: Local variation in radius lengths
6. COMPACTNESS: (perimeter² / area - 1.0)
7. CONCAVITY: Severity of concave portions of the contour
8. CONCAVE POINTS: Number of concave portions of the contour
9. SYMMETRY: Symmetry of the nucleus
10. FRACTAL DIMENSION: "Coastline approximation" - 1

Complete list of measured features (30 in total):"""
       
        info_text.setText(dataset_info)
        layout.addWidget(info_text)

        
        features_table = QTextEdit()
        features_table.setReadOnly(True)
        features_table.setStyleSheet("""
            QTextEdit {
                font-family: Courier;
                font-size: 12px;
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
            }
        """)
        layout.addWidget(features_table)