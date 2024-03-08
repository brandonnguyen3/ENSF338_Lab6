'''
ENSF 338 Lab 6
Exercsie 2

Question 4
Discuss: which approach is faster? Why do you think is that? [0.2 pts]

Although both were quite fast, binary search in general tended to be faster than the BST. 
This is most likely because a BST needs to populate the results while binary search can just
search the results. In some situations it might make sense to have a BST structure if the 
design calls for it. However, if you are just looking to search for results in the fastest manner, 
going straight to binary search will generally be faster. 
'''

import random
import timeit

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = TreeNode(value)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

def build_tree_from_shuffled_array(array):
    bst = BinarySearchTree()
    for value in array:
        bst.insert(value)
    return bst

def measure_bst_performance(shuffled_array):
    bst = build_tree_from_shuffled_array(shuffled_array)
    total_time = 0
    for value in shuffled_array:
        start_time = timeit.default_timer()
        for _ in range(10):
            bst.search(value)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)
    average_time = total_time / len(shuffled_array)
    return average_time, total_time

def binary_search_in_sorted_array(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def measure_binary_search_performance(sorted_array):
    total_time = 0
    for value in sorted_array:
        start_time = timeit.default_timer()
        for _ in range(10):
            binary_search_in_sorted_array(sorted_array, value)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)
    average_time = total_time / len(sorted_array)
    return average_time, total_time

if __name__ == "__main__":
    sorted_vector = list(range(10000))
    random.shuffle(sorted_vector)

    bst_avg_time, bst_total_time = measure_bst_performance(sorted_vector)
    binary_search_avg_time, binary_search_total_time = measure_binary_search_performance(sorted_vector)

    print("BST average time:", bst_avg_time)
    print("BST total time:", bst_total_time)
    print("Binary search average time:", binary_search_avg_time)
    print("Binary search total time:", binary_search_total_time)
