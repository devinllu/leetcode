class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))

            if s_sorted in d.keys():
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]

        return list(d.values())
                