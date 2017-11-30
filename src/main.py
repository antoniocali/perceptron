"""
Author: Antonio Cali
Project: perceptron
---
Simple perceptron project with no Numphy module.
----
"""

from perceptron import Perceptron
from trainer import Trainer
import random
# Define a main() function that prints a little greeting.
def main():
    #f: is straight line that divide our plane in 2 different classes
    f = lambda x: x*2+1
    """
    c: is the learning rate. (0.0,1.0].
    High value: faster learning but error rate will probably be higher
    Low Value: slower learning, if too low it could "stuck" the learning process
    """
    c = 0.1
    """
    p: Perceptron.
    Number 3 is fixed, it represents the (n-1)-dimensional case, for this example
    we're working on 2-dimension. The (+1) dimension stands for the bias value (fixed to 1)
    """
    p = Perceptron(3, c)
    #n: number of points to use to traing (and test).
    n = 20000
    #d: display at every percent of rounds to show current learning/test phase
    d = 10
    trainingInputs = []
    for _ in range(n):
        trainingInputs.append(Trainer(random.randint(-100, 100), random.randint(-100, 100), f))
    for i, t in enumerate(trainingInputs):
        p.train(t.inputs, t.output)
        if i % int((n/100)*d) == 0 or i == len(trainingInputs)-1:
            correctGuess = 0
            for point in trainingInputs:
                if point.output == p.fit(point.inputs):
                    correctGuess+=1
            print "Round %d / Correct Guess %i" % (i, correctGuess)
    print p.weights


    # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
