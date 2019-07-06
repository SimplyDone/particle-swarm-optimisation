from PSO import rast_function;
from PSO import NUM_OF_DIMENSIONS;

import random

class RandomSearch:

    def __init__(self, bounds):

        self.bounds = bounds
        self.pos = []
        self.best_pos = []
        self.best_fitness = 10000

        for i in range(150000):
            self.evaluate()

        print(self.best_fitness)

    def evaluate(self):

        self.pos = [random.uniform(self.bounds[0], self.bounds[1]) for i in range(NUM_OF_DIMENSIONS)]
        value = rast_function(self.pos)

        if(value < self.best_fitness):
            self.best_fitness = value