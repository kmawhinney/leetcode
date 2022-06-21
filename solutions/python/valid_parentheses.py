class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketmap = {')': '(',
                      '}': '{',
                      ']': '['}
        
        for c in s:
            if c in bracketmap:
                if stack and bracketmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if not stack:
            return True
