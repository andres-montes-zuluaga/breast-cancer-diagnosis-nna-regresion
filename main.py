import sys
from src.load_and_prepare_data import load_and_prepare_data
from src.build_ann import build_ann
from src.ResultsWindow import ResultsWindow
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from PyQt5.QtWidgets import QApplication
                             
def main():
    X_train, X_test, y_train, y_test, df, breast_cancer = load_and_prepare_data()
    
    model = build_ann(X_train.shape[1])
    model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=1)
    
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred, target_names=['Maligno', 'Benigno'])
    
    app = QApplication(sys.argv)
    window = ResultsWindow(y_test, y_pred, accuracy, classification_rep, breast_cancer)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()