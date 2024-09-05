class DictionaryDemo:
    def __init__(self):
        """Initialize an empty dictionary."""
        self.d = {}

    def add(self, key, value):
        """Add or update a key-value pair in the dictionary."""
        self.d[key] = value

    def remove(self, key):
        """Remove a key-value pair by key."""
        if key in self.d:
            del self.d[key]
        else:
            raise KeyError("Key not found in the dictionary")

    def get(self, key):
        """Retrieve the value for a given key."""
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError("Key not found in the dictionary")

    def keys(self):
        """Return all keys in the dictionary."""
        return list(self.d.keys())

    def values(self):
        """Return all values in the dictionary."""
        return list(self.d.values())

    def size(self):
        """Return the size of the dictionary."""
        return len(self.d)
    