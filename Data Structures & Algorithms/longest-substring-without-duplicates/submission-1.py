class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: return n

        window_l, window_r = 0, 0 # left and right inclusive
        record = {}
        ans = 0
        while window_r < n:
            # check the window
            c = s[window_r]
            if (c in record) and (record[c]>=0):
                l = window_r - window_l
                if ans < l: ans = l
                # window left move
                last_c_index = record[c]
                while window_l <= last_c_index:
                    record[s[window_l]] = -1
                    window_l += 1
            record[c] = window_r
            # window right move
            window_r += 1

        # last time update
        l = window_r - window_l
        if ans < l: ans = l

        return ans
