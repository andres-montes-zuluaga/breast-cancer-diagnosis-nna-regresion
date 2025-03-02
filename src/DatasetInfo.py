from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit)

class DatasetInfo(QWidget):
    """
    Clase para mostrar la información del conjunto de datos de cáncer de mama.

    Esta clase crea una interfaz gráfica que muestra información general y 
    características del conjunto de datos de cáncer de mama de Wisconsin (diagnóstico).
    """
    def __init__(self, breast_cancer):
        """
        Inicializa la interfaz de información del conjunto de datos.

        Parámetros:
        - breast_cancer: Objeto que contiene el conjunto de datos de cáncer de mama.
        """
        super().__init__()
        layout = QVBoxLayout(self)
        
        title = QLabel("Información del Dataset")
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
CONJUNTO DE DATOS DE CÁNCER DE MAMA DE WISCONSIN (DIAGNÓSTICO)
===========================================================

Información General:
------------------
- Número total de muestras: {breast_cancer.data.shape[0]}
- Número de características: {breast_cancer.data.shape[1]}
- Clases: {', '.join(breast_cancer.target_names)}

Descripción:
-----------
Este conjunto de datos contiene características computadas a partir de imágenes 
digitales de aspirados con aguja fina (FNA) de masas mamarias. Estas características 
describen las características de los núcleos celulares presentes en las imágenes.

Características utilizadas en el análisis:
----------------------------------------
Las características se agrupan en tres categorías principales, y para cada característica 
se calcula la media, el error estándar y el "peor" valor (media de los tres valores más grandes):

1. RADIO: Distancia media desde el centro a los puntos del perímetro
2. TEXTURA: Desviación estándar de los valores de escala de grises
3. PERÍMETRO: Tamaño del contorno del núcleo
4. ÁREA: Área del núcleo
5. SUAVIDAD: Variación local en las longitudes del radio
6. COMPACIDAD: (perímetro² / área - 1.0)
7. CONCAVIDAD: Severidad de las porciones cóncavas del contorno
8. PUNTOS CÓNCAVOS: Número de porciones cóncavas del contorno
9. SIMETRÍA: Simetría del núcleo
10. DIMENSIÓN FRACTAL: "Aproximación al perímetro de la costa" - 1

Lista completa de características medidas (30 en total):"""
       
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