# Approach: using deque (Queue) and insort
# Verdict: TLE

import collections
import bisect

def cookies(k: int, A: list[int]) -> int:
    ops = 0
    q = collections.deque(sorted(A))
    while q[0] < k and len(q) > 1:
        cookie1 = q.popleft()
        cookie2 = q.popleft()
        new_cookie = cookie1 + cookie2*2
        bisect.insort(q, new_cookie)
        ops += 1
    if q[0] < k:
        return -1
    return ops
