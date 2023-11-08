import unittest
from data_structures.stack import Stack

class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack[int]()

        stack.push(3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(stack.length, 3)

        self.assertEqual(stack.pop(), 1)

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.length, 1)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.length, 0)


if __name__ == "__main__":
    unittest.main()
