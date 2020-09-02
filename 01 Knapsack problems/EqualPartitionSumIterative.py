class Solution:
    def canPartition(self, nums):
        sumnum=sum(nums)
        if sumnum%2!=0:
            return False
        k=sumnum//2
        def subset(nums,k):
            dp=[[None]*(k+1) for _ in range(len(nums)+1)]
            for i in range(len(dp)):
                dp[i][0]=True
            for i in range(1,len(dp[0])):
                dp[0][i]=False
            for i in range(len(dp)):
                for j in range(len(dp[0])):
                    if nums[i-1]<=j:
                        dp[i][j]=(dp[i-1][j-nums[i-1]])or(dp[i-1][j])
                    # not needed science no will not be greater than sum
                    # elif nums[i-1]>j:
                    #     dp[i][j]=dp[i-1][j]
            return dp[-1][-1]
        return subset(nums,k)