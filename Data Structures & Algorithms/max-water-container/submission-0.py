class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p_left, p_right = 0, len(heights)-1

        ans = 0
        while p_left < p_right:
            p_min = p_left if heights[p_left]<heights[p_right] else p_right
            volume = heights[p_min] * (p_right-p_left)
            ans = max(ans, volume)
            if p_min == p_left:
                p_left += 1
            else:
                p_right -= 1

        return ans
