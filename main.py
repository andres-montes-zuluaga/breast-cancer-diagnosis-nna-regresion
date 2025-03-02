import sys
from src.load_and_prepare_data import load_and_prepare_data
from src.build_ann import build_ann
from src.ResultsWindow import ResultsWindow
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from PyQt5.QtWidgets import QApplication

def main():
    """
    Main function that runs the complete workflow of the breast cancer diagnosis project.

    This function performs the following tasks:
    1. Loads and prepares the data.
    2. Builds and trains the artificial neural network (ANN).
    3. Makes predictions on the test set.
    4. Calculates accuracy and classification report.
    5. Displays the results in a graphical window.
    """
    # Load and prepare the data
    X_train, X_test, y_train, y_test, df, breast_cancer = load_and_prepare_data()
    
    # Build and train the neural network
    model = build_ann(X_train.shape[1])
    model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=1)
    
    # Make predictions
    y_pred_prob = model.predict(X_test)
    # Convert predicted probabilities to binary labels (0 or 1)
    # If the probability is greater than 0.5, classify as 1 (positive), otherwise as 0 (negative)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    # Calculate accuracy and classification report
    accuracy = accuracy_score(y_test, y_pred)
    # Generate a detailed classification report including precision, recall, and F1-score for each class
    classification_rep = classification_report(y_test, y_pred, target_names=['Malignant', 'Benign'])
    
    # Create the application and display the results window
    app = QApplication(sys.argv)
    # Initialize the results window with true labels, predicted labels, accuracy, and classification report
    window = ResultsWindow(y_test, y_pred, accuracy, classification_rep, breast_cancer)
    window.show()
    # Run the main application loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()