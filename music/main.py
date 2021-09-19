from pyo import *
from time import sleep
from random import sample, choices, randint

from constants import *
from mutation import mutation
from crossover import crossover

POPULATION_SIZE = 10 # at least 5
GENOME_SIZE = BITS_PER_NOTE * NOTES_PER_BAR * NUMBER_OF_BARS


def rank_population(population):
    sorted(population, key=lambda g: g[1])
    return [pop for pop, rank in population]

def create_genome(length):
    return choices(range(2), k=length)

def create_population(pop_size=POPULATION_SIZE, genome_size=GENOME_SIZE):
    return [create_genome(genome_size) for _ in range(pop_size)]

def play(events, index):
    for e in events:
        e.play()
    s.start()
    rank = input(f'genome {index}: ')
    s.stop()
    for e in events:
        e.stop()
    # sleep(1)
    return rank


def fitness_function(population):
    for i, genome in enumerate(population):
        events, melody = genome_to_melody(genome)
        rank = play(events, i)
        population[i] = (melody, rank)
        print(population[i])


def genome_to_melody(genome):
    # [1, 0, 1, 0, 1, 1, 1, 1] -> [[1, 0, 1, 0], [1, 1, 1, 1]]
    notes = [genome[i*BITS_PER_NOTE:i*BITS_PER_NOTE+BITS_PER_NOTE] for i in range(NOTES_PER_BAR * NUMBER_OF_BARS)]
    event_scale = EventScale(SCALE_ROOT, SCALE, PITCH_LEVEL)
    # note_length = BEATS_PER_BAR / float(NOTES_PER_BAR) # for beats

    melody = []
    for note in notes:
        note = int(''.join(str(n) for n in note), 2)
        melody += [note]
    print(melody)

    steps = [
        [event_scale[(note + step * 2) % len(event_scale)] for note in melody]
        for step in range(NUMBER_OF_STEPS)
    ]

    return (
        [Events(
            midinote=note,
            attack=0.001,
            decay=0.05,
            sustain=0.5,
            release=0.005,
        ) for note in steps],
        melody
    )


s = Server()
s.setOutputDevice(0)
s.boot()

population = create_population()
top_number = int(max(POPULATION_SIZE // 1.8, 4))
new_genoms_number = POPULATION_SIZE - 3 - (top_number - 2) * 2 # mutations = 2, crossovers = (top_number - 2)*2, add top[0 or 1]
print('BITCH 1')
print(top_number, new_genoms_number)
for i in range(10):
    print(f'***GEN {i}***')
    fitness_function(population)
    top = rank_population(population)[:top_number]
    
    crossovers = []
    print('CROSSOVER')
    for i in range(2, len(top)):
        chosen = randint(0, 1)
        print(chosen, i)
        new_pair = crossover(top[chosen], top[i])
        crossovers.append(new_pair[0])
        crossovers.append(new_pair[1])
    print('\nMUTATIONS')
    mutations = [mutation(melody) for melody in top[:2]]
    population = create_population(pop_size=5) # new random ones
    population += crossovers + mutations + [top[randint(0, 1)]]
    print('BITCH 2')
    print(len(top), len(crossovers), len(mutations), len(population))

# s.gui(locals())