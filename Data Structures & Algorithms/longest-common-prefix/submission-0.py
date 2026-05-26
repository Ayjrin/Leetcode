class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs)-1):
            while strs[i+1][:len(strs[0])] != strs[0]:
                strs[0] = strs[0][:-1]
        return strs[0]
