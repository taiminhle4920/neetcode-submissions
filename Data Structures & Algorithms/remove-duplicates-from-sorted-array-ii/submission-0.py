class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        for i in nums:
            if cur < 2 or i != nums[cur -2]:
                nums[cur] = i
                cur += 1
        return cur