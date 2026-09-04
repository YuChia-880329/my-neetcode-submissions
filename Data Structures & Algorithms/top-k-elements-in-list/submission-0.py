from collections import defaultdict, deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # count the frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # bucket sort
        buckets = [[] for _ in range(n)]
        bucket_count = [0] * n
        for num, freq in freqs.items():
            buckets[freq-1].append(num)
            bucket_count[freq-1] += 1

        # top k
        i = k
        ans = deque()
        for index in range(n-1, -1, -1):
            if bucket_count[index] > 0:
                i -= bucket_count[index]
                ans.extend(buckets[index])
            if i <= 0:
                break

        return list(ans)
