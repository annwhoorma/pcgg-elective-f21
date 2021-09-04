from pyo import *
from time import sleep
from random import sample, choices

NUMBER_OF_BARS = 2
NOTES_PER_BAR = 16
BITS_PER_NOTE = 4
BEATS_PER_BAR = 4 # definitely a constant
SCALE = 'major'
SCALE_ROOT = 'C'
PITCH_LEVEL = 8

def create_genome(length):
    # sample() didnt work
    return choices(range(2), k=length)

def genome_to_melody(genome):
    # [1, 0, 1, 0, 1, 1, 1, 1] -> [[1, 0, 1, 0], [1, 1, 1, 1]]
    print(NOTES_PER_BAR//NUMBER_OF_BARS)
    notes = [genome[i*BITS_PER_NOTE:i*BITS_PER_NOTE+BITS_PER_NOTE] for i in range(NOTES_PER_BAR//NUMBER_OF_BARS)]
    # event_scale = EventScale(SCALE, SCALE_ROOT, PITCH_LEVEL) # for case if we have chords
    # note_length = BEATS_PER_BAR / float(NOTES_PER_BAR) # for beats

    melody = []
    print(notes)
    for note in notes:
        note = int(''.join(str(n) for n in note), 2)
        melody += [note]
        print(f'melody: {melody}')

    return [Events(
            midinote=note
        ) for note in melody]

s = Server()
s.setOutputDevice(2)
s.boot()
# s.start()

genome = create_genome(NOTES_PER_BAR*NUMBER_OF_BARS)
print(f'genome: {genome}')
events = genome_to_melody(genome)

for e in events:
    e.play()
s.start()
input("here is the no1 hit …")
s.stop()
for e in events:
    e.stop()

# a = Sine(freq=100, phase=0, mul=1).out()

s.gui(locals())

# sleep(2)
# s.stop()    