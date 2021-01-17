from enum import Enum
from typing import List, Tuple, NewType

import networkx as nx


PlainGraph = NewType("PlainGraph", nx.DiGraph)  # type: ignore
Puzzle = NewType("TripleGraph", nx.DiGraph)  # type: ignore


Node = str
ColorNode = Tuple[str, str]
PrettyNode = Tuple[str, str]
Solution = List[PrettyNode]
