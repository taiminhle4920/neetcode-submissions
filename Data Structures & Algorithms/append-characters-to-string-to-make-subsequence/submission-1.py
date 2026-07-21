class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # l, r = 0, 0
        # while l < len(s) and r < len(t):
        #     if s[l] == t[r]:
        #         l += 1
        #         r += 1
        #     else:
        #         l += 1
        # return len(t) - r

        i = 0
        for c in s:
            if i <len(t) and c == t[i]:
                i += 1
        return len(t) - i