from Particle import *

import math

# constant number of dimensions
NUM_OF_DIMENSIONS = 30


def rast_function(x):
    """ Computes the Rastrigin function for the defined number of dimensions"""

    value = 10 * NUM_OF_DIMENSIONS
    for i in range(NUM_OF_DIMENSIONS):
        value += x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])

    return value


class PSO:
    """ This class handles the main functionality of the PSO.
        
        It stores the global best fitness, global best position, the particle swarm,
        and the total number of iterations.
        
        It initially sets the global fitness to -1 and assigns a global position after iterations begin
        The particle swarm is initiated as particles with random position and velocities of 0
        
    """

    def __init__(self, num_particles, bounds, num_iterations, w, c1, c2):
        """
        :param num_particles: The number of particles in the swarm.
        :param bounds: The minimum and maximum values that a position element can be
        :param num_iterations: The total number of iterations to run for
        :param w: Inertia weight value
        :param c1: The cognitive component
        :param c2: The social component
        """

        self.global_best_fitness = -1
        self.global_best_pos = []
        self.swarm = [Particle(NUM_OF_DIMENSIONS, bounds, w, c1, c2) for i in range(num_particles)]
        self.num_iterations = num_iterations

    def begin_pso(self):
        """
            Begins the main PSO algorithm
            Loops for the number of iterations afterwards prints
            the global best position and the global best fitness
        """

        for i in range(self.num_iterations):

            for j in range(len(self.swarm)):

                self.swarm[j].eval(rast_function)

                # if the particle is in the search space
                if self.swarm[j].in_bounds():

                    # if the particles's best is better than the global best
                    if self.swarm[j].get_best_fitness() < self.global_best_fitness or self.global_best_fitness == -1:
                        self.global_best_pos = list(self.swarm[j].get_best_position())
                        self.global_best_fitness = self.swarm[j].get_best_fitness()

            for j in range(len(self.swarm)):
                self.swarm[j].update_velocity(self.global_best_pos)
                self.swarm[j].update_position()

        ##print("Best position:", self.global_best_pos)
        ##print("Best fitness:",self.global_best_fitness)
        print(self.global_best_fitness)
