class Solution:

    _SEP = '#'
    def encode(self, strs: List[str]) -> str:
        ans_li = [''] * 3 * len(strs)
        
        for i in range(len(strs)):
            index = 3*i
            s = strs[i]
            ans_li[index] = str(len(s))
            ans_li[index+1] = Solution._SEP
            ans_li[index+2] = s
        return "".join(ans_li)

    def decode(self, s: str) -> List[str]:
        p_start = 0
        p_end = 0
        ans = []
        while p_start < len(s):
            # length
            while s[p_end] != Solution._SEP:
                p_end += 1
            length = int(s[p_start: p_end])
            # string
            p_start = p_end + 1
            p_end = p_start + length
            ans.append(s[p_start:p_end])
            p_start = p_end
        return ans
