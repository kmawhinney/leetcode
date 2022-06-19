class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        
        for char in s.lower():
            if char in string.ascii_letters:
                new_str += char
            elif char in string.digits:
                new_str += char
            else:
                continue
                
        l = 0 # left pointer
        r = len(new_str) - 1 # right pointer
        
        while l < r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
