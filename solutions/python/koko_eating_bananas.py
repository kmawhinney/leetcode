class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        
        while l <= r:
            k = (r + l) // 2
            
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat += math.ceil(pile / k)
            
            if hours_to_eat > h:
                l = k + 1
            else:
                result = min(result, k)
                r = k - 1
                
        return result
