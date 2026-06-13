class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0
        i = 0
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            tot += abs(ord(s[i + 1]) - ord(s[i]))
            i += 1
            if i + 1 >= len(s):
                return tot