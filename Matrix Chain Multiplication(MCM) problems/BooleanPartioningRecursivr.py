"""
same approach as MCM just here ew also need to pass 4th argument that says is taht true or not

"""


def soln(arr, i, j, isTrue):
    if i > j:
        return 0
    if i == j:
        if (isTrue == True):
            return arr[i] == "T"
        else:
            return arr[i] == "F"
    ans = 0
    # operator is at k and i,j denotes string/boolean
    for k in range(i+1, j, 2):
        lt = soln(arr, i, k-1, True)
        lf = soln(arr, i, k-1, False)
        rt = soln(arr, k+1, j, True)
        rf = soln(arr, k+1, j, False)
        if arr[k] == '|':
            if isTrue:
                ans = ans+(lt*rf)+(rt*lf)+(lt*rt)
            else:
                ans = ans+(lf*rf)
        elif arr[k] == '&':
            if isTrue:
                ans = ans + (lt*rt)
            else:
                ans = ans + (lt*rf) + (rt*lf) + (rf*lf)
        else:
            if isTrue:
                ans = ans + (lt*rf) + (rt*lf)
            else:
                ans = ans + (lt*rt) + (lf*rf)
    return ans
