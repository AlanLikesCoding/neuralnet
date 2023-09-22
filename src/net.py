import math
from nodes import node


class network:
    """
    Args:
        inputs (int): The number of input neurons in the input layer.
        hlayers (int): The number of hidden layers in the network.
        hneurons (int): The number of neurons in each hidden layer.
        outputs (int): The number of output neurons in the output layer.

    Returns:
        None
    """
    def __init__(self, inputs: int, hlayers: int, hneurons: int, outputs: int) -> None:
        self.inputs = inputs
        self.hlayers = hlayers
        self.hneurons = hlayers
        self.outputs = outputs

        inputs_nodes: list = []
        for _ in range(inputs):
            inputs_nodes.append(node(neurons_before=0, make_weights=False))

        hlayers_nodes: list = [[]]
        for _ in range(hneurons):
            hlayers_nodes[0].append(node(inputs))
        for i in range(hlayers - 1):
            hlayers_nodes.append([])
            for _ in range(hneurons):
                hlayers_nodes[i].append(node(hneurons))

        outputs_nodes: list = []
        for _ in range(outputs):
            outputs_nodes.append(node(hneurons))

        self.nodes = [inputs_nodes] + [hlayers_nodes] + [outputs_nodes]

        print(self.nodes)
    
    def propagate(self, inputs: list):
        result = []
        result.append(inputs)
        for i in range(1, len(self.nodes)):
            result.append([])
            prev_neurons = result[i - 1]
            for p in range(len(self.nodes[i])):
                if not type(self.nodes[i][p]) == node:
                    for n in range(len(self.nodes[i][p])):
                        result[i].append(math.tanh(self.nodes[i][p][n].propagate(prev_neurons)))
                else:
                    result[i].append(math.tanh(self.nodes[i][p].propagate(prev_neurons)))
        return result[-1]
