def sonl(wt, val, w, n):
    dp = [[None]*(w+1) for _ in range(len(wt)+1)]
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(1, len(dp[0])):
        dp[0][i] = 0
    # j is size of bag i is wt
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if wt[i-1] <= j:
                # change is only when if select itam for 01 knapsack if we not take item one then we never take it again
                dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]], dp[i-1][j])
            elif wt[i-1] > j:
                dp[i][j] = dp[i-1][j]
    for a in dp:
        print(a)


sonl([1, 2, 3, 4], [1, 4, 5, 7], 5, 4)
