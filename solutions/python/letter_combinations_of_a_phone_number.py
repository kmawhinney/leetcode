class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        letter_map = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl", 
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        
        def word_build(i, curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
            
            for c in letter_map[digits[i]]:
                word_build(i + 1, curr + c)
                
        if not digits:
            return ""
        else:
            word_build(0, "")
            
        return result
