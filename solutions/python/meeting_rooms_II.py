class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        min_heap = []
        
        for start, end in sorted(intervals, key=lambda x: x[0]):
            if not min_heap:
                min_heap.append(end)
                
            else:
                if start >= min_heap[0]:
                    heapq.heapreplace(min_heap, end)
                else:
                    heapq.heappush(min_heap, end)
        
        return len(min_heap)
