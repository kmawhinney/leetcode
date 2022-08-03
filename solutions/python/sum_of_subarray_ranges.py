class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # O(n^2) Solution
        
        result = 0
        
        for i in range(len(nums)):
            smallest = nums[i]
            largest = nums[i]
            
            for j in range(i, len(nums)):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                result += largest - smallest
                
        return result
