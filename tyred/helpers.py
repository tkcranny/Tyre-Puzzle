from .types import ColorNode, Node


def r(n: Node) -> ColorNode:
    """
    'Color' a label red.
    >>> r("A") == ("A", "red")
    """
    return (n, "red")


def b(n: Node) -> ColorNode:
    """
    'Color' a label blue.
    >>> b("A") == ("A", "blue")
    """
    return (n, "blue")


def g(n: Node) -> ColorNode:
    """
    'Color' a label green.
    >>> g("A") == ("A", "green")
    """
    return (n, "green")
