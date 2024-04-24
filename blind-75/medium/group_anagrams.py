'''
desc: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

soln: create list of size 26 0's (each representing an alphabet in-order) for each string, and inc the index of
the list corresponding to each char. this becomes the key to our dict, then return dict.values()
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        ret = []

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            res[tuple(counter)].append(s)
        
        for val in res.values():
            ret.append(val)
        return ret