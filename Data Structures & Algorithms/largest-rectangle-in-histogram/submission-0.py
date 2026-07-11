class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        stack = []

        area = 0

        for i in range (len(nums) + 1):
            while stack and (i == len(nums) or nums[stack[-1]] >= nums[i]):
                h = nums[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)
        return area