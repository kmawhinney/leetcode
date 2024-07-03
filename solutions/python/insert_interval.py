class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]
        result = []

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            # new interval comes BEFORE current interval
            if newEnd < start:
                result.append(newInterval)
                return result + intervals[i:]
            # new interval comes AFTER current interval
            elif newStart > end:
                result.append(intervals[i])
            # new interval OVERLAPS with current interval
            else:
                newInterval = [min(newStart, start), max(newEnd, end)]
                newStart = newInterval[0]
                newEnd = newInterval[1]
        
        # if interval has not yet been added
        result.append(newInterval)

        return result
