from collections import OrderedDict
# OrderedDict is a HashMap that allows for ordering

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key) # end is most recently used
            return self[key]
        else:
            return -1
                
    def put(self, key: int, value: int) -> None:
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last=False) # front is least recently used
        
        self.move_to_end(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
