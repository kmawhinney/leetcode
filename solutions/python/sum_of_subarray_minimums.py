class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        stack = []
        
        # mid is the minimum value we're looking at
        # l is the leftmost value that is smaller than mid
        # r is the rightmost value that is smaller than mid
        # mid is the smallest value for every subarray between l and r
        
        # example: [2, 8, 6, 7, 3, 5, 4, 1]
        # when we are at 3, it is the smallest value for everything to the right of 2 (which is l), and everything to the left of 1 (which is r)
        
        # we have to do len(arr) + 1, and the else -1 because when we reach the end, we will not have done calculations for the final value in arr
        
        for r in range(len(arr) + 1):
            curr = arr[r] if r < len(arr) else -1
            while stack and curr < arr[stack[-1]]:
                mid = stack.pop()
                l = stack[-1] if stack else -1
                result += (mid - l) * arr[mid] * (r - mid)
            stack.append(r)
        
        return result % (10 ** 9 + 7)
