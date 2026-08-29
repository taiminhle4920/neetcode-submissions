class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, arr, cur):
            if cur == target:
                res.append(arr.copy())
                return
            if cur > target:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                arr.append(candidates[i])
                backtrack(i+1, arr, cur + candidates[i])
                arr.pop()
            
        backtrack(0, [], 0)
        return list(res)