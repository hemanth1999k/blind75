class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            area = self.largestRectangleArea(height)
            maxArea = max(maxArea, area)
        return maxArea