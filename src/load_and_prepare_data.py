from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_and_prepare_data():
    """
    Loads and prepares the breast cancer dataset.

    This function performs the following tasks:
    1. Loads the breast cancer dataset from sklearn.
    2. Separates the features (X) and labels (y).
    3. Converts the features into a pandas DataFrame.
    4. Splits the data into training and test sets.
    5. Scales the features using StandardScaler.

    Returns:
    - X_train_scaled (ndarray): Scaled training set.
    - X_test_scaled (ndarray): Scaled test set.
    - y_train (ndarray): Training set labels.
    - y_test (ndarray): Test set labels.
    - df (DataFrame): Pandas DataFrame with the original features.
    - breast_cancer (Bunch): Original breast cancer dataset object.
    """
    breast_cancer = load_breast_cancer()
    X = breast_cancer.data
    y = breast_cancer.target
    
    feature_names = breast_cancer.feature_names
    df = pd.DataFrame(X, columns=feature_names)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, df, breast_cancer