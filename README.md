# Tyre Puzzle

At a café in Toowoomba, some friends and I were intrigued by a
simple-looking puzzle made to entertain children. It was made of a
couple dozen tyres laid out, with coloured planks attaching adjacent
ones. The rules were simple: follow the planks in order of Red, Blue, Green, starting from the single tyre next to the rules board, and get to the raised tyre in the centre.

![](./images/puzzle.jpeg)

This repo contains a Python solution to the puzzle, using NetworX and a
few tricks.

## Getting Started

- Clone the repo
- Install the python dependencies with
  [Poetry](https://python-poetry.org), then enter a shell:
  ```
  $ poetry install
  $ poetry shell
  ```
- Use `solve.py` to find solutions, using puzzle files from `./puzzles`. E.g.:
  ```
  (tyre-puzzle) $ ./solve ./puzzle/puzzle_original.txt --start=A --goal=J
  ```
- Run tests with PyTest:
  ```
  (tyre-puzzle) $ pytest .
  ```
