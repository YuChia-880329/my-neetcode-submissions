from itertools import chain

class Solution:

    _SEP = '#'

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        pos_li = [''] * n
        p_end_pos = 0
        meta_len = 0
        for i, s in enumerate(strs):
            p_end_pos += len(s)
            pos_li[i] = f'{p_end_pos}{Solution._SEP}'
            # update
            meta_len += len(pos_li[i])

        return ''.join(chain([f'{n}{Solution._SEP}', f'{meta_len}{Solution._SEP}'], pos_li, strs))

    def decode(self, s: str) -> List[str]:
        # n
        p_end = s.find(Solution._SEP)
        n = int(s[:p_end])
        # meta_len
        p_start = p_end + 1
        p_end = s.find(Solution._SEP, p_start)
        meta_len = int(s[p_start:p_end])
        # strings
        ans = [''] * n
        p_meta_from = p_end + 1
        p_data_from = p_meta_from + meta_len
        p_from = p_data_from
        for i in range(n):
            # meta: end_pos
            p_meta_end = s.find(Solution._SEP, p_meta_from)
            end_pos = int(s[p_meta_from:p_meta_end])
            p_end = p_data_from + end_pos
            # string
            ans[i] = s[p_from:p_end]
            # update
            p_meta_from = p_meta_end + 1 # here's separator
            p_from = p_end               # here's no separator

        return ans
