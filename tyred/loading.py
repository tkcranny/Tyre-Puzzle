from pathlib import Path

import networkx as nx

from .data import r, b, g
from .types import Puzzle, PlainGraph


class PuzzleLoader:
    def load_puzzle_from_file(self, spec_file: Path) -> Puzzle:
        with spec_file.open(mode="r") as fh_in:
            content = fh_in.read()
        return self.load_puzzle(content)

    def load_puzzle(self, spec: str) -> Puzzle:
        plain = self._get_plain_graph(spec)
        result = self._make_triple(plain)
        return result

    @staticmethod
    def _get_plain_graph(spec: str) -> PlainGraph:
        result: PlainGraph = nx.DiGraph()
        for line in spec.splitlines():
            if is_skippable(line):
                continue
            u, v, color = line.strip().split()
            result.add_edge(u, v, color=color)
        return result

    @classmethod
    def _make_triple(cls, plain: PlainGraph) -> Puzzle:
        result: Puzzle = nx.DiGraph()

        for node in plain.nodes():
            result.add_node((node, "red"))
            result.add_node((node, "blue"))
            result.add_node((node, "green"))

        cls._link_triple_graph_with_rbg_rules(plain=plain, triple=result)

        return result

    @staticmethod
    def _link_triple_graph_with_rbg_rules(plain: PlainGraph, triple: Puzzle) -> None:
        for u, v, data in plain.edges(data=True):
            c = data["color"]
            if c == "red":
                triple.add_edge(g(u), r(v))
                triple.add_edge(g(v), r(u))
            if c == "blue":
                triple.add_edge(r(u), b(v))
                triple.add_edge(r(v), b(u))
            if c == "green":
                triple.add_edge(b(u), g(v))
                triple.add_edge(b(v), g(u))


def is_skippable(line: str) -> bool:
    return line.strip() == "" or line.startswith("#")
