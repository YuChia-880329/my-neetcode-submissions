class Solution:

    _NUM_SEP = '_'
    
    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        # encode
        starts_encode = ''
        strs_encode = ''
        temp_start = 0
        for s in strs:
            strs_encode += s
            starts_encode += str(temp_start) + Solution._NUM_SEP
            temp_start += len(s) # next string start
        return str(n) + Solution._NUM_SEP + starts_encode + strs_encode
        

    def decode(self, s: str) -> List[str]:
        n_str, _, other_str = s.partition(Solution._NUM_SEP)
        n = int(n_str)

        other_str_li = other_str.split(Solution._NUM_SEP, n)
        strs_encode = other_str_li[n]

        ans = [''] * n
        for i in range(n):
            start = int(other_str_li[i])
            end = int(other_str_li[i+1]) if i<n-1 else len(strs_encode)
            ans[i] = strs_encode[start:end]

        return ans
