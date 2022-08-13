class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = 0
        max_end = 0
        result = []
        
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(sorted_intervals)
        
        for start, end in sorted_intervals:
            if result and start in range(max_start, max_end + 1):
                result[-1][1] = max(max_end, end)
            else:
                result.append([start, end])
            max_start = max(max_start, start)
            max_end = max(max_end, end)
        
        return result
