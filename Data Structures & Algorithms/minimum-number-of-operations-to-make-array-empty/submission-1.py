class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 0
        count = Counter(nums)
        for k, v in count.items():
            if v < 2:
                return -1
            
            res += v // 3
            if v % 3 != 0:
                res += 1
        return res