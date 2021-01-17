#!/usr/bin/env python3

from pathlib import Path

import click

from tyred.loading import PuzzleLoader
from tyred.solving import NoSolutionError, find_path
from tyred.types import Solution


@click.command()
@click.argument("spec", type=click.Path(exists=True))
@click.option("--start", default="A")
@click.option("--goal", default="T")
def main(spec, start: str, goal: str) -> None:
    puzzle = PuzzleLoader().load_puzzle_from_file(Path(spec))
    click.echo(f"Puzzle has {len(puzzle)} nodes and {len(puzzle.edges())} edges")
    click.echo(f"Finding solution from {start} to {goal}")

    try:
        solution = find_path(puzzle, start=start, goal=goal)
    except NoSolutionError:
        raise click.ClickException(f"No solution between {start} and {goal} possible")
    click.echo(f"Solution found with {len(solution)} steps")
    print_solution(solution)


def print_solution(solution: Solution) -> None:
    click.secho(solution[0][0], nl=False)
    for node, color in solution[1:]:
        click.secho("➜", fg=color, nl=False)
        click.secho(node, nl=False)
    click.secho()


if __name__ == "__main__":
    main()
