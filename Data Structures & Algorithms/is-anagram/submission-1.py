class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(list(s))
        y = sorted(list(t))
        return x == y