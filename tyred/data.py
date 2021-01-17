import networkx as nx

from .types import ColorNode, Node


def r(n: Node) -> ColorNode:
    return (n, "red")


def b(n: Node) -> ColorNode:
    return (n, "blue")


def g(n: Node) -> ColorNode:
    return (n, "green")
