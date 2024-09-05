import unittest
from data_structures.list_demo import ListDemo

class TestListDemo(unittest.TestCase):

    def setUp(self):
        self.lst = ListDemo()

    def test_add_and_get(self):
        self.lst.add(10)
        self.lst.add(20)
        # Confirm items were added correctly
        self.assertEqual(self.lst.get(0), 10)
        self.assertEqual(self.lst.get(1), 20)

    def test_remove_by_value(self):
        self.lst.add(10)
        self.lst.add(20)
        self.lst.remove(10)
        # Confirm the item was removed
        with self.assertRaises(IndexError):
            self.lst.get(1)  # Only one item should remain
        self.assertEqual(self.lst.get(0), 20)

    def test_remove_by_index(self):
        self.lst.add(10)
        self.lst.add(20)
        removed_item = self.lst.remove_at(0)
        # Confirm the correct item was removed
        self.assertEqual(removed_item, 10)
        self.assertEqual(self.lst.get(0), 20)

    def test_update(self):
        self.lst.add(10)
        self.lst.add(20)
        self.lst.update(0, 30)
        # Confirm the item was updated
        self.assertEqual(self.lst.get(0), 30)

    def test_size(self):
        self.lst.add(10)
        self.lst.add(20)
        # Confirm the size of the list
        self.assertEqual(self.lst.size(), 2)
        self.lst.remove_at(0)
        self.assertEqual(self.lst.size(), 1)

    def test_out_of_range_access(self):
        # Check out of range indexing and removing
        with self.assertRaises(IndexError):
            self.lst.get(0)
        with self.assertRaises(IndexError):
            self.lst.remove_at(0)

if __name__ == '__main__':
    unittest.main()
    