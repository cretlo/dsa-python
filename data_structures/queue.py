from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Node[T] | None = None


class Queue(Generic[T]):

    def __init__(self) -> None:
        self.length = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None


    def enqueue(self, value: T) -> None:
        node = Node(value)
        self.length += 1

        if self.tail is None:
            self.tail = self.head = node
            return

        self.tail.next = node
        self.tail = node
        return


    def dequeue(self) -> T | None:
        if self.head is None:
            return

        self.length -= 1 
        removed_node = self.head
        self.head = removed_node.next
        removed_node.next = None
        
        if self.head is None:
            self.head = self.tail = None

        return removed_node.value

    def peek(self) -> T | None:
        if self.head is None:
            return

        return self.head.value


