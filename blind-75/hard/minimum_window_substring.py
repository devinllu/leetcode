class Solution:
    
    def minWindow(self, s: str, t: str) -> str:

        def valid_substr(d):
            return all(value >= 0 for value in d.values())

        lowest = ""
        dq = []
        counter = {}

        for c in t:
            if c in counter.keys():
                counter[c] -= 1
            else:
                counter[c] = -1
        
        for i, c in enumerate(s):
            if c in counter.keys():
                counter[c] += 1
                dq.append((c, i))

                if valid_substr(counter) and lowest == "":
                
                    first = dq[0][1]
                    second = dq[len(dq) - 1][1] + 1

                    lowest = s[first:second]
                while any(value > 0 for value in counter.values()) and valid_substr(counter):
                    vals = dq.pop(0)
                    counter[vals[0]] -= 1
                
                    first = dq[0][1]
                    second = dq[len(dq) - 1][1] + 1

                    potential_lowest = s[first:second]
                    if len(lowest) > len(potential_lowest) and valid_substr(counter):
                        lowest = potential_lowest
        return lowest

# expected: "abbbbbcdd"
# s = Solution()
# first, second = 'aaaaaaaaaaaabbbbbcdd', 'abcdd'
# print(f's: {first}, t: {second}\n')
# print(s.minWindow(first, second))