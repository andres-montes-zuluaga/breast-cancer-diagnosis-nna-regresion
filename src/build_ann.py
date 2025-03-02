from keras.models import Sequential
from keras.layers import Dense

def build_ann(input_dim):
    """Construye y compila la red neuronal artificial."""
    model = Sequential()
    
    # Primera capa oculta con 16 neuronas y función de activación 'relu'.
    # Se elige 16 neuronas para capturar patrones complejos en los datos de entrada.
    # La función 'relu' ayuda a manejar el problema de desvanecimiento del gradiente y permite una mejor convergencia.
    model.add(Dense(16, input_dim=input_dim, activation='relu'))
    
    # Segunda capa oculta con 8 neuronas y función de activación 'relu'.
    # Se reduce el número de neuronas para forzar la red a aprender representaciones más compactas y relevantes.
    # La función 'relu' sigue ayudando a la convergencia eficiente del modelo.
    model.add(Dense(8, activation='relu'))
    
    # Capa de salida con 1 neurona y función de activación 'sigmoid'.
    # Se usa 1 neurona porque estamos realizando una clasificación binaria (diagnóstico de cáncer).
    # La función 'sigmoid' convierte la salida en una probabilidad entre 0 y 1.
    model.add(Dense(1, activation='sigmoid'))
    
    # Compilación del modelo con el optimizador 'adam' y la función de pérdida 'binary_crossentropy'.
    # El optimizador 'adam' es eficiente y requiere poca memoria.
    # La función de pérdida 'binary_crossentropy' es adecuada para problemas de clasificación binaria.
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model