class Solution(object):
    def isPalindrome(self, s):
        filtered_s = ''.join(c for c in s if c.isalnum()).lower()

        l = 0
        r = len(filtered_s) - 1

        if len(filtered_s) == 1:
            return True

        while l <= r:
            if filtered_s[l] != filtered_s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
