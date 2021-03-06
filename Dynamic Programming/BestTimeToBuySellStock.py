from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastIndex = len(prices)
        if lastIndex < 2:
            return 0
        minLeft = min(prices[0], prices[1])
        maxScore = prices[1] - prices[0]

        i = 2
        while i < lastIndex:
            newScore =  prices[i] - minLeft
            if newScore > maxScore:
                maxScore = newScore
            newLeft =  prices[i]
            if newLeft < minLeft:
                minLeft =  prices[i]
            i += 1
        return max(maxScore,0)
