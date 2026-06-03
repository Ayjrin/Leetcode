class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0

        while j < len(nums):
            if j == i:
                j += 1
            
        
            if abs(i - j) > k: 
                i += 1
            if nums[i] != nums[j]:
                j += 1

            if abs(i - j) <= k and nums[i] == nums[j]:
                return True
        return False
        