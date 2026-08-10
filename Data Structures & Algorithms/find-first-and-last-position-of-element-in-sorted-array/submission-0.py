class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, -1
        for i, v  in enumerate(nums):
            if v == target:
                r = i
                if l == -1:
                    l = i
        return [l, r]