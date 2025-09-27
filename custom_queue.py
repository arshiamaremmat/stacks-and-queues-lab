# custom_queue.py
import random
from typing import Any, List, Optional

class Queue:
    """
    A simple FIFO queue backed by a Python list.
    Index 0 is the 'front' of the queue.
    """
    def __init__(self) -> None:
        self.items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        """Add an item to the end (rear) of the queue."""
        self.items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the item from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self) -> Any:
        """
        Return (without removing) the item at the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.items) == 0

    def select_and_announce_winner(self) -> str:
        """
        Randomly selects a winner from the queue.
        Dequeues everyone up to and including the winner.
        Returns the winning customer's name.

        Example:
          items = [A, B, C, D], winner randomly = C (index 2)
          After call -> items = [D] (A, B, C removed)
        """
        if self.is_empty():
            raise IndexError("cannot select winner from empty queue")

        winner_index = random.randrange(len(self.items))
        winner = self.items[winner_index]

        # Dequeue up to and including the winner:
        # Everything before winner_index plus the winner are removed.
        self.items = self.items[winner_index + 1 :]

        return winner
