class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i , v in enumerate(nums):
            sub =  target - v
            if sub in res:
                return [res[sub], i]
            res[v] = i
        return