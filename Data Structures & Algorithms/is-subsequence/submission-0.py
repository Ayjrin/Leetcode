class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = False
        new_t = ""
        if len(t) == 0 or len(s) == 0:
            return s == t
        for i in range(len(s)):
            while t[i] != s[i]:
                t = t[1:]
                if len(t) == 1:
                    return res # return early if we run out of letter in t -- todo: get rid of extra return
            if t[i] == s[i]:
                new_t += t[i]
        if new_t == s:
            res = True
        return res