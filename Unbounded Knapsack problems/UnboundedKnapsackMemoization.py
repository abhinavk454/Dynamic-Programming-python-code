class soln:
    def main(self):
        # we will store -1 where we dont know soln and value where we knows the soln
        dp = [[-1]*100 for _ in range(100)]

        def knapsack(wt, val, w, n):
            if w == 0 or n == 0:
                return 0
            # if value is already calculated tehn we will retuern that
            if dp[n][w] != -1:
                return dp[n][w]
            if w >= wt[-1]:
                # stores choice returns weather iter selected or not which one gives max profit
                dp[n][w] = max((val[-1]+knapsack(wt, val,
                                                 w-wt[-1], n-1)), knapsack(wt[:-1], val[:-1], w, n-1))
                return dp[n][w]
            elif w < wt[-1]:
                # item will not be selected
                dp[n][w] = knapsack(wt[:-1], val[:-1], w, n-1)
                return dp[n][w]
        print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))


soln().main()
