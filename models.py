import numpy as np
import matplotlib.pyplot as plt

class Node():
    def __init__(self, value):
        self.value = value
    
class Network():
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_hidden_layers = num_hidden_layers
    
class MyFFNetworkForClassification(Network):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        super().__init__(input_dim, hidden_dim, output_dim, num_hidden_layers)
        pass
    
class MyFFNetworkForRegression(Network):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_hidden_layers: int):
        super().__init__(input_dim, hidden_dim, output_dim, num_hidden_layers)
        pass
