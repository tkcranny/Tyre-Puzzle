import networkx as nx
import pytest

from tyred.data import get_graph
from tyred.puzzle import path


@pytest.fixture
def g() -> nx.DiGraph:
    return get_graph()


@pytest.mark.parametrize("goal", ["E", "I", "H"])
def test_get_to(g, goal):
    result = path(g, "A", goal)


@pytest.mark.parametrize(
    "start,goal,n",
    [
        ("A", "E", 2),
        ("A", "I", 3),
        ("A", "J", 4),
        ("A", "F", 7),
    ],
)
def test_hops(g, start, goal, n):
    result = path(g, start, goal)
    assert len(result) == n
