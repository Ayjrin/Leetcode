class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        col = {"red": 0, "white": 0, "blue": 0}

        for num in nums:
            if num == 0:
                col['red'] += 1
            elif num == 1:
                col['white'] += 1
            else:
                col['blue'] += 1


        index = 0
        for _ in range(col['red']):
            nums[index] = 0
            index += 1
        for _ in range(col['white']):
            nums[index] = 1
            index += 1
        for _ in range(col['blue']):
            nums[index] = 2
            index += 1


