'''
description: given list of nums, find triplets [i, j, k] where i + j + k == 0. no dupes

given nums = [-1,0,1,2,-1,-4], sort array for ascending order property.
one for loop to iterate, and a lhs + rhs bracket to check for zero condition
add/subtract lhs/rhs as you go depending if pos/neg
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()

        for i in range(len(nums) - 2):
            lhs, rhs = i + 1, len(nums) - 1

            while lhs < rhs:
                f, s, t = nums[i], nums[lhs], nums[rhs]
                total = f + s + t

                if total < 0:
                    lhs += 1
                elif total > 0:
                    rhs -= 1
                else:
                    if [f, s, t] not in lst:
                        lst.append([f, s, t])
                    lhs += 1
                    rhs -= 1
        
        return lst
