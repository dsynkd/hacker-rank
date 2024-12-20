def hourglassSum(arr):
    maxSum = float('-inf')
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            s = arr[i][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i-1][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            if s > maxSum: maxSum = s
    return maxSum
