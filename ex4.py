'''
Exercise 4 Lab 6 ENSF 338 (Complete)

'''

class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._max_heapify_down(i)

    def enqueue(self, value):
        self.heap.append(value)
        self._max_heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._max_heapify_down(0)
        return root

    def _max_heapify_up(self, index):
        parent_idx = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            self._max_heapify_up(parent_idx)

    def _max_heapify_down(self, index):
        left_child_idx = 2 * index + 1
        right_child_idx = 2 * index + 2
        largest = index

        if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[largest]:
            largest = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[largest]:
            largest = right_child_idx

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._max_heapify_down(largest)

    def display(self):
        print(self.heap)


# Tests
def test_sorted_heap():
    # Input array is already a sorted max heap
    input_array = [9, 4, 5, 1, 3, 2]
    expected_output = [9, 4, 5, 1, 3, 2]
    
    heap = MaxHeap()
    heap.heapify(input_array)
    
    print("Test Sorted Heap:")
    print("Expected:", expected_output)
    print("Actual:", heap.heap)
    
    assert heap.heap == expected_output, "Test failed: Sorted heap test"


def test_empty_heap():
    # Input array is empty
    input_array = []
    expected_output = []
    
    heap = MaxHeap()
    heap.heapify(input_array)
    
    print("Test Empty Heap:")
    print("Expected:", expected_output)
    print("Actual:", heap.heap)
    
    assert heap.heap == expected_output, "Test failed: Empty heap test"


def test_shuffled_heap():
    # Input array is a shuffled heap
    input_array = [3, 9, 2, 1, 4, 5]
    expected_output = [9, 4, 5, 1, 3, 2]
    
    heap = MaxHeap()
    heap.heapify(input_array)
    
    print("Test Shuffled Heap:")
    print("Expected:", expected_output)
    print("Actual:", heap.heap)
    
    assert heap.heap == expected_output, "Test failed: Shuffled heap test"


# Run tests
if __name__ == "__main__":
    test_sorted_heap()
    test_empty_heap()
    test_shuffled_heap()
    print("All tests passed.")
