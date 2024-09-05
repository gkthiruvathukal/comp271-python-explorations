import unittest
from data_structures.trie_demo import Trie

class TestTrie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.trie = Trie()
        # Load words from the words.txt file in the data folder
        with open('data/words.txt', 'r') as file:
            words = file.read().splitlines()
            for word in words:
                cls.trie.insert(word)

    def test_search_common_words(self):
        # Test search for common words
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("banana"))
        self.assertTrue(self.trie.search("orange"))
        self.assertFalse(self.trie.search("notaword"))

    def test_starts_with_prefix(self):
        # Test prefix matching
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertFalse(self.trie.starts_with("xyz"))

if __name__ == '__main__':
    unittest.main()
