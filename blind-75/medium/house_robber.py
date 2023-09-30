'''
description: find max val of sum of nums in list, but cannot choose adjacent pairs to accumulate

memoize results with first/second, update as you go
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        first, second = 0, 0

        for n in nums:
            pair = max(first + n, second)
            first = second
            second = pair
        
        return second
