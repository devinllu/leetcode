class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        longest = 0
        counter = 0

        i = 0
        
        while i < len(s):
            c = s[i]

            if c in d.keys():
                i = d[c] + 1
                d.clear()
                if counter > longest:
                    longest = counter
                counter = 1
                d[s[i]] = i
                

            else:
                d[c] = i
                counter += 1

            i += 1
        
        if counter > longest:
            longest = counter
        return longest