import heapq

class HeapDemo:
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []

    def insert(self, item):
        """Add an item to the heap."""
        heapq.heappush(self.heap, item)

    def remove_min(self):
        """Remove and return the smallest item from the heap."""
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise IndexError("Remove from an empty heap")

    def peek_min(self):
        """Return the smallest item from the heap without removing it."""
        if self.heap:
            return self.heap[0]
        else:
            raise IndexError("Peek from an empty heap")

    def heap_sort(self, items):
        """Perform a heap sort and return a sorted list."""
        heapq.heapify(items)  # Convert the list to a heap
        sorted_list = []
        while items:
            sorted_list.append(heapq.heappop(items))
        return sorted_list

    def size(self):
        """Return the size of the heap."""
        return len(self.heap)
    