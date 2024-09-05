class SetDemo:
    def __init__(self):
        """Initialize an empty set."""
        self.s = set()

    def add(self, item):
        """Add an item to the set."""
        self.s.add(item)

    def remove(self, item):
        """Remove an item from the set if present."""
        if item in self.s:
            self.s.remove(item)
        else:
            raise KeyError("Item not found in the set")

    def union(self, other_set):
        """Return the union of the current set and another set."""
        return self.s.union(other_set.s)

    def intersection(self, other_set):
        """Return the intersection of the current set and another set."""
        return self.s.intersection(other_set.s)

    def difference(self, other_set):
        """Return the difference of the current set and another set."""
        return self.s.difference(other_set.s)

    def is_subset(self, other_set):
        """Check if the current set is a subset of another set."""
        return self.s.issubset(other_set.s)

    def size(self):
        """Return the size of the set."""
        return len(self.s)
    