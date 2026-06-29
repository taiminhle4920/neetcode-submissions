class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct  = []
        for i in nums:
            if i not in dct:
                dct.append(i)
            else:
                return True
        return False