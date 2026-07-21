class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = ord(s[0])
        for i in range(1, len(s)):
            res += abs(prev - ord(s[i]))
            prev = ord(s[i])
        return res