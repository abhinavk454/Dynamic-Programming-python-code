def soln(arr1, arr2):
    dp = [[None]*(len(arr2)+1) for _ in range(len(arr1)+1)]
    # initializing the base case fo dp array on x axis arr2 on y axis arr1
    # if len(arr)==0 or len(arr2)==0 return 0
    for i in range(len(dp)):
        dp[i][0] = 0
    for i in range(len(dp[0])):
        dp[0][i] = 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if arr1[i-1] == arr2[j-1]:
                # in case ele of bot arr are equal
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                # if ele not equal then 0 main diffrence is here from standerd LCS
                dp[i][j] = 0
    maxi=0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j]>maxi:
                maxi=dp[i][j]
    return maxi


print(soln(['a', 'b', 'c', 'h'], ['c', 'a', 'b', 'h', 'k']))
