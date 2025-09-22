class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start,lst):
            res.append(lst[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                lst.append(nums[i])
                backtrack(i+1,lst)
                lst.pop()
        
        backtrack(0,[])
        return res