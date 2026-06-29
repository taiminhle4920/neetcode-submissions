class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        maxl = 1
        temp = 1
        s = list({i for i in nums})  # Remove duplicates and convert back to a list
        s.sort()  # Ensure the list is sorted

        if len(s) == 1:
            return 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1] + 1:
                temp += 1
            else:
                temp = 1

            if temp > maxl:
                maxl = temp

        return maxl
