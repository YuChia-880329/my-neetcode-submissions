class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # egde cases
        if n <= 2:
            return 0
        
        wall_left, wall_right = height[0], height[n-1]
        p_left, p_right = 1, n-2
        ans = 0
        while p_left <= p_right: # the last one should be when they are equal
            # left one move forward
            if wall_left < wall_right:
                # there is water
                if height[p_left] < wall_left:
                    ans += (wall_left-height[p_left])
                # there is no water
                else:
                    wall_left = height[p_left]
                # update
                p_left += 1
            else:
                # there is water
                if height[p_right] < wall_right:
                    ans += (wall_right-height[p_right])
                # there is no water
                else:
                    wall_right = height[p_right]
                # update
                p_right -= 1

        return ans
