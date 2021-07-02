class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit = 0
    #     min_price = 10**4
    #     for i in range(len(prices) - 1):
    #         if prices[i] < min_price:
    #             min_price = prices[i]
    #         else:
    #             continue
    #         if prices[i + 1] < prices[i]:
    #             continue
    #         for j in range(i + 1, len(prices)):
    #             if prices[j] < prices[i]:
    #                 break
    #             profit = prices[j] - prices[i]
    #             if profit > max_profit:
    #                 max_profit = profit
    #     return max_profit
    
    # O(n)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10**4
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
