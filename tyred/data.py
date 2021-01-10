from typing import Dict, List, Tuple

import networkx as nx

from .types import ColorNode, Node, blue, green, red

# Nodes
A = START = (-4, 4)
B = 0, -3
C = 1, -3
D = 2, -3
E = 3, -3
F = -1, -2
G = 0, -2
H = 1, -2
I = 2, -2
J = 3, -2
K = -2, -1
L = -1, -1
M = 0, -1
N = 1, -1
O = 2, -1
P = 3, -1
Q = -3, 0
R = -2, 0
S = -1, 0
T = GOAL = 0, 0
U = 1, 0
V = 2, 0
W = 3, 0
X = -3, 1
Y = -2, 1
Z = -1, 1
AA = 0, 1
AB = 1, 1
AC = 2, 1
AD = -3, 2
AE = -2, 2
AF = -1, 2
AG = 0, 2
AH = 1, 2
AI = -3, 3
AJ = -2, 3
AK = -1, 3
AL = 0, +3


NODES: Dict[str, Node] = {
    k: v for k, v in locals().items() if k.isupper() and len(k) <= 2
}
NODE_INDEX = {v: k for k, v in NODES.items()}

RAW_EDGES: List[Tuple[int, int, str]] = [
    (A, E, red),
    # -3 Hotizontal
    (B, C, blue),
    (C, D, red),
    (D, E, green),
    # -3 to -2 diagonals
    (B, F, red),
    (B, G, green),
    (C, G, blue),
    (C, H, green),
    (D, H, blue),
    (D, I, red),
    (E, I, blue),
    (E, J, red),
    # -2 horizontals
    (F, G, red),
    (G, H, red),
    (H, I, green),
    (I, J, green),
    # -2 to -1 diagonals
    (F, K, blue),
    (F, L, green),
    (G, L, blue),
    (G, M, green),
    (H, M, red),
    (H, N, blue),
    (I, N, red),
    (I, O, green),
    (J, O, blue),
    (J, P, green),
    # -1 Horizontals
    (K, L, red),
    (L, M, blue),
    (M, N, blue),
    (N, O, red),
    (O, P, blue),
    # -1 to 0 Diagonals
    (K, Q, green),
    (K, R, red),
    (L, R, red),
    (L, S, red),
    (M, S, green),
    (N, U, green),
    (O, U, blue),
    (O, V, green),
    (P, V, blue),
    (P, W, red),
    # 0 Horizontals
    (Q, R, red),
    (R, S, blue),
    (U, V, blue),
    (V, W, blue),
    # 0 to 1 Diagonals
    (Q, X, blue),
    (R, X, red),
    (R, Y, green),
    (S, Y, green),
    (S, Z, blue),
    (T, Z, red),
    (U, AA, red),
    (U, AB, blue),
    (V, AB, green),
    (V, AC, red),
    (W, AC, green),
    # +1 Horiztontal
    (X, Y, red),
    (Y, Z, blue),
    (Z, AA, red),
    # MISSING GREEN PLANK: AA to AB
    (AB, AC, blue),
    # +1 to +2 diagonal
    (X, AD, green),
    (Y, AD, blue),
    (Y, AD, blue),
    (Y, AE, blue),
    (Z, AE, green),
    (Z, AF, red),
    (AA, AF, blue),
    (AA, AG, red),
    (AB, AG, green),
    (AB, AH, red),
    (AC, AH, green),
    # +2 horizontals
    (AD, AE, blue),
    (AE, AF, blue),
    (AF, AG, blue),
    (AG, AH, red),
    # +2 to +3 Diagonals
    (AD, AI, red),
    (AE, AI, blue),
    (AE, AJ, red),
    (AF, AJ, blue),
    (AF, AK, green),
    (AG, AK, blue),
    (AG, AL, green),
    (AH, AL, blue),
    # +3 HORIZONTAL
    (AI, AJ, green),
    (AJ, AK, blue),
    (AK, AL, red),
]


def get_plain_graph() -> nx.Graph:
    result = nx.Graph()
    for u, v, color in RAW_EDGES:
        result.add_edge(u, v, color=color)
    return result


def get_plain_graph_with_missing_plank() -> nx.Graph:
    result = get_plain_graph()
    result.add_edge(AA, AB, color=green)
    return result


# Add colour dimensions.


def r(n: Node) -> ColorNode:
    return (*n, red)


def b(n: Node) -> ColorNode:
    return (*n, blue)


def g(n: Node) -> ColorNode:
    return (*n, green)


GREEN_START = g(START)
RED_GOAL = r(GOAL)


def get_triple_graph(plain: nx.Graph) -> nx.DiGraph:
    result = nx.DiGraph()
    for n in plain.nodes():
        result.add_node(r(n))
        result.add_node(g(n))
        result.add_node(b(n))

    _link_triple_graph_with_rbg_rules(plain, result)

    return result


def _link_triple_graph_with_rbg_rules(plain: nx.Graph, triple: nx.DiGraph) -> None:
    for u, v, data in plain.edges(data=True):
        c = data["color"]
        if c == red:
            triple.add_edge(g(u), r(v))
            triple.add_edge(g(v), r(u))
        if c == blue:
            triple.add_edge(r(u), b(v))
            triple.add_edge(r(v), b(u))
        if c == green:
            triple.add_edge(b(u), g(v))
            triple.add_edge(b(v), g(u))


def get_graph() -> nx.DiGraph:
    plain = get_plain_graph()
    result = get_triple_graph(plain)
    return result


def get_graph_with_missing_green_plank() -> nx.DiGraph:
    plain = get_plain_graph_with_missing_plank()
    result = get_triple_graph(plain)
    return result
