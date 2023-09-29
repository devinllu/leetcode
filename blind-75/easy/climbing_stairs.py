'''
description: You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Input: n = 2
Output: 2

1. 1 step + 1 step
2. 2 steps

need to update first + second vars as you go, memoize
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 1 1 1 1
        # 1 2 3 5 8

        if n < 4:
            return n
        
        first = 2
        second = 3
        for i in range(4, n):
            new_second = first + second
            first = second
            second = new_second
        
        return first + second
