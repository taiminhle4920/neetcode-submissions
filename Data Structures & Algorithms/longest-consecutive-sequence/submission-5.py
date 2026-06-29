class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # maxl = 1
        # temp = 1
        # s = list({i for i in nums}) 
        # s.sort()  
        # for i in range(1, len(s)):
        #     if s[i] == s[i - 1] + 1:
        #         temp += 1
        #     else:
        #         temp = 1
        #     if temp > maxl:
        #         maxl = temp
        # return maxl

        numSet = set(nums)
        longest = 0 

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(longest, length) 
        return longest
