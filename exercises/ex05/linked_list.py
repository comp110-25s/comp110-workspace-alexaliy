"""File to practice using recurisve function calls."""

__author__: str = "730483620"


class Node:
    """A node in a sinlge linked list."""

    value: int
    next: "Node | None"

    def __init__(self, val: int, next: "Node | None"):
        """Special method for initializing."""
        self.value = val
        self.next = next


def value_at(head: "Node | None", index: int) -> int:
    """Recursive functions for values."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: "Node | None") -> int:
    """Return the maximum value in the linked list recursively."""
    if head is None:
        raise ValueError("Cannont call max with None.")
    if head.next is None:
        return head.value

    max_rest = max(head.next)
    if head.value > max_rest:
        return head.value
    else:
        return max_rest


def linkify(items: list[int]) -> "Node | None":
    """Recursive function for a list of Nodes."""
    if not items:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: "Node | None", factor: int) -> "Node | None":
    """Recursive function with scaling factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
