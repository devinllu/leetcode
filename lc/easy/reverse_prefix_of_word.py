class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = ""
        for i, v in enumerate(word):
            if v == ch:
                rev = word[0:i+1][::-1]
                last = word[i+1:len(word)]


                return rev + last
        return word