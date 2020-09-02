"""
same as MCM just here we have to select i from 0 
"""


def soln(arr, i, j):
    def ispelindrome(arr, i, j):
        arr = arr[i:j+1]
        return arr == arr[::-1]
    if i >= j:  # sigle string is self pelindrome so o partitions
        return 0
    if ispelindrome(arr, i, j):
        return 0
    min_a = 999999999
    for k in range(i, j):
        # last one is extra cost which is 1
        temp_a = soln(arr, i, k)+soln(arr, k+1, j)+1
        min_a = min(temp_a, min_a)
    return min_a


print(soln(['n', 'i', 't', 'i', 'n'], 0, 4))
