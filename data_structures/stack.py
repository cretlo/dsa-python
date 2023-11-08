from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.prev: Node[T] | None = None

class Stack(Generic[T]):

    def __init__(self) -> None:
        self.length = 0
        self.head: Node[T] | None = None


    def push(self, value: T) -> None:
        node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = node
            return

        node.prev = self.head
        self.head = node
        return


    def pop(self) -> T | None:
        if self.head is None:
            return

        self.length -= 1
        removed_node = self.head 
        self.head = removed_node.prev
        removed_node.prev = None
        return removed_node.value

        

    def peek(self) -> T | None:
        if self.head is None:
            return

        return self.head.value 
