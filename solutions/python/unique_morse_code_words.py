class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()

        for word in words:
            curr = []
            for char in word:
                curr.append(morse_codes[ord(char) - 97]) # ord() returns Unicode for char, and subtracting 97 gives morse_code index
            transformations.add("".join(curr))
        
        return len(transformations)
