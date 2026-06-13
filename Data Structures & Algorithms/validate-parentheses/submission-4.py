class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        hold = []
        pairs = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i == "(" or i == "{" or i == "[":
                hold.append(i)
            elif hold and pairs[i] == hold[-1]:
                hold.pop(-1)
            else:
                return False
        return len(hold) == 0