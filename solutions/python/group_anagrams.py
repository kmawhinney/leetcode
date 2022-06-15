class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            
            if sorted_word in hashmap:
                # add word as value to sorted_word key
                hashmap[sorted_word].append(word)
                
            else:
                # add sorted_word as new hash map key
                # then add word as value to sorted_word key
                hashmap[sorted_word] = []
                hashmap[sorted_word].append(word)
        
        for value in hashmap.values():
            result.append(value)
            
        return result
