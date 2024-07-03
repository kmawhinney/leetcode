class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        maxEndingHere = nums[0]
        maxTotal = nums[0]

        for i in range(1, len(nums)):
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            maxTotal = max(maxTotal, maxEndingHere)
        
        return maxTotal
