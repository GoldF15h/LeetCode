class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = cost[0]
        p2 = cost[1]
        for i in range(2,len(cost)) :
            tmp = cost[i] + min(p1,p2)
            p1 = p2 
            p2 = tmp
        return min(p1,p2)