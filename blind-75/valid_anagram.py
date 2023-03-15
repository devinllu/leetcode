class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        if len(s) != len(t):
            return False

        for c in s:
            d1[c] = d1.get(c, 0) + 1
        
        for c in t:
            d2[c] = d2.get(c, 0) + 1

        
        for entry in d1:
            if d1[entry] != d2.get(entry, 0):
                return False
        
        return True
