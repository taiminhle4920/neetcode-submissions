class Solution:
    def trap(self, height: List[int]) -> int:
        # maxL, maxR = [], [0]* len(height)
        # cur = 0
        # res = 0
        # for i in range(len(height)):
        #     maxL.append(cur)
        #     if height[i] > cur:
        #         cur = height[i]
        # cur = 0
        # for i in range(len(height) - 1, -1, -1):
        #     maxR[i] = cur
        #     if height[i] > cur:
        #         cur = height[i]
        
        # for i in range(len(height)):
        #     v = max(0, min(maxL[i], maxR[i]) - height[i])
        #     res += v
        
        # return res

        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]  

        return res

