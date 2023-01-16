class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        def finish_bananas(rate):
            time_to_finish = 0
            for pile in piles:
                time_to_finish += math.ceil(pile / rate)
            return time_to_finish
                
        while l <= r:
            mid = (l + r) // 2
            if finish_bananas(mid) <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return result
