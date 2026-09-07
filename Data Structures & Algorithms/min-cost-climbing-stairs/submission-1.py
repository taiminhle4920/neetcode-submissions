class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [i for i in cost]
        dp.append(0)
        if len(cost) == 1:
            return cost[0]
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2], dp[i-1]) +dp[i]
        return dp[-1]