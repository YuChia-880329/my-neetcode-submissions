class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p_left, p_right = 0, len(heights)-1

        ans = 0
        while p_left < p_right:
            h_left, h_right = heights[p_left], heights[p_right]

            if h_left < h_right:
                volume = h_left * (p_right-p_left)
                if ans < volume: ans = volume
                # fast forwarding
                while (p_left<p_right) and (heights[p_left]<=h_left):
                    p_left += 1
            else:
                volume = h_right * (p_right-p_left)
                if ans < volume: ans = volume
                # fast forwarding
                while (p_left<p_right) and (heights[p_right]<=h_right):
                    p_right -= 1

        return ans
