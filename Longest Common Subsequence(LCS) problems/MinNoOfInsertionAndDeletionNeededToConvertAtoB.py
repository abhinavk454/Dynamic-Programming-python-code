# this is bottom up soln

def soln(a, b):
    dp = [[None]*(len(b)+1) for _ in range(len(a)+1)]
    """
    no of deletion will be len(a)-LCS from a
    no of insertion will be len(b)-LCS in b
    so total no of insertion and deletion will be (len(a)+len(b))-2*LCA
    """
    # initializing dp list with initial condition
    x_r = len(dp[0])
    y_r = len(dp)
    for i in range(y_r):
        dp[i][0] = 0
    for i in range(1, x_r):
        dp[0][i] = 0
    # a is on y axis and b on x
    for i in range(1, y_r):
        for j in range(1, x_r):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]  # case for smalling both array by 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return len(a)+len(b)-(2*(dp[-1][-1]))


print(soln(['h', 'e', 'a', 'p'], ['p', 'e', 'a']))
