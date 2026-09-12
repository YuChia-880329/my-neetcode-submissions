class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p_left, p_right = 0, len(heights)-1

        ans = 0
        while p_left < p_right:
            p_min = p_left if heights[p_left]<heights[p_right] else p_right
            h_min = heights[p_min]
            volume = h_min * (p_right-p_left)
            ans = ans if ans>volume else volume
            # update
            if p_min == p_left:
                # fast forwarding
                while (p_left<p_right) and (heights[p_left]<=h_min):
                    p_left += 1
            else:
                # fast forwarding
                while (p_left<p_right) and (heights[p_right]<=h_min):
                    p_right -= 1

        return ans
