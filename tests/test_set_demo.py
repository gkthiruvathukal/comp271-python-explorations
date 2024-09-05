import unittest
from data_structures.set_demo import SetDemo

class TestSetDemo(unittest.TestCase):

    def setUp(self):
        self.set1 = SetDemo()
        self.set2 = SetDemo()

    def test_add_and_size(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set1.add(30)
        # Verify the size of the set after adding items
        self.assertEqual(self.set1.size(), 3)

    def test_remove(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set1.remove(10)
        # Verify item removal
        self.assertEqual(self.set1.size(), 1)
        with self.assertRaises(KeyError):
            self.set1.remove(100)  # Remove non-existing item

    def test_union(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set2.add(20)
        self.set2.add(30)
        union_set = self.set1.union(self.set2)
        # Verify the union of two sets
        self.assertEqual(union_set, {10, 20, 30})

    def test_intersection(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set2.add(20)
        self.set2.add(30)
        intersection_set = self.set1.intersection(self.set2)
        # Verify the intersection of two sets
        self.assertEqual(intersection_set, {20})

    def test_difference(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set2.add(20)
        self.set2.add(30)
        difference_set = self.set1.difference(self.set2)
        # Verify the difference of two sets
        self.assertEqual(difference_set, {10})

    def test_is_subset(self):
        self.set1.add(10)
        self.set1.add(20)
        self.set2.add(10)
        self.assertTrue(self.set2.is_subset(self.set1))
        self.assertFalse(self.set1.is_subset(self.set2))

if __name__ == '__main__':
    unittest.main()
    