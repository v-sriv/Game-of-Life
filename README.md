# John Conway's Game of Life
John Conway's Game of Life (also simply known as Game of Life) is characterised as a cellular automaton. It's a zero player game, where the evolution of the game depends entirely and solely upon the initial state.

## Description
One interacts with the Game of Life by creating an initial configuration and observing how it evolves in discrete time steps called generations. There is no limit to the number of generations (computational resources permitting) nor is there a win condition.

The Game of Life is played on an infinite square grid, with each cell being in one of two states: live or dead. Cells in configurations called patterns evolve over generations according to the number of live and dead cells in their Moore neighborhood, that is, the eight cells in their immediate proximity.

The rules which are followed and decides the fate of the evolution of a cell, or a cluster, in the subsequent generation are described below:
```
- Any live cell with fewer than two live neighbours dies, as if by underpopulation
- Any live cell with two or three live neighbours lives on to the next generation
- Any live cell with more than three live neighbours dies, as if by overpopulation
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
```

![Represenation of the project.](./Game%20of%20Life.gif)

## References
- [Wikipedia - John Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)