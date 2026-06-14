class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # -- https://www.youtube.com/watch?v=7h1s2SojIRw --
        def partition(l, h):
            # added this so that if largest is at front in reverse sorted, we dont hit recursion max. hope its not dead in the middle lol
            mid = (l + h) // 2 
            nums[l], nums[mid] = nums[mid], nums[l]


            pivot = nums[l]
            i, j = l, h

            while i < j:
                while i < h and nums[i] <= pivot:
                    i += 1
                while nums[j] > pivot:
                    j -=1
                if i < j:
                    nums[j], nums[i] = nums[i], nums[j]
            nums[l], nums[j] = nums[j], nums[l]
            return j

        def quicksort(l, h):
            if l < h:
                j = partition(l, h)
                quicksort(l, j-1)
                quicksort(j+1, h)
       
       
        if len(nums) <2:
            return nums
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
        else:
            quicksort(0, len(nums)-1)

        return nums

        


