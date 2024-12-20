# Array-based implementation
# Verdict: TLE

from typing import Optional


class MinHeap:

    heap = []

    def __init__(self, nums: list[int] = []):
        self.heap = self._heapify(nums)
    
    def peek(self) -> Optional[int]:
        if not self.heap:
            return None
        return self.heap[0]

    def pop(self) -> Optional[int]:
        if not self.heap:
            return None
        root = self.heap[0]
        bottom = self.heap.pop()
        if self.heap:
            self.heap[0] = bottom
            self._siftDown()
        return root

    def push(self, node: int):
        self.heap.append(node)
        self._swim()

    def delete(self, item: int):
        lastItem = self.heap.pop()
        if item == lastItem:
            return
        for i in range(len(self.heap)):
            if self.heap[i] == item:
                self.heap[i] = lastItem
                break
        if self._hasParentNode(i):
            p = self._getParentNodeIndex(i)
            if self.heap[i] > self.heap[p]:
                self._sink(i)
            else:
                self._swim(i)
        else:
            self._sink(i)

    def _getLeftNodeIndex(self, index: int) -> int:
        return index * 2 + 1
    
    def _getRightNodeIndex(self, index: int) -> int:
        return index * 2 + 2
    
    def _getParentNodeIndex(self, index: int) -> int:
        return (index - 1) // 2

    def _hasLeftNode(self, index: int, heap: Optional[list] = None) -> bool:
        heap = heap or self.heap
        return self._getLeftNodeIndex(index) < len(heap)
    
    def _hasRightNode(self, index: int, heap: Optional[list] = None) -> bool:
        heap = heap or self.heap
        return self._getRightNodeIndex(index) < len(heap)

    def _hasParentNode(self, index: int, heap: Optional[list] = None) -> bool:
        heap = heap or self.heap
        return self._getParentNodeIndex(index) >= 0

    def _getMinChildIndex(self, index: int, heap: Optional[list]) -> int:
        heap = heap or self.heap
        if self._hasRightNode(index, heap):
            l = self._getLeftNodeIndex(index)
            r = self._getRightNodeIndex(index)
            if heap[l] < heap[r]:
                return l
            else:
                return r
        elif self._hasLeftNode(index, heap):
            return self._getLeftNodeIndex(index)
        else:
            return -1

    def _heapify(self, nums: Optional[list[int]] = None) -> list[int]:
        heap = nums or self.heap
        i = len(heap)-1
        while i >= 0:
            self._sink(i, heap)
            i -= 1
        return heap
    
    # "Heapify Down" or "Shift Down"
    def _sink(self, index = 0, heap: Optional[list[int]] = None):
        heap = heap or self.heap
        while (m := self._getMinChildIndex(index, heap)) >= 0:
            if heap[index] > heap[m]:
                heap[index], heap[m] = heap[m], heap[index]
            index = m
    
    # "Heapify Up" or "Shift Up"
    def _swim(self, index = -1, heap: Optional[list[int]] = None):
        heap = heap or self.heap
        if index == -1:
            index = len(heap)-1
        while (p := self._getParentNodeIndex(index)) >= 0:
            if heap[p] > heap[index]:
                heap[index], heap[p] = heap[p], heap[index]
            index = p

    def __str__(self) -> str:
        return str(self.heap)

heap = MinHeap()
q = int(input())
for i in range(q):
    line = input().split(" ")
    cmd = int(line[0])
    if cmd == 1:
        arg = int(line[1])
        heap.push(arg)
    elif cmd == 2:
        arg = int(line[1])
        heap.delete(arg)
    elif cmd == 3:
        print(heap.peek())