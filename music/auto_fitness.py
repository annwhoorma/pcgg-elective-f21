MIN_REPS = 4
MAX_REPS = 8

MAX_STEP = 1 # for chords

def fitness(melody):
    score = 0
    if MIN_REPS <= calculate_repetitions(melody) <= MAX_REPS:
        score += 5
    # do for odd and even indices
    for idx in range(len(melody) - 2):
        if melody[idx] 


def calculate_repetitions():
    pass
