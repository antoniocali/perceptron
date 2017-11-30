"""
Author: Antonio Cali
Project: perceptron
---
Perceptron Class:
    3 important function:
    -activateFunction
    -fit
    -train

    activateFunction: defines the output of inputs (sum of weights)
    fit: defines how perceptron is able to receive inputs and generate an output
    train: defines how weights should change
----
"""
import random

class Perceptron:
    def __init__(self, n, lr):
        self.n = n
        self.lr = lr
        self.weights = []
        for _ in range(self.n):
            self.weights.append(0)

    #A simple sign(x) function
    def activateFunction(self, n):
        if n >= 0:
            return 1
        else:
            return -1
    #Calcs sum of weightX*pointX+weightY*pointY+weightB*bias and return sign of sum
    def fit(self, point):
        sum_ = 0.0
        for i,(w,c) in enumerate(zip(self.weights, point)):
            sum_ += w*c
        return self.activateFunction(sum_)

    #Train itself, adjusting owns weights
    def train(self, inputs, desired):
        guess = self.fit(inputs)
        error = desired - guess
        for i, (w,inp) in enumerate(zip(self.weights,inputs)):
            self.weights[i] += self.lr * error * inp
