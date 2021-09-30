'''
Contains 6 types of mutations
'''

from random import randint

from constants import BITS_PER_NOTE

def mutation_type_1(notes, index):
    '''
    Type 1: changes current note to be as the next one
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    try:
        return notes[index + 1]
    except:
        return None

def mutation_type_2(notes, index):
    '''
    Type 2: changes current note to be as the previous one
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    try:
        return notes[index - 1]
    except:
        return None

def mutation_type_3(notes, index):
    '''
    Type 3: changes current note to be as the one before the previous one
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    return notes[index - 2] if index >= 2 else None

def mutation_type_4(notes, index):
    '''
    Type 4: changes current note to be as the the one after the next one
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    return notes[index + 2] if index + 2 < len(notes) else None

def mutation_type_5(notes, index):
    '''
    Type 5: changes current note to be as the one 8 notes before
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    new_note = notes[index] - 8 # go down by an octave
    return new_note if new_note >= 0 else None

def mutation_type_6(notes, index):
    '''
    Type 6: changes current note to be as the one 8 notes after
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note or None, if not possible to change
    '''
    new_note = notes[index] + 8 # go up by an octave
    return new_note if new_note < 2 ** BITS_PER_NOTE else None

# list of possible mutations
possible_mutations = [
    mutation_type_1,
    mutation_type_2,
    mutation_type_3,
    mutation_type_4,
    mutation_type_5,
    mutation_type_6,
]

def mutate_one_note(notes, index):
    '''
    Mutates one note with a random mutation
    @param notes: all notes in the melody
    @param index: index of the current note
    @return changed note
    '''
    new_note = None
    counter = 0
    while new_note is None and counter < 100:
        mutation_type =  randint(0, len(possible_mutations) - 1)
        mutation = possible_mutations[mutation_type]
        new_note = mutation(notes, index)
        counter += 1
    return new_note or notes[index]

def mutation(notes):
    '''
    Mutates some notes from the melody
    @param notes: the melody (as numbers, e.g. [[1, 14, 15, 15], ...] - for 1 bar containing 4 notes)
    @return changed melody
    '''
    number_of_notes_to_change = len(notes) // 4
    for _ in range(number_of_notes_to_change):
        index = randint(0, len(notes)-1)
        notes[index] = mutate_one_note(notes, index)
    return notes