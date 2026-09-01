class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_diff = {chr(c_ord):0 for c_ord in range(ord('a'), ord('z')+1)}
        for c1, c2 in zip(s,t):
            freq_diff[c1] += 1
            freq_diff[c2] -= 1

        for c in freq_diff.keys():
            if freq_diff[c] != 0:
                return False

        return True