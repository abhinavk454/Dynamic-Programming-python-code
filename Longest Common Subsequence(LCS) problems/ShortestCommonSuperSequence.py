"""

this is same as longest common subsequence
if we substract LCS length from both the string length of both string concatinated
since lcs strings appears twice in worst cast for elimanting one worst case it will 
give best answer

"""


def ans(arr1, arr2):
    dp = [[None]*(len(arr2)+1) for _ in range(len(arr1)+1)]
    total = len(arr1)+len(arr2)
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(1, len(dp[0])):
        dp[0][i] = 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return total-dp[-1][-1]


print(ans(['g', 'e', 'e', 'k'], ['e', 'k', 'e']))
