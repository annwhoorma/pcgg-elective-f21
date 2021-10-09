# Music generation

The music is generated using evolutionary algorithm.

**To run the project, do the following:**

1. Go to the file _args.py_ which contains user input. _Preffered_ values are already there, but most of them are changable
    - `NUMBER_OF_BARS` - number of bars in the final melody
    - `NOTES_PER_BAR` - number of notes in one bar (according to music "rules" it should be 1, 2, 4, 8, or 16 - more just doesn't make sense)
    - `BITS_PER_NOTE` - number of bits to encode a note. The less bits, the smaller span of notes is available for generation.
    - `BEATS_PER_BAR` # definitely a constant
    - `SCALE` - scale of the melody ('major' or 'minor')
    - `SCALE_ROOT` - scale root of the melody ('A', 'B', 'C' etc)
    - `PITCH_LEVEL` - level of pitch of the melody; may sound differently after converting _.mid_ to _.mp3_
    - `BPM` - beats per minute; may sound differently after converting _.mid_ to _.mp3_
    - `VELOCITY` - velocity of the melody; may sound differently after converting _.mid_ to _.mp3_
    - `EPOCHS` - number of epochs for the evolutionary algorithm; in other words, number of generations
    - `POP_SIZE` - population size (high numbers are not recommended, as the algorithm converges very fast with any number)
    - `FITNESS_FUNCTION` - fitness function to use; 'manual' will allow to grade the melodies as they are generated manually, 'auto' will mean that genoms will be ranked automatically by fitness function in _auto\_fitness.py_
    - `SAVE_AS` - filename to store the final result

    **Note**: since the algorithm saves the file as _.mid_, it must be converted to _.mp3_, unless you have a _mid_-player. Moreover, if you are ranking the genomes manually based on how they sound, then probably the generated file will sound a bit different due to different libraries used to play and save the melodies.

2. In the terminal, run:

```bash
pip install requirements.txt
python main.py
```

## The results

| initial # of genoms | number of epochs | time spent, s | best genome’s rank | the result |
| ------------------- | ---------------- | ------------- | ------------------ | ---------- |
| 15                  | 5000             | 13.77562      | 59                 | ![](results/mp3/p15_e5000.mp3)           |
| 15                  | 10000            | 22.68578      | 60                 | <audio controls src="results/mp3/p15_e10000.mp3">           |
| 15                  | 50000            | 106.16036     | 60                 | <audio controls src="results/mp3/p15_e50000.mp3">           |
| 50                  | 5000             | 20.84560      | 54                 | <audio controls src="results/mp3/p50_e5000.mp3">           |
| 50                  | 10000            | 39.67426      | 65                 | <audio controls src="results/mp3/p50_e10000.mp3">           |
| 50                  | 50000            | 188.70546     | 54                 | <audio controls src="results/mp3/p50_e50000.mp3">           |
| 80                  | 5000             | 32.15173      | 53                 | <audio controls src="results/mp3/p80_e5000.mp3">           |
| 80                  | 10000            | 61.03217      | 79                 | <audio controls src="results/mp3/p80_e10000.mp3">           |
| 80                  | 50000            | 291.33743     | 73                 | <audio controls src="results/mp3/p80_e50000.mp3">           |
