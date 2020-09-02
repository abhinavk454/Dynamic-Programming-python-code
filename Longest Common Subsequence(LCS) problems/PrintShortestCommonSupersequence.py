from collections import deque


def soln(a, b):
    # b on x axis a on y axis
    dp = [[None]*(len(b)+1) for _ in range(len(a)+1)]
    x, y = len(dp[0]), len(dp)
    # initialization part
    for i in range(y):
        dp[i][0] = 0
    for i in range(1, x):
        dp[0][i] = 0
    # filling rest matrix choice digram derived code
    for i in range(1, y):
        for j in range(1, x):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # printing part
    i, j = y-1, x-1
    ans = deque([])

    while (i > 0 and j > 0):
        if a[i-1] == b[j-1]:
            # if both are equal then take that element only once
            ans.appendleft(a[i-1])
            i -= 1
            j -= 1
        else:
            # always move towards bigger term
            if dp[i-1][j] > dp[i][j-1]:
                ans.appendleft(a[i-1])
                i -= 1
            # elif dp[i][j-1] > dp[i-1][j]:
            else:
                ans.appendleft(b[j-1])
                j -= 1
    # this section handles empty case
    while i > 0:
        ans.appendleft(a[i-1])
        i -= 1

    while j > 0:
        ans.appendleft(b[j-1])
        j -= 1

    return list(ans)


print(soln(['g', 'e', 'e', 'k'], ['e', 'k', 'e']))
