class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i in range(len(heights) + 1):
            while stack and (i== len(heights) or heights[stack[-1]] >= heights[i]):
                h = heights[stack.pop()]
                if not stack:
                    w = i
                else: 
                    w = i - stack[-1] -1
                area = max(area, h * w)
            stack.append(i)
        return area
            