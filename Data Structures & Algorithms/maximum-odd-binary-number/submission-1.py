class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero, one = 0, 0
        for i in s:
            if i == "0":
                zero += 1
            else:
                one += 1
        
        
        return ("1" * (one-1) + "0" * zero)+"1"