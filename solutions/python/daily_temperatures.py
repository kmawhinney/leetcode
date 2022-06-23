class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevday = stack.pop()
                answer[prevday] = day - prevday
            stack.append(day)
            
        return answer
