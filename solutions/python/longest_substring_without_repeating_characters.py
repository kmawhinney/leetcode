class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1

        if len(s) == 0:
            longest_substring = 0
        else:
            current_substring = s[l]
            longest_substring = 1
            
            while r <= len(s) - 1:
                if s[r] not in current_substring:
                    r += 1
                    current_substring = s[l:r]
                    longest_substring = max(longest_substring, len(current_substring))
                else:
                    l += 1
                    current_substring = s[l:r]

        return longest_substring
