from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # heap sort
        def heapsort_k(freqs: dict, k: int) -> List[int]:
            h = []
            h_count = 0
            for num, freq in freqs.items():
                if h_count < k:
                    heapq.heappush(h, (freq, num))
                    h_count += 1
                else:
                    heapq.heappushpop(h, (freq, num))
            # top k        
            ans = [0] * k
            for index in range(k-1, -1, -1):
                freq, num = heapq.heappop(h)
                ans[index] = num
            return ans


        # cases
        dist_count = len(freqs)
        SORT_METHOD_THHESHOLD = 10*2
        if dist_count == 1:
            return [nums[0]]
        elif dist_count <= SORT_METHOD_THHESHOLD:
            return[num for num, _ in sorted(freqs.items(), key=(lambda pair:pair[1]), reverse=True)][:k:]
        else:
            return heapsort_k(freqs, k)
