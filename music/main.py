from pyo import *
from time import sleep
from random import sample, choices, randint, choice
from numpy import arange

from args import *
from mutation import mutation
from crossover import crossover
from auto_fitness import fitness
from midiutil import MIDIFile

from time import time


GENOME_SIZE = BITS_PER_NOTE * NOTES_PER_BAR * NUMBER_OF_BARS


def generate_random_lengths(mind=0.25, maxd=2, step=0.25, total=BITS_PER_NOTE*NOTES_PER_BAR):
    current_sum = 0
    lengths = []
    possible = arange(mind, maxd+step, step)
    while current_sum < total:
        duration = choice(possible)
        if duration <= total - current_sum:
            lengths.append(duration)
            current_sum += duration
    if current_sum == total:
        return lengths
    return None


def save_genome_to_midi(filename, genome):
    _, melody, note_length = genome_to_melody(genome)
    # print(melody, note_length)

    mf = MIDIFile(numTracks=1)

    track = 0
    channel = 0
    volume = 127
    time = 0.0
    duration = 1
    offset = PITCH_LEVEL * 14

    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, tempo=BPM)

    for i, note in enumerate(melody):
        mf.addNote(track, channel, offset + note, time + i * note_length, duration, volume)

    # os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        mf.writeFile(f)


def rank_population(population, epoch):
    population = sorted(population, key=lambda g: g[1], reverse=True)
    if epoch % 4999 == 0 or epoch % EPOCHS == 0:
        print(i, [j for i, j in population])
    return [pop for pop, rank in population]

def create_genome(length):
    # generate of different length, just so that it gives a reasonable number of beats at the end
    beats_sum = BEATS_PER_BAR * NOTES_PER_BAR
    # generate random numbers from 0.25 to 2
    return choices(range(2), k=length)

def create_population(pop_size=POP_SIZE, genome_size=GENOME_SIZE):
    return [create_genome(genome_size) for _ in range(pop_size)]

def play(events, index):
    for e in events:
        e.play()
    s.start()
    rank = input(f'genome {index}: ')
    s.stop()
    for e in events:
        e.stop()
    return rank


def fitness_function(population):
    for i, genome in enumerate(population):
        events, melody, _ = genome_to_melody(genome)
        rank = play(events, i) if FITNESS_FUNCTION == 'manual' else fitness(melody)
        population[i] = (melody, rank)
    return population


def genome_to_melody(genome):
    # [1, 0, 1, 0, 1, 1, 1, 1] -> [[1, 0, 1, 0], [1, 1, 1, 1]]
    notes = [genome[i*BITS_PER_NOTE:i*BITS_PER_NOTE+BITS_PER_NOTE] for i in range(NOTES_PER_BAR * NUMBER_OF_BARS)]
    event_scale = EventScale(SCALE_ROOT, SCALE, PITCH_LEVEL)
    note_length = float(BEATS_PER_BAR / NOTES_PER_BAR) # for beats

    melody = []
    for note in notes:
        note = int(''.join(str(n) for n in note), 2)
        melody += [note]

    steps = [
        [event_scale[(note + step * 2) % len(event_scale)] for note in melody]
        for step in range(NUMBER_OF_STEPS)
    ]

    return (
        [Events(
            midinote=EventSeq(note, occurrences=1),
            beat=note_length,
            attack=0.001,
            decay=0.05,
            sustain=0.5,
            release=0.005,
        ) for note in steps],
        melody,
        note_length
    )


def melody_to_bin(melody):
    binary_sequence = []
    for notenum in melody:
        binary_repr = bin(notenum).split('b')[1]
        binary_repr = binary_repr.zfill(BITS_PER_NOTE)
        binary_sequence += [int(char) for char in binary_repr]
    return binary_sequence


if __name__ == '__main__':
    s = Server()
    s.setOutputDevice(2)
    s.boot()
    
    start = time()
    population = create_population()
    top_number = max(int(0.1 * POP_SIZE), 4)
    new_genoms_number = POP_SIZE - 3 - (top_number - 2) * 2 # mutations = 2, crossovers = (top_number - 2)*2, add top[0 or 1]
    for i in range(EPOCHS):
        population = fitness_function(population)
        top = rank_population(population, i)[:top_number]
        if i == EPOCHS - 1:
            save_genome_to_midi(SAVE_AS or f'results/gen{i}.mid', melody_to_bin(top[0]))
        crossovers = []
        for i in range(top_number):
            chosen = randint(0, top_number//3)
            new_pair = crossover(top[chosen], top[i])
            crossovers.append(melody_to_bin(new_pair[0]))
            crossovers.append(melody_to_bin(new_pair[1]))
        mutations = [melody_to_bin(mutation(melody)) for melody in top]
        population = create_population(POP_SIZE // 3) # new random ones
        population += crossovers + mutations # + [melody_to_bin(m) for m in top[:10]]
    # s.gui(locals())
    print(f'Generation time: {time() - start}')
