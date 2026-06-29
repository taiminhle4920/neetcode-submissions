class Solution:
    def isValid(self, s: str) -> bool:
        # s = []
        # dct = {")": "(", "]": "[", "}": "{"}
        
        # for char in s:
        #     if char not in dct:
        #         s.append(char)

        #         continue
            
        #     if not s or s[-1] != dct[char]:
        #         return False
        #     s.pop()
        # return not s
            
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack