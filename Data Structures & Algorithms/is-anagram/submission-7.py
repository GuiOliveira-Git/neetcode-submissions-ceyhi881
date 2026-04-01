class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        chars_count = {}

        for c in s:
            if c not in chars_count:
                chars_count[c] = 1
                continue
            chars_count[c] += 1

        for c in t:
            if c not in chars_count:
                return False
            if chars_count[c] == 0:
                return False
            chars_count[c] -= 1
        
        return True