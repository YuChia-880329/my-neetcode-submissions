from itertools import chain

class Solution:

    _SEP = '#'

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        len_li = [''] * n
        for i, s in enumerate(strs):
            len_li[i] = f'{len(s)}{Solution._SEP}'
        return ''.join(chain.from_iterable(zip(len_li, strs)))

    def decode(self, s: str) -> List[str]:
        ans = []
        p_from = 0
        while p_from < len(s):
            # length
            p_end = s.find(Solution._SEP, p_from)
            length = int(s[p_from:p_end])
            # string
            p_from = p_end + 1  # here's seperator
            p_end = p_from + length
            ans.append(s[p_from:p_end])
            # update
            p_from = p_end      # here's no seperator

        return ans
