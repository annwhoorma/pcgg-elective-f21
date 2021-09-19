from random import randint

from constants import BITS_PER_NOTE

def mutation_type_1(notes, index):
    try:
        return notes[index + 1]
    except:
        return None

def mutation_type_2(notes, index):
    try:
        return notes[index - 1]
    except:
        return None

def mutation_type_3(notes, index):
    return notes[index - 2] if index >= 2 else None

def mutation_type_4(notes, index):
    return notes[index + 2] if index + 2 < len(notes) else None

def mutation_type_5(notes, index):
    new_note = notes[index] - 8 # go down by an octave
    return new_note if new_note >= 0 else None

def mutation_type_6(notes, index):
    new_note = notes[index] + 8 # go up by an octave
    return new_note if new_note < 2 ** BITS_PER_NOTE else None

possible_mutations = [
    mutation_type_1,
    mutation_type_2,
    mutation_type_3,
    mutation_type_4,
    mutation_type_5,
    mutation_type_6,
]

def mutate_one_note(notes, index):
    new_note = None
    counter = 0
    print('****')
    while new_note is None and counter < 100:
        mutation_type =  randint(0, len(possible_mutations) - 1)
        mutation = possible_mutations[mutation_type]
        new_note = mutation(notes, index)
        print(notes[index], mutation_type, new_note)
        counter += 1
    return new_note or notes[index]

def mutation(notes):
    '''
    notes - an array of notes (not bits), e.g. [1, 14, 15, 15] - for 1 bar containing 4 notes

    possible mutations:
    '''
    number_of_notes_to_change = len(notes) // 4
    for _ in range(number_of_notes_to_change):
        index = randint(0, len(notes)-1)
        notes[index] = mutate_one_note(notes, index)
    return notes