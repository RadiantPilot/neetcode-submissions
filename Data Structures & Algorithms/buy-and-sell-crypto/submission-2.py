class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        for i in range(1, len(prices)):
            hold = prices[i] - min(prices[:i])
            if hold > prof:
                prof = hold
        return prof