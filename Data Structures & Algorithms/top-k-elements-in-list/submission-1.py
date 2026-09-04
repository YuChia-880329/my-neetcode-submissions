from collections import defaultdict, deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # count frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # bucket sort
        buckets = [deque() for _ in range(n)]
        for num, freq in freqs.items():
            buckets[freq-1].append(num)

        # top k
        ans = [0] * k
        ans_index = 0
        for bucket in buckets[::-1]:
            bucket_count = len(bucket)
            while bucket_count > 0:
                ans[ans_index] = bucket.pop()
                ans_index += 1
                bucket_count -= 1
            if ans_index >= k:
                break

        return ans
