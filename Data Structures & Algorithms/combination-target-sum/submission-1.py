class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, arr, cur):
            if cur > target:
                return
            if cur == target:
                res.append(arr.copy())
                return
            
            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i, arr, cur + nums[i])
                arr.pop()
               
            
        backtrack(0,[], 0)
        return list(res)