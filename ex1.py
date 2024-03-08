import timeit
import random as r

# Tree node definition
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

# Binary search tree using code from class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key, root=None):
        current = root or self.root
        while current is not None:
            if key == current.data:
                return current
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, key, root=None):
        current = root or self.root
        parent = None

        while current is not None:
            parent = current
            if key <= current.data:
                current = current.left
            else:
                current = current.right

        newnode = Node(key, parent)    
        if root is None:
            self.root = newnode
        elif key <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode

        return newnode

def build_tree(vectorSorted):
    binarySearch = BinarySearchTree()
    for i in vectorSorted:
        binarySearch.insert(i)
    return binarySearch

#use chatgpt
def performance(binarySearch, vectorSearch):
    avgTime = timeit.timeit(lambda: [binarySearch.search(i) for i in vectorSearch], number=10) / 10
    totalTime = avgTime * len(vectorSearch)
    return avgTime, totalTime
#enfofchatgpt

vectorSorted = list(range(1, 10000))
binarySearch = build_tree(vectorSorted)
avgTimeSorted, totalTimeSorted = performance(binarySearch, vectorSorted)

# Part 2
vectorShuffled = vectorSorted.copy()
r.shuffle(vectorShuffled)
binarySearchShuffled = build_tree(vectorShuffled)
avgTimeShuffled, totalTimeShuffled = performance(binarySearchShuffled, vectorShuffled)

print(f"Average Time of a search performance on sorted vector:  {avgTimeSorted}, Total Time: {totalTimeSorted}")
print(f"Average Timeof a Search performance on shuffled vector: {avgTimeShuffled}, Total Time: {totalTimeShuffled}")


# ANSWER to question 4
'''
After implementing binary search for both the sorted and shuffled vectors, the total and average times are almost the same. 
This similarity arises because the vector size is small. However, increasing the size of the vector will result
in less time for the sorted vector compared to the shuffled vector. 
This is because the sorted vector has a better time complexity than the shuffled vector. The time complexity of the sorted vector is O(log n)
while the time complexity of the shuffled vector is O(n).
'''


