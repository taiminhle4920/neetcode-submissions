class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char not in dct:
                stack.append(char)
                continue
            
            if not stack or stack[-1] != dct[char]:
                return False
            stack.pop()
        return not stack
            
