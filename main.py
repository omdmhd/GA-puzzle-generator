'''
    load skeleton
    make N Set Generation with M Population
    OffSpring
    Mutation
    Population Trimming
    Aggregation
'''
from skeleton import Skeleton
from population import Population

skeleton = Skeleton()
skeleton.read_skeleton_from_file('input/sample.txt')
N = input('Enter N : ')
M = input('Enter Population Size')
Sets = []

for i in range(0, N):
    population = Population(M)
    Sets.append(population)

for population in Sets:
    population.offspring()

for population in Sets:
    population.trim()

'''
    Aggregation
'''