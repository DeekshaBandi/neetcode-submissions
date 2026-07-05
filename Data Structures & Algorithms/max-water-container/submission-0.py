class Solution:
    def maxArea(self, num: List[int]) -> int:
        out = 0
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                out = max(out, min(num[i], num[j]) * (j-i))
        return out            

