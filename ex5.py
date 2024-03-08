#Part1:
class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        
        # If the list is empty or the new element has higher priority than the head
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and priority >= current.next.priority:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if not self.head:
            return None

        dequeued_value = self.head.value
        self.head = self.head.next
        return dequeued_value

#Part2:
class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        new_element = (priority, value)
        self.heap.append(new_element)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None

        # Swap the root with the last element
        self._swap(0, len(self.heap) - 1)

        # Remove the last element (previously the root)
        priority, value = self.heap.pop()

        # Restore the heap property by heapifying down
        if self.heap:
            self._heapify_down(0)

        return value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index][0] > self.heap[index][0]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#Part3
import random
import timeit

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and priority >= current.next.priority:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if not self.head:
            return None

        dequeued_value = self.head.value
        self.head = self.head.next
        return dequeued_value

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        new_element = (priority, value)
        self.heap.append(new_element)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        priority, value = self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index][0] > self.heap[index][0]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def generate_random_task_list(size):
    tasks = random.choices(['enqueue', 'dequeue'],
                           weights=[0.7, 0.3], k=size)
    return tasks

def measure_execution_time(priority_queue_class, tasks):
    pq = priority_queue_class()
    start_time = timeit.default_timer()

    for task in tasks:
        if task == 'enqueue':
            pq.enqueue(random.randint(1, 1000), random.randint(1, 100))  # Random values for enqueue
        elif task == 'dequeue':
            pq.dequeue()

    end_time = timeit.default_timer()
    overall_time = end_time - start_time
    average_time_per_task = overall_time / len(tasks)

    return overall_time, average_time_per_task

# Generate a random list of 1000 tasks
tasks = generate_random_task_list(1000)

# Measure execution time for ListPriorityQueue
list_pq_time, list_pq_avg_time = measure_execution_time(ListPriorityQueue, tasks)
print(f"ListPriorityQueue: Overall time - {list_pq_time:.6f} seconds, Average time per task - {list_pq_avg_time:.9f} seconds")

# Measure execution time for HeapPriorityQueue
heap_pq_time, heap_pq_avg_time = measure_execution_time(HeapPriorityQueue, tasks)
print(f"HeapPriorityQueue: Overall time - {heap_pq_time:.6f} seconds, Average time per task - {heap_pq_avg_time:.9f} seconds")
#Part 4
'''
The implementation with the heap works faster than the implementation using linked list this is because heap has the the complexity of O(log n) for insertion 
and deletion where as linked list has the complexity of O(n) for insertion and O(1) for deletion.
'''