from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ocean_views = deque()
        tallest = 0

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > tallest:
                ocean_views.appendleft(i)
                tallest = heights[i]

        return ocean_views
