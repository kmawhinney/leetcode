from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key : [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        curr_value = ""

        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            value = values[mid][0]
            time = values[mid][1]
            if time == timestamp:
                return value
            if time < timestamp:
                curr_value = value
                l = mid + 1
            else:
                r = mid - 1
        return curr_value



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
