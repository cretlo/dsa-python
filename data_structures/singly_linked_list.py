from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):

    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

class SinglyLinkedList(Generic[T]):

    def __init__(self):
        self.length = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None


    def prepend(self, value: T) -> None:
        node = Node(value) 
        self.length += 1

        if (self.head is None):
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head = node
        return

    def append(self, value: T) -> None:
        node = Node(value)
        self.length += 1

        if (self.tail is None):
            self.tail = self.head = node
            return

        self.tail.next = node
        self.tail = node
        return


    def insert_at(self, value: T, idx: int) -> None:
        if (0 > idx > self.length):
            raise IndexError("Idx out of range")

        if (idx == self.length):
            self.append(value)
            return

        if (idx == 0):
            self.prepend(value)
            return

        assert self.head is not None

        curr = self.head
        count = 0

        while curr.next and count < idx:
            curr = curr.next
            idx += 1

        self.length += 1
        node = Node(value)
        node.next = curr.next
        curr.next = node
        return
        

    def remove(self, value: T) -> T | None:
        if (self.head is None):
            return

        if (self.head.value == value):
            return self.remove_at(0)

        curr = self.head


        while (curr.next is not None) and (curr.next.value != value):
            curr = curr.next

        if (curr.next is None):
            return

        self.length -= 1
        removed_node = curr.next
        curr.next = curr.next.next

        if curr.next is self.tail:
            self.tail = curr

        return removed_node.value


    def remove_at(self, idx: int) -> T:
        if (0 > idx >= self.length):
            raise IndexError("Idx out of range")

        assert self.head is not None

        removed_node = self.head

        if idx == 0:
            self.head = self.head.next
        else:
            curr = self.head
            count = 0

            while curr.next and count < idx - 1:
                curr = curr.next
                count += 1

            assert curr.next is not None

            removed_node = curr.next
            curr.next = removed_node.next

            if removed_node is self.tail:
                self.tail = curr

        self.length -= 1
        removed_node.next = None

        if self.length == 0:
            self.head = self.tail = None

        return removed_node.value


    def get(self, idx: int) -> T:
        if 0 > idx >= self.length:
            raise IndexError("Idx out of range")

        assert self.head is not None

        curr = self.head
        count = 0

        while curr.next and count != idx:
            curr = curr.next
            count += 1

        assert self.head is not None

        return curr.value
