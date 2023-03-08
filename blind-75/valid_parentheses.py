class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        openings = ['(', '[', '{']
        for c in s:
            if c in openings:
                st.append(c)
            
            else:
                if len(st) == 0:
                    return False
                
                previous = st.pop()
                if pairs[previous] != c:
                    return False
        if len(st) != 0:
            return False
            
        return True
