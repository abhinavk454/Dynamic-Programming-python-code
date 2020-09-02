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


def ans(arr, i, j):
    if i >= j:
        return 0
    min_ans = math.inf
    for k in range(i, j):
        # temp1 +temp2 +ectra cost to multiply these two
        # (a1*b)*(b*c1)=a1*b*c1 cost in MCM
        temp_ans = ans(arr, i, k)+ans(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        print(temp_ans)
        if (min_ans > temp_ans):
            min_ans = temp_ans
    return min_ans


print(ans([40, 20, 30, 20, 30], 1, 4))
# A naive recursive implementation that
# simply follows the above optimal
# substructure property

# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n


# def MatrixChainOrder(p, i, j):
#     if i >= j:
#         return 0
#     _min = sys.maxsize
#     # place parenthesis at different places
#     # between first and last matrix,
#     # recursively calculate count of
#     # multiplications for each parenthesis
#     # placement and return the minimum count
#     for k in range(i, j):
#         count = (MatrixChainOrder(p, i, k)
#                  + MatrixChainOrder(p, k + 1, j)
#                  + p[i-1] * p[k] * p[j])
#         if count < _min:
#             _min = count
#     # Return minimum count
#     return _min


# # Driver program to test above function
# arr = [1, 2, 3, 4, 3]
# n = len(arr)

# print("Minimum number of multiplications is ",
#       MatrixChainOrder(arr, 1, n-1))
