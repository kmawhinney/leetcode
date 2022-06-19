class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = min(height[l],height[r]) * (r-l)
        
        while l < r:
            if height[l] < height[r]:
                new_area = min(height[l+1],height[r]) * (r-l-1)
                if new_area > area:
                    area = new_area
                l += 1
            else:
                new_area = min(height[l],height[r-1]) * (r-l-1)
                if new_area > area:
                    area = new_area
                r -= 1
        
        return area
