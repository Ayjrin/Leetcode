class Solution:
    
    
    def maxArea(self, heights: List[int]) -> int:
        def find_water_volume(l, r):
            return (r - l) * min(heights[r], heights[l])

        l = 0
        r = len(heights) - 1
        max_water = find_water_volume(l, r)



        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
            max_water = max(max_water, find_water_volume(l, r))
        return max_water