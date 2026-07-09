class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}
        for i in magazine:
            dct[i] = dct.get(i, 0) + 1
        for c in ransomNote:
            if dct and dct.get(c, 0) == 0:
                return False
            dct[c] -= 1
        return True