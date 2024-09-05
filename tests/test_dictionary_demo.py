import unittest
from data_structures.dictionary_demo import DictionaryDemo

class TestDictionaryDemo(unittest.TestCase):

    def setUp(self):
        self.dictionary = DictionaryDemo()

    def test_add_and_get(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("b", 2)
        # Verify that values are added and can be retrieved
        self.assertEqual(self.dictionary.get("a"), 1)
        self.assertEqual(self.dictionary.get("b"), 2)

    def test_update_value(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("a", 10)  # Update the value
        # Verify that the value is updated
        self.assertEqual(self.dictionary.get("a"), 10)

    def test_remove(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("b", 2)
        self.dictionary.remove("a")
        # Verify that the key is removed
        with self.assertRaises(KeyError):
            self.dictionary.get("a")
        # Ensure the other key is still present
        self.assertEqual(self.dictionary.get("b"), 2)

    def test_keys(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("b", 2)
        # Verify that the keys can be retrieved
        self.assertEqual(set(self.dictionary.keys()), {"a", "b"})

    def test_values(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("b", 2)
        # Verify that the values can be retrieved
        self.assertEqual(set(self.dictionary.values()), {1, 2})

    def test_size(self):
        self.dictionary.add("a", 1)
        self.dictionary.add("b", 2)
        # Verify the size of the dictionary
        self.assertEqual(self.dictionary.size(), 2)

    def test_remove_key_not_found(self):
        with self.assertRaises(KeyError):
            self.dictionary.remove("non_existing_key")

if __name__ == '__main__':
    unittest.main()
    