class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        INDEX_OFFSET = ord('a')
        LIST_SIZE = 26
        freq_diff = [0]*LIST_SIZE
        for c1, c2 in zip(s, t):
            freq_diff[ord(c1)-INDEX_OFFSET] += 1
            freq_diff[ord(c2)-INDEX_OFFSET] -= 1

        for i in range(0, LIST_SIZE):
            if freq_diff[i] != 0:
                return False

        return True 
