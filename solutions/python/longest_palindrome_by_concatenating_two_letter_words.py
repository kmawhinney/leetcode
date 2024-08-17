from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = defaultdict(int)
        length = 0

        for pair in words:
            complement = pair[::-1]
            if complement in counter and counter[complement] > 0:
                length += 4
                counter[complement] -= 1
            else:
                counter[pair] += 1

        # Double check: If there is an unused pair that has double letters, add 2 to result
        for pair in counter:
            if pair[0] == pair[1] and counter[pair] > 0:
                length += 2
                break

        return length
