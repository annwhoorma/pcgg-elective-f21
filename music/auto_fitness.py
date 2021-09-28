MIN_REPS = 4
MAX_REPS = 8

MAX_STEP = 1

def fitness(melody):
    # do for odd and even indices
    repeated_notes = sum(
        note1 == note2 for note1, note2 in zip(melody[:-2:2], melody[2::2])
    ) + sum(
        note1 == note2 for note1, note2 in zip(melody[1:-2:2], melody[3::2])
    )
    if not MIN_REPS <= repeated_notes <= MAX_REPS:
        return 0
    return repeated_notes

def repeatedness(melody):
    # do for odd and even indices
    repeated_notes = sum(
        note1 == note2 for note1, note2 in zip(melody[:-2:2], melody[2::2])
    ) + sum(
        note1 == note2 for note1, note2 in zip(melody[1:-2:2], melody[3::2])
    )
    if not MIN_REPS <= repeated_notes <= MAX_REPS:
        return 0
    return repeated_notes

def score_chords(melody):
    # if containes note and note + 8
    # if the step == 1
    pass
