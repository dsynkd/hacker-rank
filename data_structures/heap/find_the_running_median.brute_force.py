# Approach: using statistics.median
# Verdict: Fail (TLE)

import statistics

def runningMedian(a: list[int]) -> list[float]:
    medians = []

    for i in range(1, len(a)+1):
        medians.append(float(statistics.median(a[0:i])))
    return medians