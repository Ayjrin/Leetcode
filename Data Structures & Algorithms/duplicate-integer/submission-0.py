class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.append(nums[i])
            else: return True
        return False