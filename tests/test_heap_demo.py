import unittest
import random
from data_structures.heap_demo import HeapDemo

class TestHeapDemo(unittest.TestCase):

    def setUp(self):
        self.heap = HeapDemo()

    def test_insert_and_peek_min(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(5)
        # Verify that the smallest item is correct after inserting
        self.assertEqual(self.heap.peek_min(), 5)

    def test_remove_min(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(5)
        # Remove the smallest item and verify
        removed_item = self.heap.remove_min()
        self.assertEqual(removed_item, 5)
        # Verify that the next smallest is now at the top
        self.assertEqual(self.heap.peek_min(), 10)

    def test_heap_sort(self):
        items = random.sample(range(1, 101), 10)  # Generate 10 random numbers between 1 and 100
        sorted_items = self.heap.heap_sort(items[:])  # Pass a copy of the list to heap_sort
        # Verify that the list is sorted in ascending order
        self.assertEqual(sorted_items, sorted(items))

    def test_size(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(5)
        # Verify the size of the heap
        self.assertEqual(self.heap.size(), 3)

    def test_remove_min_empty(self):
        with self.assertRaises(IndexError):
            self.heap.remove_min()

    def test_peek_min_empty(self):
        with self.assertRaises(IndexError):
            self.heap.peek_min()

if __name__ == '__main__':
    unittest.main()
    