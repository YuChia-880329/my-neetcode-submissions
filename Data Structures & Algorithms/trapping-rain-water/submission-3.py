class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        p_left, p_right = 0, len(height)-1
        # fast forwarding
        while (p_left<p_right) and (height[p_left]==0):
            p_left += 1
        while (p_left<p_right) and (height[p_right]==0):
            p_right -= 1

        ans = 0
        while p_left < p_right:
            h_left, h_right = height[p_left], height[p_right]
            # move from the shorter one
            if h_left < h_right:
                p = p_left + 1
                water_taken = 0
                while (p<p_right) and (height[p]<h_left):
                    water_taken += height[p]
                    p += 1
                volume = h_left * (p-p_left-1) - water_taken
                # update
                p_left = p
                ans += volume
            else:
                p = p_right - 1
                water_taken = 0
                while (p>p_left) and (height[p]<h_right):
                    water_taken += height[p]
                    p -= 1
                volume = h_right * (p_right-p-1) - water_taken
                # update
                p_right = p
                ans += volume
        return ans
