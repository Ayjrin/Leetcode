class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smol = 1
        nums.sort()
        for num in nums:
            if num == smol:
                smol += 1
        return smol