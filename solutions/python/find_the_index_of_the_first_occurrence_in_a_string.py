class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        haystackLen = len(haystack)

        if needleLen > haystackLen:
            return -1

        for i in range(haystackLen - needleLen + 1):
            if haystack[i:i+needleLen] == needle:
                return i
        return -1
