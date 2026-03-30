import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strn = s
        strn = re.sub(r'[^a-zA-Z0-9]','', strn)
        strn = strn.lower()
        strn2 = strn[::-1]
        print(strn)
        print(strn2)

        return True if strn == strn2 else False