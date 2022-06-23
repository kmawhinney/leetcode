class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix, suffix = 1, 1
        pre_array, suf_array = [], []
        
        for num in nums:
            pre_array.append(prefix)
            prefix *= num
            
        nums.reverse()
            
        for num in nums:
            suf_array.append(suffix)
            suffix *= num
            
        suf_array.reverse()
        
        for i in range(len(nums)):
            answer.append(pre_array[i] * suf_array[i])
            
        return answer
