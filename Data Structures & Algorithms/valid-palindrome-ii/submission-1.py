class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        grace = True
        while s[l] == s[r] or grace == True:
            if r - l <2:
                return True
            else:
                l += 1
                r -= 1
                if grace == True and s[l] != s[r]:
                    if s[l+1] == s[r]:
                        l+=1
                        grace = False
                        continue
                    elif s[r-1] == s[l]:
                        r-=1
                        grace = False
                        continue
                    else:
                        return False

        return False
