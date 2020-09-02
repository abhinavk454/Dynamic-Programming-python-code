def soln(a):
    a_bar = a[::-1]
    dp = [[None]*(len(a)+1) for _ in range(len(a)+1)]
    """
    answer of this problem will be LCS common between a and abar
    """
    x, y = len(dp[0]), len(dp)

    def lcs(a, a_bar):
        # since x=y so we can set inintialization in only one step
        for i in range(y):
            dp[i][0] = 0
            dp[0][i] = 0
        for i in range(1, y):
            for j in range(1, x):
                if a[i-1] == a_bar[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    return lcs(a, a_bar)


print(soln(['a', 'g', 'b', 'c', 'b', 'a']))
