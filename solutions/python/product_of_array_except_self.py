class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        pre, post, result = [1]*length, [1]*length, [1]*length

        # Calculate prefix
        for i in range(length):
            if i > 0:
                pre[i] = nums[i-1] * pre[i-1]
        
        # Calculate postfix
        for i in range(length, -1, -1):
            if i < (length - 1):
                post[i] = nums[i+1] * post[i+1]
        
        # Multiple prefix and postfix
        for i in range(length):
            result[i] *= pre[i] * post[i]
        
        return result
