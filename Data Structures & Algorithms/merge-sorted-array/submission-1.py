class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0

        while i < len(nums1) and j < n:
            if nums1[i] < nums2[j] and (m > 0 or nums1[i] != 0):
                i+=1
                m-=1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop(-1)
                j+=1
                i+=1
                m-=1
        while j < n:     
            nums1.insert(i, nums2[j])
            nums1.pop(-1)
            j+=1
        return nums1

