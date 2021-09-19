from random import randint

def _one_point_crossover(notes1, notes2):
    p = randint(0, len(notes1)-1)
    return (
        notes1[:p] + notes2[p:],
        notes2[:p] + notes1[p:]
    )

def _two_points_crossover(notes1, notes2):
    p1 = randint(0, len(notes1)-2)
    p2 = randint(p1+1, len(notes1)-1)
    return (
        notes1[:p1] + notes2[p1:p2] + notes1[p2:],
        notes2[:p1] + notes1[p1:p2] + notes2[p2:]
    )

possible_crossovers = [
    _one_point_crossover,
    _two_points_crossover
]

def crossover(notes1, notes2):
    crossover_function = possible_crossovers[randint(0, 1)]
    return crossover_function(notes1, notes2)
