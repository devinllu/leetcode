class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)

        d = {}

        for val in nums:
            reversed_val = val * -1
            if val not in d.keys() and val > 0:
                d[val] = -1

            elif val < 0 and (reversed_val) in d.keys():
                d[reversed_val] = reversed_val
        
        if len(d.keys()) > 0:
            return max(d.values())

        return -1