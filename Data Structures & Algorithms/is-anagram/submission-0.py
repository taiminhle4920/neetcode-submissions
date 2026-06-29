class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = dict()
        res2 = dict()
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = 1
            else:
                res[s[i]] += 1
            
            if t[i] not in res2:
                res2[t[i]] = 1
            else:
                res2[t[i]] += 1


        for k, v in res.items():

            if k not in res2.keys() or res[k] != res2[k]:
                return False
        return True