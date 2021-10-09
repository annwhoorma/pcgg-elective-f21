# Mountains Generation

The mountains are generated using L-system method created in 2005 by Daniel Ashlock.

**To run the project, do the following:**

1. Go to the file _args.py_ which contains user input.
    - `start_height = 20` - the start level for tile generation; it doesn't affect the visualization though.

    - `size` - size of one tile; must be a degree of 2

    - `mountain_type` - type of one mountain to generate; possible types are: `TileType.CALM`, `TileType.HILL`, `TileType.STEEP`.

    - `mountain_comb` - an two-dimensional array containing a combination of mountain tile types to construct. When constructed, all the tiles are connected.

2. In the terminal, run:

```bash
pip install requirements.txt
python main.py
```

3. The script will ask what would you like to generate - a mountain or a forest of mountains. If you choose the first option, then the algorithm will generate whatever is `mountain_type` set to. If you choose the second option, then the algorithm will generate a set of mountains as specified in `mountain_comb`.


## The results

### "Calm" type
![Calm Mountain](./results/calm_mount.png)

### "Hill" type
![Hill Mountain](./results/hill_mount.png)

### "Steep" type
![Steep Mountain](./results/steep_mount.png)

### Combinations of types
![Forest of mountains](./results/connected2.png)
![Forest of mountains](./results/connected3.png)
![Forest of mountains](./results/connected4.png)

### Timing

| map size and tile size | generation time, s | generation + visualization time, s | the result                                                   |
| ---------------------- | --------------- | ------------------------------- | ------------------------------------------------------------ |
| 1x1 x 8x8              | 0.00892         | 0.01078                         | <img src="results/1x1x8x8.jpg" style="zoom:67%;" /> |
| 1x1 x 16x16            | 0.11135         | 0.11398                         | <img src="results/1x1x16x16.jpg" style="zoom:67%;" /> |
| 1x1 x 32x32            | 1.84991         | 1.85417                         | <img src="results/1x1x32x32.jpg" style="zoom:67%;" /> |
| 4x4 x 8x8              | 0.09771         | 0.10152                         | <img src="results/4x4x8x8.jpg" style="zoom:67%;" /> |
| 4x4 x 16x16            | 1.30003         | 1.34257                         | <img src="results/4x4x16x16.jpg" style="zoom:67%;" /> |
| 7x7 x 8x8              | 0.39618         | 0.42008                         | <img src="results/7x7x8x8.jpg" style="zoom:67%;" /> |
| 7x7 x 16x16            | 5.30813         | 5.33290                         | <img src="results/7x7x16x16.jpg" style="zoom:67%;" /> |
