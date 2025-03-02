from keras.models import Sequential
from keras.layers import Dense

def build_ann(input_dim):
    """Builds and compiles the artificial neural network."""
    model = Sequential()
    
    # First hidden layer with 16 neurons and 'relu' activation function.
    # 16 neurons are chosen to capture complex patterns in the input data.
    # The 'relu' function helps handle the vanishing gradient problem and allows better convergence.
    model.add(Dense(16, input_dim=input_dim, activation='relu'))
    
    # Second hidden layer with 8 neurons and 'relu' activation function.
    # The number of neurons is reduced to force the network to learn more compact and relevant representations.
    # The 'relu' function continues to aid in efficient model convergence.
    model.add(Dense(8, activation='relu'))
    
    # Output layer with 1 neuron and 'sigmoid' activation function.
    # 1 neuron is used because we are performing binary classification (cancer diagnosis).
    # The 'sigmoid' function converts the output into a probability between 0 and 1.
    model.add(Dense(1, activation='sigmoid'))
    
    # Model compilation with 'adam' optimizer and 'binary_crossentropy' loss function.
    # The 'adam' optimizer is efficient and requires little memory.
    # The 'binary_crossentropy' loss function is suitable for binary classification problems.
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model