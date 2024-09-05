import unittest
from data_structures.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_insert_and_display(self):
        self.linked_list.insert(10)
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        # Verify the elements are inserted and displayed correctly
        self.assertEqual(self.linked_list.display(), [10, 20, 30])

    def test_remove(self):
        self.linked_list.insert(10)
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.remove(20)
        # Verify the element is removed correctly
        self.assertEqual(self.linked_list.display(), [10, 30])

    def test_search(self):
        self.linked_list.insert(10)
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        # Verify search works
        self.assertTrue(self.linked_list.search(20))
        self.assertFalse(self.linked_list.search(40))

    def test_size(self):
        self.linked_list.insert(10)
        self.linked_list.insert(20)
        # Verify the size of the linked list
        self.assertEqual(self.linked_list.size(), 2)
        self.linked_list.remove(10)
        self.assertEqual(self.linked_list.size(), 1)

    def test_remove_value_not_found(self):
        self.linked_list.insert(10)
        with self.assertRaises(ValueError):
            self.linked_list.remove(30)

if __name__ == '__main__':
    unittest.main()
    