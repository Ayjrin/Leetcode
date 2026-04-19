class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # while k > 0 
        #we can subtract 1 for every letter that is not the letter we are looking for

        # current char
        # longest run
        # left starts at 0
        # right starts at l + 1 and keeps getting bigger so long as k > 0 or s[r] == current char
        longest_run = 0

        for l in range(len(s)):
            curr_char = s[l]
            sub = k
            r = l + 1

            while sub > 0 and r < len(s):
                if curr_char == s[r]:
                    r += 1
                    if r - l > longest_run:
                        longest_run = r - l
                else:
                    r += 1
                    if r - l > longest_run:
                        longest_run = r - l
                    sub -= 1
                    continue
            
            while r < len(s) and curr_char == s[r]:
                r += 1
                if r - l > longest_run:
                    longest_run = r - l
            
            if r - l > longest_run:
                longest_run = r - l

        return longest_run
                
