class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                l_skip, r_skip = s[l+1:r+1], s[l:r]
                return l_skip == l_skip[::-1] or r_skip == r_skip[::-1]
        
            l+=1
            r-=1
        return True