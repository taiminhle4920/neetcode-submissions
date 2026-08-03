class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        elif not s:
            return ""
        elif len(s) < len(t):
            return ""
        res = ""
        c = Counter(t)
        need = len(c)
        l, r = 0, 0
        while l <= r and r < len(s):
            if s[r] in c:
                c[s[r]] -= 1
                if c[s[r]] == 0:
                    need -= 1
            
            if need == 0:
                if res == "" or  len(res) > len(s[l:r+1]):
                    res = s[l:r+1]

                while need == 0:
                    if len(res) > len(s[l:r+1]):
                        res = s[l:r+1]
                    if s[l] in c:
                        c[s[l]] += 1
                        if c[s[l]] > 0:
                            need += 1

                    l += 1
            r += 1

        return res

            