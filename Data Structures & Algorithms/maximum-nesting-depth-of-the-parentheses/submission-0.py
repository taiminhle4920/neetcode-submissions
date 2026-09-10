class Solution:
    def maxDepth(self, s: str) -> int:
        maxP = 0
        cur = 0
        for c in s:
            if c == "(":
                cur += 1
                maxP = max(maxP, cur)
            elif c ==")":
                cur -= 1
        return maxP