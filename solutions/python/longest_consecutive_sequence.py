class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # faster lookups in sets VS lists
        longest_streak = 0
        
        for num in num_set:
            # if a smaller value is available, we'll start the sequence there
            if (num - 1) not in num_set:
                curr_streak = 1
                
                while (num + 1) in num_set:
                    num += 1
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
