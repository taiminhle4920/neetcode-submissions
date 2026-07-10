class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_even = nums[0] % 2
        for i in range(1,len(nums)):
            if nums[i] % 2 == is_even:
                return False
            is_even = nums[i] % 2
        return True