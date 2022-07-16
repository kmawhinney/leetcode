class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # faster lookups in sets VS lists
        longest_ever = 0
        
        for num in num_set:
            # if a smaller value is available, we'll start the sequence there
            if (num - 1) not in num_set:
                longest_curr = 1
                
                while (num + 1) in num_set:
                    num += 1
                    longest_curr += 1
                
                longest_ever = max(longest_ever, longest_curr)
        return longest_ever
