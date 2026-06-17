class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tot = []
        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1
            while L < R:
                hold = nums[L] + nums[R] + nums[i]
                if hold < 0:
                    L += 1
                elif hold > 0:
                    R -= 1
                elif hold == 0:
                    if [nums[i], nums[L], nums[R]] in tot:
                        L += 1
                        continue
                    tot.append([nums[i], nums[L], nums[R]])
                    L += 1
        return tot
