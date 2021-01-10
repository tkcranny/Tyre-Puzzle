from itertools import product
from typing import List, Tuple

import networkx as nx

from .data import (
    GOAL,
    NODE_INDEX,
    NODES,
    START,
    ColorNode,
    Node,
    b,
    g,
    get_graph,
    get_graph_with_missing_green_plank,
    r,
)

PrettyNode = Tuple[str, str]
Solution = List[PrettyNode]


class NoSolutionError(Exception):
    pass


def pretty_node(n: ColorNode) -> PrettyNode:
    *qr, c = n
    letter = NODE_INDEX[tuple(qr)]
    return letter, c


def _color_path(triple: nx.DiGraph, start: ColorNode, goal: ColorNode) -> Solution:
    try:
        result = nx.shortest_path(triple, start, goal)
    except:
        raise NoSolutionError()
    return list(map(pretty_node, result))


def _all_colors(n: Node) -> Tuple[ColorNode, ...]:
    return b(n), r(n), g(n)


def path(triple: nx.DiGraph, start: str, goal: str) -> Solution:
    starts = _all_colors(NODES[start])
    goals = _all_colors(NODES[goal])

    solutions = []
    for s, g in product(starts, goals):
        try:
            solution = _color_path(triple, s, g)
            solutions.append(solution)
        except NoSolutionError:
            pass

    if not solutions:
        raise NoSolutionError()

    return min(solutions, key=len)


def main() -> None:
    triple = get_graph_with_missing_green_plank()
    print(f"running with {len(triple)} nodes and {len(triple.edges())} edges")

    result = path(triple, "A", "T")
    print(f"Solution found with {len(result)} steps")
    for step in result:
        print(step)


if __name__ == "__main__":
    main()
