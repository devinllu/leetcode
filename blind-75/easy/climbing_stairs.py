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
