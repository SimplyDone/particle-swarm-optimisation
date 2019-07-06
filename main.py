import argparse

from PSO import *
from RandomSearch import *


def main():
    parser = argparse.ArgumentParser(description="Run a PSO algorithm to optimize the"
                                                 " Rastrigin function for 30 dimensions")
    req = parser.add_argument_group("required arguments")
    parser.add_argument("-p", "--num_particles", help="The number of particles to use. (Default=30)", type=int,
                     default=30)
    req.add_argument("-i", "--num_iterations", help="The number of iterations to run for.",
                        type=int, required=True)
    parser.add_argument("-c", "--coefficient", help="The cognitive/social coefficient value. (Default=1.496180)",
                        type=float, default=1.496180)
    parser.add_argument("-ub", "--upper_bound", help="The upper bound of the search space. (Default=5.12)",
                        type=float, default=5.12)
    parser.add_argument("-lb", "--lower_bound", help="The lower bound of the search space. (Default=-5.12)",
                        type=float, default=-5.12)
    parser.add_argument("-w", "--weight", help="The inertia weight. (Default=0.729844)",
                        type=float, default=0.729844)
    args = parser.parse_args()

    pso = PSO(args.num_particles, (args.lower_bound, args.upper_bound), args.num_iterations, args.weight,
              args.coefficient, args.coefficient)
    pso.begin_pso()


main()

def test():
    values = ((0.729844, 1.496180), (0.4, 12), (1.0, 2.0), (-1.0, 2.0))

    for i in range(2,4):

        print("Running test", i)

        for j in range(20):
            pso = PSO(30, (-5.12, 5.12), 5000, values[i][0],
                      values[i][1], values[i][1])
            pso.begin_pso()


#test()

def rand_search():

    for j in range(20):
        RandomSearch((-5.12,5.12))

#rand_search()