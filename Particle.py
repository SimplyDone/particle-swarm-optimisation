import random

class Particle:
    """ This class represents a single particle.
        
        It stores the particle's current fitness, current position, current 
        velocity, best fitness, best position, various problem specific details such as map bounds
        and whether or not the particle is in the problem bounds.
        
        It initially sets the the velocity to 0, the position to a random point, and the best fitness to -1
    """
    def __init__(self, dimension, bounds, w, c1, c2):

        self.w, self.c1, self.c2 = w, c1, c2
        self.bounds = bounds
        self.dimension = dimension

        self.pos = [random.uniform(bounds[0], bounds[1]) for i in range(self.dimension)]
        self.vel = [0.0 for i in range(dimension)]

        self.best_pos = []
        self.best_fitness = -1

        self.is_in_bounds = True

    def eval(self, funct):
        """ This method evaluates the particles current position and compares it to its best position.
            If the particles is still within the map bounds it update the particles best position
        
        :param funct: The function to minimize
        """

        value = funct(self.pos)

        if self.is_in_bounds:

            if value < self.best_fitness or self.best_fitness == -1:
                self.best_fitness = value
                self.best_pos = list(self.pos)

    def update_velocity(self, global_best_pos):
        """ This method updates the particles velocity based on the cognitive, social, and
            inertial components.
            
            It also limits the maximum velocity to half of the search space.
        
        :param global_best_pos: The current global best position
        """

        vmax = (self.bounds[1] - self.bounds[0]) / 2

        for i in range(self.dimension):

            cognitive = self.get_cognitive(i)
            social = self.get_social(i, global_best_pos)
            self.vel[i] = self.w * self.vel[i] + cognitive + social

            if self.vel[i] > vmax:
                self.vel[i] = vmax

            if self.vel[i] < -vmax:
                self.vel[i] = -vmax

    def get_cognitive(self, i):
        """
        :param i: The current dimension
        :return:  The cognitive component
        """
        return self.c1 * random.random() * (self.best_pos[i] - self.pos[i])

    def get_social(self, i, global_best_pos):
        """
        :param i: The current dimension
        :param global_best_pos: The best position
        :return: The social component
        """
        return self.c2 * random.random() * (global_best_pos[i] - self.pos[i])

    def update_position(self):
        """ Updates the particles current position and determines if it is currently 
            in the bounds of the map
        """

        self.is_in_bounds = True

        for i in range(self.dimension):

            self.pos[i] += self.vel[i]

            if self.pos[i] < self.bounds[0] or self.pos[i] > self.bounds[1]:
                self.is_in_bounds = False

    def in_bounds(self):
        """
        :return: Whether the particle in the map bounds
        """
        return self.is_in_bounds

    def get_best_fitness(self):
        """
        :return: The particle's best fitness
        """
        return self.best_fitness

    def get_best_position(self):
        """
        :return: The particle's best position
        """
        return self.best_pos

    def get_position(self):
        """
        :return: The particle's current position
        """
        return self.pos
