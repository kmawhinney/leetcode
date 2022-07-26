class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_frequency = defaultdict(int)
        
        word_list = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph]).split()
        
        for word in word_list:
            if word not in banned:
                word_frequency[word] += 1
        
        return max(word_frequency, key=word_frequency.get)
