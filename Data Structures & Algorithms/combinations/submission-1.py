class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            for c in range(i, n+1):
                arr.append(c)
                backtrack(c+1, arr)
                arr.pop()
        
        backtrack(1, [])
        return res