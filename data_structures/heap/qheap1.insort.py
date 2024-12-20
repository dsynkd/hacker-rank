# Sorted array implementation
# Not actually a heap but passes all tests

from bisect import insort

class Heap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        insort(self.heap, val)
    
    def delete(self, val):
        self.heap.remove(val)
    
    def minimum(self):
        if self.heap:
            print(self.heap[0])

q = int(input())
heap = Heap()
for _ in range(q):
    query = [int(i) for i in input().split(" ")]
    
    if query[0] == 1:
        heap.insert(query[1])
    elif query[0] == 2:
        heap.delete(query[1])
    elif query[0] == 3:
        heap.minimum()