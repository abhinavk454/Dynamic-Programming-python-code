def sonl(arr, diff):
    sum_arr = sum(arr)
    """
    if we drive two subset  arr s1 ans s2 then
    for to have answer
    sum(s1)-sum(s2)==diff ----let eq(1)
    and also
    sum(s1)+sum(s2)==sum(arr) ---let eq(2)
    then adding both these equation
    we need to calucate how many subset exists with sum =(diff+sum(arr))//2
    """
    # below is similar to count subset sum
    sum_s1 = (diff+sum_arr)//2
    print(sum_s1)
    dp = [[None]*(sum_s1+1) for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(1, len(dp[0])):
        dp[0][i] = 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if arr[i-1] <= j:
                # i-1 weight reduced if selection choice else none
                dp[i][j]= dp[i-1][j-arr[i-1]]+dp[i-1][j]
            elif arr[i-1] > j:
                dp[i][j]= dp[i-1][j]
    return dp[-1][-1]


print(sonl([1, 1, 2, 3], 1))
