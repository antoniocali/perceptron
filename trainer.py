"""
Author: Antonio Cali
Project: perceptron
---
Trainer Class:
    Simple point class that have a X and Y Coordinate.
    We pass also the function of the straight line that divide the plane:
    usefull to automatically calculate the expected output of classification
----
"""
class Trainer:
    def __init__(self, x, y, function):
        self.inputs = [x,y,1]
        self.output = 1
        if (y<function(x)):
            self.output = -1
