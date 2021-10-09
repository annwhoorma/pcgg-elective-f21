MAX_STEP = 1

def fitness(melody):
    '''
    Fitness function. Calculates fitness score for a melody
    @param melody: the melody (as numbers, e.g. [[1, 14, 15, 15], ...] - for 1 bar containing 4 notes)
    @return score
    '''
    offset = int(0.3*len(melody))
    return repeatedness(melody, offset) + distance(melody, offset) # + ... - To be implemented.


def repeatedness(melody, offset):
    '''
    Gives a score to melody based on its repeatedness;
    Counts only even and odd places
    @param melody: the melody (as numbers, e.g. [[1, 14, 15, 15], ...] - for 1 bar containing 4 notes)
    @return number of repeated notes on odd and even places
    '''
    min_reps = 0.15 * len(melody)
    max_reps = 0.3 * len(melody)
    offset = offset + 1 if offset % 2 != 0 else offset
    # do for odd and even indices
    repeated_notes = sum(
        note1 == note2 for note1, note2 in zip(melody[offset:-offset-2:2], melody[offset+2:-offset:2])
    )
    - 2 * sum(
        melody[i] == melody[i+1] for i in range(len(melody[:-1]))
    )
    return repeated_notes


def score_melody_beginning(part):
    if len(part) < 1:
        return
    score = 0
    for i in range(len(part[:-1])):
        if 0 < part[i+1] - part[i] <= 2:
            score += 5
        elif 0 == part[i+1] - part[i]:
            score -= 1
        else:
            score -= 2
    return score


def score_melody_ending(part):
    if len(part) < 1:
        return
    score = 0
    for i in range(len(part[:-1])):
        if 0 < part[i] - part[i+1] <= 2:
            score += 5
        else:
            score -= 1
    return score
    

def distance(melody, offset):
    if len(melody) < 2 * offset + 1:
        return 0
    first_part, _, last_part = melody[:offset], melody[offset:-offset], melody[-offset:]
    score = 0
    # score the beginning
    score += score_melody_beginning(first_part)
    # score the end
    score += score_melody_ending(last_part)
    return score


def score_chords(melody):
    '''
    Gives a score to a chord; To be implemented
    '''
    pass
