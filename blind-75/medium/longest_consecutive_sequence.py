'''
desc: given unsorted array of ints, find longest conseq seq in linear time
'''


# O(nlog(n)) solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        nums.sort()

        counter = 1
        max_count = 0
        for i in range(len(nums) - 1):
            crrnt = nums[i]
            nxt = nums[i + 1]

            if crrnt + 1 != nxt and crrnt != nxt:
                if counter > max_count:
                    max_count = counter
                
                counter = 1

            elif crrnt + 1 == nxt:
                counter += 1
            
        
        if max_count < counter:
            max_count = counter
        return max_count