class Solution:
    def canPartition(self, nums):
        sumnum = sum(nums)
        if sumnum % 2 != 0:
            return False
        k = sumnum//2

        def subset(nums, k):
            if not nums:
                return False
            if sum(nums) == k:
                return True
            elif nums[-1] <= k:
                return subset(nums[:-1], k-nums[-1]) or subset(nums[:-1], k)
            else:
                return subset(nums[:-1], k)
        return subset(nums, k)
