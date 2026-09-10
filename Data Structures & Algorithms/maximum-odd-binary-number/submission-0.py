class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero, one = 0, 0
        for i in s:
            if i == "0":
                zero += 1
            elif i == "1":
                one += 1
        res = ""
        if one > 1:
            res += "1" * (one-1)
            res += "0" * zero
            res += "1"
        else:
            res += "0" * zero
            if one > 0:
                res += "1"
        return res