class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_sum = int(a, 2) + int(b, 2)
        
        str_sum = bin(int_sum)
        
        return str_sum[2:]