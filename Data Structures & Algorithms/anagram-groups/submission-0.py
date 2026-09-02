class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = len(strs)
        freqs = [[0]*26 for _ in range(m)]

        INDEX_OFFSET = ord('a')
        for index, str_ in enumerate(strs):
            for c in str_:
                freqs[index][ord(c)-INDEX_OFFSET] += 1

        bucket = {}
        for index, freq in enumerate(freqs):
            freq_t = tuple(freq)
            if freq_t not in bucket:
                bucket[tuple(freq)] = []
            bucket[tuple(freq)].append(strs[index])

        return list(bucket.values())
