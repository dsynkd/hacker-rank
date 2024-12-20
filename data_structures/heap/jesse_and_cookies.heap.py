# Approach: using heapq (MinHeap)
# Verdict: Pass

import heapq

def cookies(k: int, A: list[int]) -> int:
    ops = 0
    heapq.heapify(A)
    while A[0] < k and len(A) > 1:
        cookie1 = heapq.heappop(A)
        cookie2 = heapq.heappop(A)
        new_cookie = cookie1 + cookie2*2
        heapq.heappush(A, new_cookie)
        ops += 1
    if A[0] < k:
        return -1
    return ops
