class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dpn = [-1] * len(nums)
        dpn[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] * nums[i], nums[i], dpn[i-1] * nums[i])
            dpn[i] = min(dp[i-1] * nums[i], nums[i],dpn[i-1] * nums[i])
        return max(dp)