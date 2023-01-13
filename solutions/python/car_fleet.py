class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = sorted(zip(position, speed), key=lambda x:-x[0])
        stack = [] # monotonic stack, top is slowest car to reach end

        for car_pos, car_speed in pos_speed_pair:
            time_to_end = (target - car_pos) / car_speed
            print(time_to_end)

            if not stack or time_to_end > stack[-1]:
                stack.append(time_to_end)
        
        return len(stack)
