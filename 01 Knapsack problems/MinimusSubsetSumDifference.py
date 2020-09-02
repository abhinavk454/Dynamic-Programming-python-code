def minsumdiff(arr):
    """
    we will find range such that if we partion the array in two part then we calucalte in what range
    these partition will occurs
    """
    rang = sum(arr)
    """
    then will will find subset sum upto range for len of array on yaxis
    """
    dp = [[None]*(rang+1) for _ in range(len(arr))]
    for i in range(len(dp)):
        dp[i][0] = True
    for j in range(1, len(dp[0])):
        dp[0][i] = False
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j-arr[i-1]]) or (dp[i-1][j])
            elif arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
    # we will consider only upto for 1/2 range element
    midd = len(dp[0])//2
    ans = []
    for i in range(midd):
        if dp[-1][i] == True:
            ans.append(i)
    print(ans)
    """
     for ans will minimize the to partition sum 
     let partition name be s1 and s2
     then both will be within the range
     so s2=range-s1
     hence we need to find min of (range-s1-s1)=min(range-2*s1)
    """
    mins=9999999
    for i in range(len(ans)):
        mins=min(mins,rang-(2*ans[i]))
    return mins


print(minsumdiff([1, 2, 7]))
