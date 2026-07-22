class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        cur = 1
        c = chars[0]


        for i in range(1, len(chars)):
            if chars[i] != c:
                chars[res] = c
                res += 1
                if cur > 1:
                    s = str(cur)
                    for v in s:
                        chars[res] = v
                        res += 1
                cur = 1
                c = chars[i]
            else:
                cur += 1
        
        chars[res] = c
        res += 1

        if cur > 1:
            s = str(cur)
            for v in s:
                chars[res] = v
                res += 1

        return res
