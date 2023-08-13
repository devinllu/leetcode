class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 3 0 1
        # 0 1
        # 9 6 4 2 3 5 7 0 1
        true_total = 0
        total = 0
        for index, val in enumerate(nums):
            true_total += index + 1
            total += val
        
        return true_total - total
