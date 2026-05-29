class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        grace = True
        while s[l] == s[r] or grace == True:
            print(f"front of while: {l}, {r}, {grace}")
            if r <= l:
                return True
            else:
                print(f"else: {l}, {r}")
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
                else:
                    print(f"else: {l}, {r}, {grace}")
                    l += 1
                    r -= 1

        return False
