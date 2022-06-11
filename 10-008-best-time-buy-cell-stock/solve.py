# Solution as submitted by me on https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_val=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy_val:
                buy_val=prices[i]
            profit=prices[i]-buy_val
            if profit > max_profit:
                max_profit=profit
        return max_profit