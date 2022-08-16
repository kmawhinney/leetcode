class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # Without Using Min Heap
        ending_times = [0]
        rooms = 0
        
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        
        for start, end in sorted_intervals:
            min_end = min(ending_times)
            if start >= min_end:
                ending_times.remove(min_end)  
            ending_times.append(end)
            rooms = max(rooms, len(ending_times))
        
        return rooms
    
        
        # Using Min Heap
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
