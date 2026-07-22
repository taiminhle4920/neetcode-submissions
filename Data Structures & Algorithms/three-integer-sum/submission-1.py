class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while  nums[k] == nums[k + 1] and j < k:
                        k -= 1
                    
                elif cur > 0:
                    k -= 1
                else:
                    j += 1
        return res
                