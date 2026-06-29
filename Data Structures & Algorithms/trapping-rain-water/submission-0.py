class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = [], [0]* len(height)
        cur = 0
        res = 0
        for i in range(len(height)):
            maxL.append(cur)
            if height[i] > cur:
                cur = height[i]
        cur = 0
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = cur
            if height[i] > cur:
                cur = height[i]
        
        for i in range(len(height)):
            v = max(0, min(maxL[i], maxR[i]) - height[i])
            res += v
        
        return res