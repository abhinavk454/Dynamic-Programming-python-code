"""
In Knapsack part i have writter bottom up as topdown so we needs to undo these things
topdown in memo+recursion one
"""


def lcs(arr1, arr2):
    # think of smallest valid input for base case
    if len(arr1) == 0 or len(arr2) == 0:
        return 0
    # below section are solved by making choice diagram always decomose array from last
    if arr2[-1] == arr1[-1]:
        # if we found one matching sequence then we have choice to count only upto [:-1] from both array
        return 1+lcs(arr1[:-1], arr2[:-1])
    else:
        # if not found then we check for either one from which we can get max sub sequence
        return max(lcs(arr1, arr2[:-1]), lcs(arr1[:-1], arr2))


print(lcs(['a', 'b', 'c', 'h'], ['c', 'a', 'b', 'h', 'k']))
