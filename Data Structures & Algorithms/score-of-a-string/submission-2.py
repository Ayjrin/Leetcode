class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            l = s[i]
            r = s[i+1]
            res += abs(ord(l) - ord(r))
        return res