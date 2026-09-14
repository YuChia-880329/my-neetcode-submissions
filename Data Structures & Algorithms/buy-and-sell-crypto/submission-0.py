class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        left_max = 0
        for i in range(len(prices)-1): # i from 0 to n-2
            diff = prices[i+1] - prices[i]
            # update left_max
            left_max += diff
            if left_max < diff : left_max = diff
            # update ans
            if ans < left_max : ans = left_max

        return ans
