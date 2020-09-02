# MCM
import sys
import math
"""
dimensions for n matrix is stored in array of n+1
so we needs to return min cost to multiply all matrix
approach is that we will find temp ans for each k in range i to j matlab samjh gaya na
step1 : find i,j genrally i=1 and j=-1
step2 : base condition
step3 :setup k for the loop
"""


class soln:
    def answ(self):
        dp = [[-1]*1001 for _ in range(1001)]

        def ans(arr, i, j):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_ans = math.inf
            for k in range(i, j):
                # temp1 +temp2 +ectra cost to multiply these two
                # (a1*b)*(b*c1)=a1*b*c1 cost in MCM
                temp_ans = ans(arr, i, k)+ans(arr, k+1, j) + \
                    arr[i-1]*arr[k]*arr[j]
                print(temp_ans)
                if (min_ans > temp_ans):
                    min_ans = temp_ans
            dp[i][j] = min_ans
            return dp[i][j]
        print(ans([40, 20, 30, 20, 30], 1, 4))


soln().answ()
