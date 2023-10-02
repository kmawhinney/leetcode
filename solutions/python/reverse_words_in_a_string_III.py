class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = []

        for word in words:
            reversed_words.append("".join(reversed(word)))
        result = " ".join(reversed_words)
        return result
