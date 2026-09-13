class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # edge cases
        if n <= 2:
            return 0

        # left max
        max_ = height[0]
        left_max = [max_]*n # for index readability
        for i in range(1, n-1): # i from 1 to n-2
            left_max[i] = max_
            if max_ < height[i]: max_ = height[i]

        # right max
        max_ = height[n-1]
        right_max = [max_]*n # for index readability
        for i in range(n-2, 0, -1): # i from n-2 to 1
            right_max[i] = max_
            if max_ < height[i]: max_ = height[i]

        # calculate
        ans = 0
        for i in range(1, n-1): # i from 1 to n-2
            h = left_max[i] if left_max[i]<right_max[i] else right_max[i]
            if h > height[i]:
                ans += (h-height[i])

        return ans
