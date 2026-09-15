class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1: return n

        window_l, window_r = 0, 0 # both inclusive
        record = {}
        ans = 0
        while window_r < n:
            # check the window
            c = s[window_r]
            last_c_index = record.get(c, -1)
            if last_c_index >= window_l:
                l = window_r - window_l
                if ans < l: ans = l
                # move window_left
                window_l = last_c_index + 1
            record[c] = window_r
            # move window_right
            window_r += 1

        # last update
        l = window_r - window_l
        if ans < l: ans = l

        return ans
