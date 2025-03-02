from keras.models import Sequential
from keras.layers import Dense

def build_ann(input_dim):
    """Construye y compila la red neuronal artificial."""
    model = Sequential()
    model.add(Dense(16, input_dim=input_dim, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model