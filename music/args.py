NUMBER_OF_BARS = 2
NOTES_PER_BAR = 16
BITS_PER_NOTE = 4
BEATS_PER_BAR = 4 # definitely a constant
SCALE = 'major'
SCALE_ROOT = 'C'
PITCH_LEVEL = 3
NUMBER_OF_STEPS = 1 # put > 1 if you want to include chords - TODO
BPM = 60
VELOCITY = 127
EPOCHS = 10000
POP_SIZE = 80
FITNESS_FUNCTION = 'auto' # set to 'manual' if you want to evaluate the melodies manually

SAVE_AS = f'results/p{POP_SIZE}_e{EPOCHS}.mid'