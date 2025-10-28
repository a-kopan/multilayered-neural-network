import numpy as np
import matplotlib.pyplot as plt

class Layer_Dense:
    # Layer initialization
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
        # Forward pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases
        
class Network():
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        # set attributes
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_hidden_layers = num_hidden_layers

        # initialize weights
        self.initializeWeights()
    
    def initializeWeights(self):
        pass
    
class MyFFNetworkForClassification(Network):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        super().__init__(input_dim, hidden_dim, output_dim, num_hidden_layers)
        pass
    
class MyFFNetworkForRegression(Network):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        super().__init__(input_dim, hidden_dim, output_dim, num_hidden_layers)
        pass
