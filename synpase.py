import numpy as np

class Synapse:
    def __init__(self, layer=0, decay_rate=0.1):
        self.decay_rate = decay_rate #charge % decay per unit of time
        self.charge = 0
        self.layer = layer #0th layer cannot connect to 2nd layer...
        self.depth = 0

    def update(self, transmission, time=1):
        # Increment reactivity with input signal
        # Decay reactivity over time
        num_decay = time / 1
        charge = self.charge
        self.charge *= (1 - self.decay_rate * num_decay)
        return charge
    
    def connect(self, receiver):
        assert type(receiver) == Cleft

class Cleft:
    def __init__(self, plasticity=1, distance=1):
        self.plasticity = plasticity
        self.distance = 1
        self.connected = False
    
    def update(self, charge):
        trigger = charge * plasticity > distance
        return charge if trigger else 0
    
    def connect(self, transmitter, receiver):
        assert type(receiver) == Synapse and type(transmitter) == Synapse
        self.connected = True

#receptive field
receptor = Synapse(layer=0, decay_rate=0.1)
cleft = Cleft(plasticity=1, distance=1)

#transmission field
message = Synapse(layer=0, decay_rate=0.1)
cleft2 = Cleft(plasticity=1, distance=1)

#response field
response = Synapse(layer=0, decay_rate=0.1)
cleft3 = Cleft(plasticity=1, distance=1)
action = Synapse(layer=0, decay_rate=0.1)


class Field:
    def __init__(self):
        self.layers = {} #unique members...
    
    def transmit(self, transmission):
        for layer in range(max(self.layers.keys())):
            for synapse in self.layers[layer]

        
class Transmission:
    def __init__(self, callbacks=None):
        self.connections = deque()
        # self.callbacks = callbacks if callbacks else []
    
    def add(self, connection):
        self.connections.append(connection)
    
    @property
    def route(self,):
        seen = set()
        for e in self._route:
            if e in seen:
                continue
            seen.add(e)
            yield e
    
    def __call__(self, signal, **kwargs):
        """
            Forward operation for signal transmission through all connections.
            Operated on a DAG; therefore, race conditions should be considered, later.
        """
        self._route = []
        output = signal
        for connection in self.connections:
            for predecessor in connection.predecessors:
                self._route.append(predecessor)
            self._route.append(connection)
            output = connection(output, **kwargs)
            for successor in connection.successors:
                output = successor(output, **kwargs)
            # for callback in self.callbacks:
            #     callback(connection, output)
        return output
    
    def display(self):
        print('==============================')
        for connection in self.connections:
            predecessors = f"{', '.join(map(str, connection.predecessors))}"
            conn = connection._name
            successors = f"{', '.join(map(str, connection.successors))}"
            print(f"{predecessors + ': -> ' if predecessors else ''}{conn}{': -> ' + successors if successors else ''}")
        print('==============================\n\n')