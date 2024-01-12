'''
desc: given unsorted array of ints, find longest conseq seq in linear time

iterate through array to find values with no left-neighbor in nums (can achieve
O(1) lookup with python sets) to find starting point, then count length
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for n in nums:  
            prev = n - 1

            if prev not in st:
                counter = 0
                while (n + counter) in st:
                    counter += 1
                
                if counter > longest:
                    longest = counter
        return longest