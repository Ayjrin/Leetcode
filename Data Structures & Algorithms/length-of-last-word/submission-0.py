class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sub = s.split(" ")
        while sub[-1] == "":
            sub.pop()
        return len(sub[-1])