class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        
        h_set_s, h_set_t = {}, {}
        for i in range(len(s)):
            h_set_s[s[i]] = h_set_s.get(s[i], 0) + 1
            h_set_t[t[i]] = h_set_t.get(t[i], 0) + 1

        for c in h_set_s:
            if h_set_s[c] != h_set_t.get(c, 0):
                return False
        
        return True