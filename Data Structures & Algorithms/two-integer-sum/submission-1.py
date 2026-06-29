class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            if nums[i] in ht:
                return [ht[nums[i]], i]
            
            val = target - nums[i]
            ht[val] = i
        return []