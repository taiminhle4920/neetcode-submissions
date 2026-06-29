class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) -1
        maxV = 0

        while l < r:
            maxHeight = min(heights[l], heights[r])
            vol = maxHeight * (r - l)
            if vol > maxV:
                maxV = vol
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return maxV
            