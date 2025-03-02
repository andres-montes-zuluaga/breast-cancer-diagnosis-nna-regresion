import sys
from src.load_and_prepare_data import load_and_prepare_data
from src.build_ann import build_ann
from src.ResultsWindow import ResultsWindow
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from PyQt5.QtWidgets import QApplication

def main():
    """
    Función principal que ejecuta el flujo completo del proyecto de diagnóstico de cáncer de mama.

    Esta función realiza las siguientes tareas:
    1. Carga y prepara los datos.
    2. Construye y entrena la red neuronal artificial (ANN).
    3. Realiza predicciones en el conjunto de prueba.
    4. Calcula la precisión y el reporte de clasificación.
    5. Muestra los resultados en una ventana gráfica.
    """
    # Cargar y preparar los datos
    X_train, X_test, y_train, y_test, df, breast_cancer = load_and_prepare_data()
    
    # Construir y entrenar la red neuronal
    model = build_ann(X_train.shape[1])
    model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=1)
    
    # Realizar predicciones
    y_pred_prob = model.predict(X_test)
    # Convertir las probabilidades predichas en etiquetas binarias (0 o 1)
    # Si la probabilidad es mayor a 0.5, se clasifica como 1 (positivo), de lo contrario, como 0 (negativo)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    # Calcular precisión y reporte de clasificación
    accuracy = accuracy_score(y_test, y_pred)
    # Generar un reporte de clasificación detallado que incluye precisión, recall y F1-score para cada clase
    classification_rep = classification_report(y_test, y_pred, target_names=['Maligno', 'Benigno'])
    
    # Crear la aplicación y mostrar la ventana de resultados
    app = QApplication(sys.argv)
    # Inicializar la ventana de resultados con las etiquetas verdaderas, predichas, precisión y reporte de clasificación
    window = ResultsWindow(y_test, y_pred, accuracy, classification_rep, breast_cancer)
    window.show()
    # Ejecutar el bucle principal de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()