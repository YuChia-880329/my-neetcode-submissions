class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # egde cases
        if n < 2:
            return 0

        # left max
        max_ = height[0]
        left_max = [max_]*n
        for i in range(1, n-1): # i from 1 to n-2
            left_max[i] = max_
            # update
            h_i = height[i] # pre-allocate the array slot
            if max_ < h_i: max_ = h_i
        # right max
        max_ = height[n-1]
        right_max = [max_]*n
        for i in range(n-2, 0, -1): # i from n-2 to 1
            right_max[i] = max_
            # update
            h_i = height[i] # pre-allocate the array slot
            if max_ < h_i: max_ = h_i
             
        # calculate
        ans = 0
        for i in range(1, n-1): # i from 1 to n-2
            max_l, max_r, h_i = left_max[i], right_max[i], height[i] # pre-allocate the array slots
            h = max_l if max_l<max_r else max_r
            if h_i < h:
                ans += (h-h_i)

        return ans
