class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for idx, val in enumerate(nums):
            
            diff = target - val
            
            if diff in d:
                return(idx, d[diff])
            else:
                d[val] = idx