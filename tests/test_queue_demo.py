import unittest
from data_structures.queue_demo import QueueDemo

class TestQueueDemo(unittest.TestCase):

    def setUp(self):
        self.queue = QueueDemo()

    def test_enqueue_and_peek(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        # Verify the front item is correct after enqueuing
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        dequeued_item = self.queue.dequeue()
        # Verify the dequeued item and the new front of the queue
        self.assertEqual(dequeued_item, 10)
        self.assertEqual(self.queue.peek(), 20)

    def test_is_empty(self):
        # Verify the queue is initially empty
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        # After enqueuing, the queue should no longer be empty
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        # Add items and verify the size
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue_empty(self):
        # Verify dequeuing from an empty queue raises an exception
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty(self):
        # Verify peeking into an empty queue raises an exception
        with self.assertRaises(IndexError):
            self.queue.peek()

if __name__ == '__main__':
    unittest.main()
    