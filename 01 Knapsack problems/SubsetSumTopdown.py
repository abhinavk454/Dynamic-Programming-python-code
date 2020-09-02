class Solution():
    def main(self):
        def ssum(arr, w):
            dp = [[None]*(w+1) for _ in range(len(arr)+1)]
            i, j = 0, 0
            # initializing condition
            # array on y axis while weight on x axis
            while i < len(dp):
                dp[i][0] = True
                i += 1
            while j < len(dp[0]):
                if dp[0][j] is None:
                    dp[0][j] = False
                j += 1
            for i in range(1, len(arr)+1):
                for j in range(1, w+1):
                    if arr[i-1] <= j:
                        # selecting choice not selecting choice
                        dp[i][j] = (dp[i-1][j-arr[i-1]]) or (dp[i-1][j])
                    else:
                        # selection not possible then
                        dp[i][j] = dp[i-1][j]
            for a in dp:
                print(a)

        print(ssum([1, 2, 3], 4))


Solution().main()
