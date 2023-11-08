import unittest
from data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue[int]()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.length, 3)

        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.peek(), 3)
        self.assertEqual(q.dequeue(), 3)

        self.assertEqual(q.length, 0)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.peek(), None)

        q.enqueue(1)
        self.assertEqual(q.length, 1)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), None)


        

        


if __name__ == "__main__":
    unittest.main()
