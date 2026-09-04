class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        if len(prices) == 1:
            return 0
        l, r = 0, 0
        while r < len(prices):
            cur_max = max(prices[r] - prices[l], cur_max)
            if (prices[l] > prices[r]):
                l = r
            r+=1
        return cur_max