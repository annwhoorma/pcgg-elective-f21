MIN_REPS = 4
MAX_REPS = 8

MAX_STEP = 1

def fitness(melody):
    '''
    Fitness function. Calculates fitness score for a melody
    @param melody: the melody (as numbers, e.g. [[1, 14, 15, 15], ...] - for 1 bar containing 4 notes)
    @return score
    '''
    return repeatedness(melody) + distance(melody) # + ... - To be implemented.

def repeatedness(melody):
    '''
    Gives a score to melody based on its repeatedness;
    Counts only even and odd places
    @param melody: the melody (as numbers, e.g. [[1, 14, 15, 15], ...] - for 1 bar containing 4 notes)
    @return number of repeated notes on odd and even places
    '''
    # do for odd and even indices
    repeated_notes = sum(
        note1 == note2 for note1, note2 in zip(melody[:-2:2], melody[2::2])
    ) + sum(
        note1 == note2 for note1, note2 in zip(melody[1:-2:2], melody[3::2])
    )
    if not MIN_REPS <= repeated_notes <= MAX_REPS:
        return 0
    return repeated_notes


def score_melody_part(part, mindist, maxdist):
    # TODO
    # для конца мелодии надо чтобы ноты уменьшались
    # для начала - чтобы росли
    if len(part) < 1:
        return
    score = 0
    for i in range(len(part[:-1])):
        if abs(part[i] - part[i+1]) <= maxdist:
            score += 1
        if abs(part[i] - part[i+1] >= mindist):
            score += 1
    return score
    

def distance(melody):
    if len(melody) < 15:
        return 0
    offset = int(0.3*len(melody)) if len(melody) >= 15 else int(0.2*len(melody))
    first_part, middle_part, last_part = melody[:offset], melody[offset:-offset], melody[-offset:]
    score = 0
    # score the beginning
    score += score_melody_part(first_part, 1, 3)
    # score the middle part
    score += score_melody_part(middle_part, 1, 5)
    # score the end
    score += score_melody_part(last_part, 1, 3)
    return score


def score_chords(melody):
    '''
    Gives a score to a chord; To be implemented
    '''
    pass
