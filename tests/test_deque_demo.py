import unittest
from data_structures.deque_demo import DequeDemo

class TestDequeDemo(unittest.TestCase):

    def setUp(self):
        self.deque = DequeDemo()

    def test_add_to_front_and_back(self):
        self.deque.add_to_front(10)
        self.deque.add_to_back(20)
        self.assertEqual(self.deque.peek_front(), 10)
        self.assertEqual(self.deque.peek_back(), 20)

    def test_remove_from_front_and_back(self):
        self.deque.add_to_front(10)
        self.deque.add_to_back(20)
        self.assertEqual(self.deque.remove_from_front(), 10)
        self.assertEqual(self.deque.remove_from_back(), 20)

    def test_update_front_and_back(self):
        self.deque.add_to_front(10)
        self.deque.add_to_back(20)
        self.deque.update_front(30)
        self.deque.update_back(40)
        self.assertEqual(self.deque.peek_front(), 30)
        self.assertEqual(self.deque.peek_back(), 40)

    def test_size(self):
        self.deque.add_to_front(10)
        self.deque.add_to_back(20)
        self.assertEqual(self.deque.size(), 2)
    
    def test_remove_from_empty(self):
        with self.assertRaises(IndexError):
            self.deque.remove_from_front()
        with self.assertRaises(IndexError):
            self.deque.remove_from_back()

    def test_update_empty(self):
        with self.assertRaises(IndexError):
            self.deque.update_front(1)
        with self.assertRaises(IndexError):
            self.deque.update_back(1)

if __name__ == '__main__':
    unittest.main()
    