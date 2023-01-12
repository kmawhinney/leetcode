class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_stack = []

        for c in s:
            if c in close_to_open:
                if open_stack and close_to_open[c] == open_stack[-1]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(c)
        
        if not open_stack:
            return True
