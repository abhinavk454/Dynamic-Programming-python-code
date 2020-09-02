class Solution:
    def coinChange(self, coins, amount):
        dp = [[None]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(1, len(dp[0])):
            dp[0][j] = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j-coins[i-1]]+dp[i-1][j]
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
        for a in dp:
            print(a)
        return dp[-1][-1]
