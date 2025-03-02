"""
Este módulo inicializa el paquete y realiza las importaciones necesarias para el diagnóstico de cáncer de mama utilizando una red neuronal artificial (ANN) con regresión.

Importaciones:
- DatasetInfo: Clase para manejar la información del conjunto de datos.
- HelpButton: Clase para crear un botón de ayuda en la interfaz de usuario.
- load_and_prepare_data: Función para cargar y preparar los datos para el modelo.
- build_ann: Función para construir la red neuronal artificial.
- ResultsWindow: Clase para mostrar los resultados en una ventana.
"""

from .DatasetInfo import DatasetInfo
from .HelpButton import HelpButton
from .load_and_prepare_data import load_and_prepare_data
from .build_ann import build_ann
from .ResultsWindow import ResultsWindow