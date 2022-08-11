class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Dynamic Programming: Bottom-Up Approach
        
        minimum = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            one_step = minimum[i-1] + cost[i-1]
            two_steps = minimum[i-2] + cost[i-2]
            minimum[i] = min(one_step, two_steps)
        
        return minimum[-1]
