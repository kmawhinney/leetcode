class Solution(object):
    def productExceptSelf(self, nums):
        # More efficient (prefix/postfix int)
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result

        
        # Less efficient (prefix/postfix array)
        length = len(nums)
        result = [1] * length
        prefix = [1] * length
        postfix = [1] * length

        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(length - 2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        
        for i in range(length):
            result[i] = prefix[i] * postfix[i]

        return result
