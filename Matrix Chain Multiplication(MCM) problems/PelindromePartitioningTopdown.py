"""
same as MCM just here we have to select i from 0 
"""

dp = [[-1]*100 for _ in range(100)]


def soln(arr, i, j):
    def ispelindrome(arr, i, j):
        arr = arr[i:j+1]
        return arr == arr[::-1]
    if i >= j:  # sigle string is self pelindrome so o partitions
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if ispelindrome(arr, i, j):
        dp[i][j] = 0
        return 0
    min_a = 999999999
    for k in range(i, j):
        # store this if u want more optimised soln
        # last one is extra cost which is 1
        temp_a = soln(arr, i, k)+soln(arr, k+1, j)+1
        min_a = min(temp_a, min_a)
    dp[i][j] = min_a
    return dp[i][j]


print(soln(list('amana'), 0, 6))
