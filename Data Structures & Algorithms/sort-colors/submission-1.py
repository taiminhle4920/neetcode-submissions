class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        cur = 0
        for i in range(len(nums)):
            while counter[cur] == 0:
                cur += 1
            nums[i] = cur
            counter[cur] -= 1
        
        