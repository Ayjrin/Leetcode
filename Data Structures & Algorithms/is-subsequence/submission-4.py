class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # how do i not use an extra variable and get rid of all these returns?
        new_t = ""
        if len(s) == 0:
            return True
        elif len(t) == 0 and len(s) != 0:
            return False
        if len(t) < len(s):
            return False 
        for i in range(len(s)):
            while t[i] != s[i]:
                t = t[1:]
                if len(t) == 0 and len(s) - i != 1:
                    return False # if s is longer than t and also s has the subset, then false. then. its a superset.
            if t[i] == s[i]:
                new_t += t[i]
        if new_t == s:
            return True
        else: return False
