class Solution:
    def tribonacci(self, n: int) -> int:
        
        # Dynamic Programming: Top-Down Approach
        
        memo = {}
        
        def dp(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i not in memo:
                memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
            return memo[i]
        
        return dp(n)
        
        # Dynamic Programming: Bottom-Up Approach
        
        dp = [0] * (n + 1)
        dp[0] = 0
        if n >= 1:
            dp[1] = 1
        if n>= 2:
            dp[2] = 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            
        return dp[n]
