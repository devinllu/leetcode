'''
description: find max area of array with height[i] and distance i in O(n) time

setup left + right pointers at both ends of array, calc current height and
replace with max, then iterate pointer with smaller height
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        highest = 0

        while l <= r:
            front, last = height[l], height[r]

            area = min(front, last) * (r - l)

            if area > highest:
                highest = area
            
            if front < last:
                l += 1
            else:
                r -= 1
        return highest
