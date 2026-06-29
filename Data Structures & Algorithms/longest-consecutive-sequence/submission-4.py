class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxl = 1
        temp = 1
        s = list({i for i in nums}) 
        s.sort()  



        for i in range(1, len(s)):
            if s[i] == s[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            if temp > maxl:
                maxl = temp
        return maxl
