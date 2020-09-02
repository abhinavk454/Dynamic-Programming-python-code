"""
same approach as MCM just here ew also need to pass 4th argument that says is taht true or not

"""
# here three veriables are changing so 3D dp but we can optimeize it like this

dp = [[-1]*1001 for _ in range(1001)]
m = 1001


def soln(arr, i, j, isTrue):
    if i > j:
        return 0
    if i == j:
        if (isTrue == True):
            return arr[i] == "T"
        else:
            return arr[i] == "F"
    ans = 0
    if dp[i][j] != -1:
        return dp[i][j]
    # operator is at k and i,j denotes string/boolean
    for k in range(i+1, j, 2):
        lt = soln(arr, i, k-1, True)
        lf = soln(arr, i, k-1, False)
        rt = soln(arr, k+1, j, True)
        rf = soln(arr, k+1, j, False)
        if arr[k] == '|':
            if isTrue:
                ans = (ans+(lt*rf)+(rt*lf)+(lt*rt)) % m
            else:
                ans = (ans+(lf*rf)) % m
        elif arr[k] == '&':
            if isTrue:
                ans = (ans + (lt*rt)) % m
            else:
                ans = (ans + (lt*rf) + (rt*lf) + (rf*lf)) % m
        else:
            if isTrue:
                ans = (ans + (lt*rf) + (rt*lf)) % m
            else:
                ans = (ans + (lt*rt) + (lf*rf)) % m
    dp[i][j]=ans%m
    return dp[i][j]
