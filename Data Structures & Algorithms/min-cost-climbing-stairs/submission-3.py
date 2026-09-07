class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost)
        c1, c2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            t = min(c1, c2) + cost[i]
            c1 = c2
            c2 = t
        return min(c1,c2)