from itertools import product
from typing import Tuple

import networkx as nx

from .helpers import r, b, g
from .types import (
    ColorNode,
    Node,
    Puzzle,
    Solution,
)


class NoSolutionError(Exception):
    pass


def find_path(puzzle: Puzzle, start: str, goal: str) -> Solution:
    starts = _all_colors(start)
    goals = _all_colors(goal)

    solutions = []
    for s, g in product(starts, goals):
        try:
            pass
            solution = find_color_path(puzzle, s, g)
            solutions.append(solution)
        except NoSolutionError:
            pass

    if not solutions:
        raise NoSolutionError()

    return min(solutions, key=len)


def find_color_path(puzzle: Puzzle, start: ColorNode, goal: ColorNode) -> Solution:
    try:
        result = nx.shortest_path(puzzle, source=start, target=goal)
    except (nx.NodeNotFound, nx.NetworkXNoPath):
        raise NoSolutionError()
    return list(result)


def _all_colors(node: Node) -> Tuple[ColorNode, ...]:
    return (r(node), b(node), g(node))
