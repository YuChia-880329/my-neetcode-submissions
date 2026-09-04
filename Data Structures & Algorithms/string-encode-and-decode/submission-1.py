class Solution:

    _SEP = '#'

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + Solution._SEP + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        while len(s) > 0: # len(s) changes
            length, _, s = s.partition(Solution._SEP)
            length = int(length)
            ans.append(s[:length])
            s = s[length:]
            index += 1
        return ans
