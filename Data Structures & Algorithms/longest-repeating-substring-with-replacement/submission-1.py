class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}

        l = 0 
        # we dont need the exact max at every window range; we just need the max one since that is the most that could appear
        maxf = 0

        # start the loop at the right pointer and increment the left only as needed
        for r in range(len(s)):
            # increment the count for the current letter in the dict
            count[s[r]] = 1 + count.get(s[r], 0)
            # take the max of the current letter count and the max frequency
            maxf = max(maxf, count[s[r]])

            # as long as our window - the max freq is greater than the amount we can replace, we want to decrement the l letter and shift the window by left pointer up by 1
            while (r - 1 + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

