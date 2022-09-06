class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPriceIndex = -1
        for i, price in enumerate(prices):
            if minPriceIndex == -1:
                minPriceIndex = 0
                continue

            if maxProfit < price - prices[minPriceIndex]:
                maxProfit = price - prices[minPriceIndex]
            if prices[minPriceIndex] > price:
                minPriceIndex = i

        return maxProfit
