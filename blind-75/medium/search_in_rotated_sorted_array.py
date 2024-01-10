'''
description: find target in rotated sorted array in O(log(n)) time

binary search and check left + right subarrays for ascending/descending qualities,
then check existence of target in both portions using the sorted property as advantage
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1