class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        area = 0
        for i in range(n + 1):
            h = heights[i] if i < n else 0
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)
        return area