class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []

        for i in range(0, n + 1):
            b = bin(i)[2:]
            
            counter = 0
            for c in b:
                if c == '1':
                    counter += 1
            
            ret.append(counter)
        
        return ret
