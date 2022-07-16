class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i, first_num in enumerate(nums):
            if i > 0 and first_num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = first_num + nums[l] + nums[r]
                if three_sum == 0:
                    result.add(tuple([first_num, nums[l], nums[r]]))
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
                    
        return result
