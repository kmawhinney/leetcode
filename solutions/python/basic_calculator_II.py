import math

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        if not s:
            return 0

        if len(s) == 1:
            return int(s[0])
        
        operators = {"+", "-", "*", "/"}
        stack = []
        curr_num = 0
        operator = "+" # initializes as plus because we want the first number added to stack
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit(): # accounts for more than just single-digit numbers
                curr_num = curr_num * 10 + int(char)
            
            if char in operators or i == len(s) - 1: # second part accounts for last number
                if operator == "+":
                    stack.append(curr_num)
                    
                elif operator == "-":
                    stack.append(curr_num * -1)
                    
                elif operator == "*":
                    stack.append(stack.pop() * curr_num)
                    
                elif operator == "/":
                    if stack[-1] > 0: # ex: 3/2 = 1.5, we want rounded down to 1
                        stack.append(math.floor(stack.pop() / curr_num))
                    else: # ex: -3/2 = -1.5, we want rounded up to -1
                        stack.append(math.ceil(stack.pop() / curr_num))
                
                curr_num = 0 # new current num will be the next char
                operator = char
            
        return sum(stack)
