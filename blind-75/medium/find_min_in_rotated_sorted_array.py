class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        lowest = float('INF')

        while l < r:
            mid = (r + l) // 2

            lowest = min(nums[mid], lowest)

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return min(lowest, nums[l])


                


