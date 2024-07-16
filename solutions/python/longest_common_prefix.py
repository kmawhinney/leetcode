class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Case: First string is empty
        if len(strs[0]) == 0:
            return ""
        
        # Case: Only one string in list
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        minLength = min(len(s) for s in strs)

        for i in range(minLength):
            curr = strs[0][i]

            if all(s[i] == curr for s in strs):
                prefix += curr
            else:
                return prefix

        return prefix
