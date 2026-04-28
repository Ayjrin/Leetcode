class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # start l and r on the first
        # if curr in t, and l == none, l = curr
        # if curr in t and l != none, r = curr
        # if l != res = s[l:r]
        
        res = ""
        l, r = 0


        for curr in range(len(s)):
            if s[curr] in t and l == 0:
                l = curr
                r = curr
            if s[curr] in t and r < curr:
                r = curr
        if t in s[l:r]:
            res = s[l:r]
        return res
