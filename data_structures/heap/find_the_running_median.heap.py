# Approach: using a MaxHeap for upper bound and MinHeap for lower bound 
# Understanding this solution requires understanding how to
# do MaxHeap in python: https://stackoverflow.com/a/2501527
# Verdict: Pass

import heapq

def runningMedian(a: list[int]) -> list[float]:
    medians = [float(a[0])]
    lower = [-a[0]] # MaxHeap
    upper = [] # MinHeap

    for i in range(1, len(a)):
        item = a[i]
        if item > -lower[0]: # -lower[0] = maxheap.peek()
            heapq.heappush(upper, item)
        else:
            heapq.heappush(lower, -item)

        if len(lower) > len(upper)+1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower)+1:
            heapq.heappush(lower, -heapq.heappop(upper))

        median = 0.0
        if len(lower) == len(upper):
            median = (-lower[0] + upper[0]) / 2
        elif len(lower) > len(upper):
            median = float(-lower[0])
        else:
            median = float(upper[0])
        
        medians.append(median)
    return medians
