class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        leftmin = prices[0]
        for price in prices: # update the window right side
            # update the window left side
            if price < leftmin: leftmin = price
            # calculate inside the window
            diff = price - leftmin
            if ans < diff : ans = diff

        return ans