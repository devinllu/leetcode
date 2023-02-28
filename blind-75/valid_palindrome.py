class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = s.upper()
        sanitized = "".join(i for i in sanitized if i.isalnum())
        

        return sanitized == sanitized[::-1]