class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s, counter_t = {}, {}
        for i, j in zip(s, t):
            if i in counter_s:
                counter_s[i] += 1
            else:
                counter_s[i] = 1
            if j in counter_t:
                counter_t[j] += 1
            else:
                counter_t[j] = 1

        keys_s, keys_t = counter_s.keys(), counter_t.keys()
        if len(keys_s) != len(keys_t):
            return False
        for key in keys_s:
            if key not in keys_t:
                return False
            elif counter_s[key] != counter_t[key]:
                return False
            
        return True


