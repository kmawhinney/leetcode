class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # element is key, frequency is value
        output = []
        
        for num in nums:
            if num in hashmap:
                # increase frequency
                hashmap[num] += 1
                
            else:
                # add num as key, set frequency to 1
                hashmap[num] = 1
                
        while k > 0:
            # find biggest frequency, add key to output, remove pair from hashmap
            current_max = max(hashmap, key=hashmap.get)
            output.append(current_max)
            hashmap.pop(current_max)
            k -= 1
                
        return output
