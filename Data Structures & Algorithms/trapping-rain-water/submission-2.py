class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        p_left, p_right = 0, len(height)-1

        
        # fast forwarding
        while (p_left<p_right) and (height[p_left]==0):
            p_left += 1
        while (p_left<p_right) and (height[p_right]==0):
            p_right -= 1

        ans = 0
        while p_left < p_right:
            # move the shoter one   
            h_left, h_right = height[p_left], height[p_right]
            if h_left < h_right:
                p = p_left + 1
                volume = 0
                water_taken = 0
                while (p<p_right) and (height[p]<h_left):
                    water_taken += height[p]
                    p += 1
                h_water = h_left if h_left<height[p] else height[p]
                volume = h_water * (p-p_left-1) - water_taken
                # update
                p_left = p
                ans += volume
            else:
                p = p_right - 1
                volume = 0
                water_taken = 0
                while (p>p_left) and (height[p]<h_right):
                    water_taken += height[p]
                    p -= 1
                h_water = h_right if h_right<height[p] else height[p]
                volume = h_water * (p_right-p-1) - water_taken
                # update
                p_right = p
                ans += volume
        return ans 
