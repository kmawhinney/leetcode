class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Dynamic Programming: Top-Down Approach
        memo = {}
        
        def dp(x):
            if x <= 2:
                return x
            
            if x not in memo:
                memo[x] = dp(x - 1) + dp(x - 2)
                
            return memo[x]
        
        return dp(n)
    
    
        # Dynamic Programming: Bottom-Up Approach
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
