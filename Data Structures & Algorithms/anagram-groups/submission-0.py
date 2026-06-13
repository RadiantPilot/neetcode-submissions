class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hold = {}
        for i in strs:
            if tuple(sorted(i)) not in hold:
                hold[tuple(sorted(i))] = []
                hold[tuple(sorted(i))].append(i)
            else:
                hold[tuple(sorted(i))].append(i)
        return list(hold.values())