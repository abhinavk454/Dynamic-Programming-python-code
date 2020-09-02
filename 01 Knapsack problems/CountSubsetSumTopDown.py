def count(arr, k):
    """
    Same as 01 knapsack with value removed 
    so we will just ignore value term
    and make table of term those are reducing
    """
    dp = [[None]*(k+1) for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(1, len(dp[0])):
        dp[0][i] = 0
    for a in dp:
        print(a)
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    for a in dp:
        print(a)
    return dp[-1][-1]


print(count([1, 1, 2, 3, ], 4))
