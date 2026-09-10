class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        curmax = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > curmax:
                curmax = heights[i]
                res.append(i)
        
        return res[::-1]