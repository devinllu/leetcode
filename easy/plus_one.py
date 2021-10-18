class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for k, v in reversed(list(enumerate(digits))):
            
            if v == 9:
                digits[k] = 0
                
            else:
                digits[k] += 1
                return digits
            
        
        return [1] + digits