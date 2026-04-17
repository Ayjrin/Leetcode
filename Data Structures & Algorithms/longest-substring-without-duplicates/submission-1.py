class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # If we see a duplicate, shrink the window from the left 
            # until the duplicate is removed from our set.
            while s[r] in current_substring:
                current_substring.remove(s[l])
                l += 1
            # Add the new character to the set
            current_substring.add(s[r])

            # Update the max result. The current valid window size is (r - l + 1)
            res = max(res, (r - l + 1))
        return res