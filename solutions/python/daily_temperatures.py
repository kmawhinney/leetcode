class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        day_stack = []
        result = [0] * len(temperatures)

        for curr_day in range(len(temperatures)):
            curr_temp = temperatures[curr_day]
            while temp_stack and curr_temp > temp_stack[-1]:
                temp_stack.pop()
                old_day = day_stack.pop()
                result[old_day] = curr_day - old_day
            temp_stack.append(curr_temp)
            day_stack.append(curr_day)
        
        return result
