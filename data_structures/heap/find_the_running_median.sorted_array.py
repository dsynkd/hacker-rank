# Approach: using bisect.insort
# Verdict: Pass

import bisect

def runningMedian(a: list[int]) -> list[float]:
    sorted = []
    medians = []

    for num in a:
        bisect.insort(sorted, num)

        if len(sorted) % 2 == 1:
            median = sorted[len(sorted)//2]
        else:
            median = (sorted[len(sorted)//2] + sorted[len(sorted)//2-1]) / 2

        medians.append(median)
    return medians

print(runningMedian([5,1,2,3,3,1,2]))