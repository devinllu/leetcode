'''
description: return prod of array except self w/out using division in O(n) time

double pass through nums with prefix + postfix iterators. forward loop for prefix,
multiplying each ith entry to i+1th entry, and vice versa (reverse loop) for postfix
'''

# O(n) solution using division operator
# essentially get product of array, and for each entry divide by current
# edge cases around multiplying/dividing with 0 though

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         def get_prod(lst):
#             prod = 1

#             for i in lst:
#                 if i != 0:
#                     prod *= i
#             return prod
        
#         answer = []
#         total_sum = get_prod(nums)

#         if 0 in nums:
#             if nums.count(0) == 1:
#                 return [0 if i != 0 else total_sum for i in nums]
#             else:
#                 return [0 for _ in nums]

#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 total = total_sum / nums[i]
#                 answer.append(int(total))
#             else:
#                 answer.append(int(total_sum))
        

#         return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        #[1, 12, 8, 6]

        prefix, postfix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        
