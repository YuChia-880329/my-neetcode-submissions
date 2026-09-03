from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        INDEX_OFFSET = ord('a')
        for index, s in enumerate(strs):
            freq = [0]*26
            for c in s:
                freq[ord(c)-INDEX_OFFSET] += 1
            bucket[tuple(freq)].append(s)

        return list(bucket.values())
