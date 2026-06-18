class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        prefix = {0:1}
        for i in range(len(nums)):
            curr += nums[i]
            diff = curr - k
            res += prefix.get(diff, 0)
            prefix[curr] = 1 + prefix.get(curr, 0)
        return res