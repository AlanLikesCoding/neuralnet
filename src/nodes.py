import random

class node:

    def __init__(self, neurons_before=0, make_weights=True) -> None:
        """
        Args:
            neurons_before (int): The number of neurons in the previous layer.
            make_weights (bool): Whether to create weights for connections to this neuron.

        Attributes:
            neurons_before (int): The number of neurons in the previous layer.
            not_input (bool): Indicates if this neuron is in the input layer (no weights).
            bias (float): The bias value for this neuron.
            weights (list of float): The weights for connections to this neuron (if applicable).

        Methods:
            propagate(neurons_before: list) -> float:
                Propagates input from the previous layer through this neuron.
                Returns the output of this neuron after applying weights and bias.
        """
        self.neurons_before = neurons_before
        self.not_input = make_weights
        self.bias = random.random() * 2 - 1
        if make_weights:
            self.weights = [random.random() * 2 - 1 for _ in range(neurons_before)]
    
    def __repr__(self) -> str:
        return f"node(neurons_before={self.neurons_before}, make_weights={self.not_input})"

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of this neuron.
        """
        return f"node(neurons_before={self.neurons_before}, make_weights={self.not_input})"
    
    def propagate(self, neurons_before: list) -> float:
        """
        Args:
            neurons_before (list of float): The outputs of neurons in the previous layer.

        Returns:
            float: The output of this neuron after applying weights and bias.
        """
        total = self.bias
        for i in range(len(self.weights)):
            total += self.weights[i] * neurons_before[i]
        return total
