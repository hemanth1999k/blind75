class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        total = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    total += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    total += rightMax - height[right]
                right -= 1
        
        return total