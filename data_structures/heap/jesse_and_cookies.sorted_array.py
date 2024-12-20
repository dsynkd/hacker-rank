# Approach: using bisect.insort
# Verdict: TLE

import bisect

def cookies(k: int, A: list[int]) -> int:
    ops = 0
    A = sorted(A)
    while A[0] < k and len(A) > 1:
        cookie1 = A.pop(0)
        cookie2 = A.pop(0)
        new_cookie = cookie1 + cookie2*2
        bisect.insort(A, new_cookie)
        ops += 1
    if A[0] < k:
        return -1
    return ops