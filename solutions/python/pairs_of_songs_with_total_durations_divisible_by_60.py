class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = {}
        pairs = 0

        for t in time:
            modNum = t % 60

            # 0s need to be handled specially because 60 % 60 = 0
            if modNum == 0:
                if 0 in hashmap:
                    pairs += hashmap[0]
            elif (60 - modNum) in hashmap:
                pairs += hashmap[60 - modNum]
            
            if modNum not in hashmap:
                hashmap[modNum] = 1
            else:
                hashmap[modNum] += 1

        return pairs
