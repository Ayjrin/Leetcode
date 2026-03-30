class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        nums.sort()

        if not nums:
            return 0

        curr = 1
        for i in range(len(nums)-1):
            if ((nums[i] + 1) == nums[i+1]):
                curr += 1
                if curr > length:
                    length = curr
            elif (nums[i] == nums[i+1]):
                pass
            else:
                curr = 1

        return length