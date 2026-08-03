class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        c0, c1 = 0, 0
        l, r = 0, 0
        res = 0
        while l <= r and r < len(nums):
            if nums[r] == 1:
                c1 += 1
            elif nums[r] == 0:
                c0 += 1
            
            if c0 <= k:
                res = max(res, c0 + c1)
            elif c0 > k:
                if nums[l] == 0:
                    c0 -= 1
                else:
                    c1 -= 1
                l += 1

            r += 1
        return res
            