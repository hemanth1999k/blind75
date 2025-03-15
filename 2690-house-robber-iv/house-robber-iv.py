class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if self.canRobAtLeastK(nums, mid, k):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
    
    def canRobAtLeastK(self, nums, capability, k):
        count = 0
        i = 0
        
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                if count == k:
                    return True
                i += 1
            i += 1
        return False        