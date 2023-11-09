'''
desc: k most frequent elements in list

soln: ds solution, store counts in dict, convert to list with tups of key-val, swap key-val, sort
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        output = []

        for i in nums:
            counts[i] = counts.get(i, 0) + 1


        lst = list(counts.items())

        for i in range(len(lst)):
            tmp = lst[i]
            lst[i] = (tmp[1], tmp[0])
        
        lst.sort(reverse=True)

        for i in range(k):
            output.append(lst[i][1])
        
        return output





                
