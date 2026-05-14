class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = 0
        temp = 0
        for i in range(len(arr), -1, -1):
            if i == len(arr)-1:
                curr = max(curr, arr[i])
                arr[i] = -1
            elif i < len(arr):
                temp = arr[i]
                arr[i] = max(arr[i+1], curr)
                curr = max(temp, curr)

        return arr