class Solution:

    _SEP = '#'

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        ans_li = [''] * n
        for i in range(n):
            s = strs[i]
            ans_li[i] = f'{len(s)}{Solution._SEP}{s}'

        return ''.join(ans_li)

    def decode(self, s: str) -> List[str]:
        ans = []
        p_start = 0
        while p_start < len(s):
            # length
            p_end = s.find(Solution._SEP, p_start)
            length = int(s[p_start:p_end])
            # string
            p_start = p_end + 1
            p_end = p_start + length
            ans.append(s[p_start: p_end])
            p_start = p_end
        return ans
