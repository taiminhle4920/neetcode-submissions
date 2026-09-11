class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        v = sum(nums)//k
        used = [False] * len(nums)
        nums.sort(reverse=True)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == v:
                return backtrack(0, k-1, 0)

            
            for c in range(i, len(nums)):
                if used[c] or subsetSum + nums[c] > v:
                    continue
                used[c] = True
                if backtrack(c+1, k, subsetSum+nums[c]):
                    return True
                used[c] = False
            return False
        
        return backtrack(0, k, 0)
        