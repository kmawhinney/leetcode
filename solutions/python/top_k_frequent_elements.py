from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        result = []

        for num in nums:
            num_count[num] += 1
        
        sorted_count = sorted(num_count.items(), key=lambda x:x[1])

        while k > 0:
            num, count = sorted_count.pop()
            result.append(num)
            k -= 1
        
        return result
