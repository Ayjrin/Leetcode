class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)/3
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1
        
        for num in count:
            if count[num] > target:
                res.append(num)

        return res

