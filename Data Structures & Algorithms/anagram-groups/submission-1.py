from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freqs = [Counter(str_) for str_ in strs]
        bucket = {}
        for index, freq in enumerate(freqs):
            freq_key = frozenset(freq.items())
            if freq_key not in bucket:
                bucket[freq_key] = []
            bucket[freq_key].append(strs[index])

        return list(bucket.values())
