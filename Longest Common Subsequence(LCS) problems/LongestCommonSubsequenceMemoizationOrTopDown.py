"""
In Knapsack part i have writter bottom up as topdown so we needs to undo these things
topdown in memo+recursion one
"""


class solution:
    def main(self):
        # 5 is len of input1+1 and 6 is len of input2+1
        dp = [[-1]*(100) for _ in range(100)]

        def lcs(arr1, arr2):
            # think of smallest valid input for base case
            if len(arr1) == 0 or len(arr2) == 0:
                return 0
            # if already calculated
            if dp[len(arr1)][len(arr2)] != -1:
                return dp[len(arr1)][len(arr2)]
            # below section are solved by making choice diagram always decomose array from last
            elif arr1[-1] == arr2[-1]:
                # if we found one matching sequence then we have choice to count only upto [:-1] from both array
                dp[len(arr1)][len(arr2)] = 1+lcs(arr1[:-1], arr2[:-1])
                return dp[len(arr1)][len(arr2)]
            else:
                # if not found then we check for either one from which we can get max sub sequence
                dp[len(arr1)][len(arr2)] = max(
                    lcs(arr1, arr2[:-1]), lcs(arr1[:-1], arr2))
                return dp[len(arr1)][len(arr2)]
        return lcs(['a', 'b', 'c', 'h'], ['c', 'a', 'b', 'h', 'k'])


print(solution().main())
