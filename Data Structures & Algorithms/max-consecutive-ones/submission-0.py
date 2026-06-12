class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, res = 0, 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                if count > res:
                    res = count
        return res