class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, char in enumerate(nums):
            if char in nums[i + 1:]:
                return True
        return False