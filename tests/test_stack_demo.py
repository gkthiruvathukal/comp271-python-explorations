import unittest
from data_structures.stack_demo import StackDemo

class TestStackDemo(unittest.TestCase):

    def setUp(self):
        self.stack = StackDemo()

    def test_push_and_peek(self):
        self.stack.push(10)
        self.stack.push(20)
        # Verify the top item is correct after pushing
        self.assertEqual(self.stack.peek(), 20)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        popped_item = self.stack.pop()
        # Verify the popped item and the new top of the stack
        self.assertEqual(popped_item, 20)
        self.assertEqual(self.stack.peek(), 10)

    def test_is_empty(self):
        # Verify the stack is initially empty
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        # After pushing, the stack should no longer be empty
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        # Add items and verify the size
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty(self):
        # Verify popping from an empty stack raises an exception
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        # Verify peeking into an empty stack raises an exception
        with self.assertRaises(IndexError):
            self.stack.peek()

if __name__ == '__main__':
    unittest.main()
    