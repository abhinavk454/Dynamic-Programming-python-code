"""
 in top down DP we genrally converts recursive call to iterative call by the help of matrix
"""


class Solution:
    def main(self):
        def knapsack(wt, val, w, n):
            dp = [[None]*(w+1) for _ in range(n+1)]
            i = 0
            j = 0
            while i != w+1:
                dp[0][i] = 0
                i += 1
            while j != n+1:
                dp[j][0] = 0
                j += 1
            """
            i=n(on y axis) wt on y
            j=w(on x axis) size of bag on x
            """
            for i in range(1, n+1):
                for j in range(1, w+1):
                    if wt[i-1] <= j:
                        dp[i][j] = max(
                            (val[i-1]+dp[i-1][j-wt[i-1]]), dp[i-1][j])
                    elif wt[i-1] > j:
                        dp[i][j] = dp[i-1][j]
            for char in dp:
                print(char)

        knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7, 4)


Solution().main()
