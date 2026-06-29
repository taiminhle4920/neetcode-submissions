class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # l = 0
        # dct = {}
        # maxf = 0
        # for r in range(len(s)):
        #     dct[s[r]] = 1 + dct.get(s[r], 0)
        #     maxf = max(maxf, dct[s[r]])
            
        #     if (r - l + 1) - maxf > k:
        #         dct[s[l]] -= 1
        #         l += 1
        
        # return (r - l + 1)

        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
