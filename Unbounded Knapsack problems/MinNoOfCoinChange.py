import math


class Solution:
    def coinChange(self, coins, amount):
        dp = [[None]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 0
        for j in range(1, len(dp[0])):
            dp[0][j] = 9999999  # if u use math.inf then use math.inf-1
        """
        in this we also need to fill 1 row of dp
        if j is divisible by coin[0]
        dp[1][j]=j//arr[0]
        else
        dp[1][j]=Math.inf
        """
        for j in range(1, len(dp[0])):
            if j % coins[0] == 0:
                dp[1][j] = j//coins[0]
            else:
                dp[1][j] = math.inf - 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if coins[i-1] <= j:
                    # if we chosse coin then add 1 scince you have chossen one coin
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1] != 9999999 else -1
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for coin in coins:
#             for x in range(coin, amount + 1):
#                 dp[x] = min(dp[x], dp[x - coin] + 1)
#         return dp[amount] if dp[amount] != float('inf') else -1
