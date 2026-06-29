class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        minV = float("inf")

        while l <= r:
            m = l + (r-l) //2
            minV = min(minV, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return min(minV, nums[l])