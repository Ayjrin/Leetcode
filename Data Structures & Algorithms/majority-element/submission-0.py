class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 0
        big = (0, 0)
        for k, v in seen.items():
            if v > big[1]:
                big = (k, v)
        return big[0]