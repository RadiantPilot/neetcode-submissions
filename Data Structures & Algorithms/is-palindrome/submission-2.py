class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalpha() or i.isnumeric():
                continue
            else:
                s = s.replace(i,"")
        return s.upper() == s[::-1].upper()