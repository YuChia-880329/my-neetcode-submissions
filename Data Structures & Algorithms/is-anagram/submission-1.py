class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_diff = {}
        for c in s:
            if c not in freq_diff:
                freq_diff[c] = 1
            else:
                freq_diff[c] += 1
        for c in t:
            if c not in freq_diff:
                return False
            else:
                freq_diff[c] -= 1

        for c in freq_diff.keys():
            if freq_diff[c] != 0:
                return False
        
        return True
