class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        if len(prices) == 1:
            return 0
        
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if sell <= buy:
                l = r
            else:
                curr_profit = sell - buy
                max_profit = max(max_profit, curr_profit)
            r += 1
        
        return max_profit
