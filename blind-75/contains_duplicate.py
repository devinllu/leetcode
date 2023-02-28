class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for val in nums:
            if val in d.keys():
                return True
            else:
                d[val] = d.get(val, 0) + 1
        
        return False
