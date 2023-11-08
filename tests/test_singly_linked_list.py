import unittest
from data_structures.singly_linked_list import Node, SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def test_node(self):
        node = Node(42)
        self.assertEqual(node.value, 42)
        self.assertEqual(node.next, None)

        node = Node("test")
        self.assertEqual(node.value, "test")


    def test_list(self):
        linked_list = SinglyLinkedList() 

        linked_list.append(2)
        linked_list.append(3)
        linked_list.prepend(1)
        self.assertEqual(linked_list.length, 3)

        self.assertEqual(linked_list.get(0), 1)
        self.assertEqual(linked_list.get(1), 2)
        self.assertEqual(linked_list.get(2), 3)

        self.assertEqual(linked_list.remove_at(2), 3)
        self.assertEqual(linked_list.remove(100), None)
        self.assertEqual(linked_list.remove(1), 1)
        self.assertEqual(linked_list.length, 1)
        self.assertEqual(linked_list.get(0), 2)
        self.assertEqual(linked_list.remove_at(0), 2)
        self.assertEqual(linked_list.length, 0)

        linked_list.insert_at(2, 0)
        linked_list.insert_at(3, 1)
        linked_list.insert_at(1, 0)

        self.assertEqual(linked_list.get(0), 1)
        self.assertEqual(linked_list.get(1), 2)
        self.assertEqual(linked_list.get(2), 3)
        self.assertEqual(linked_list.length, 3)



if __name__ == "__main__":
    unittest.main()
