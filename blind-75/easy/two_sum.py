class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [2, 7, 11, 15], target = 9
        # [7], [11, 15]

        d = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in d:
                return (i, d[diff])
            else:
                d[nums[i]] = i
        
        return None
