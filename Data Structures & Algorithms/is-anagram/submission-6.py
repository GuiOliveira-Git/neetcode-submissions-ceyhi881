class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chars = {}
        for c in s:
            if c not in chars:
                chars[c] = 1
                continue
            chars[c] = chars[c] + 1
        
        print(chars)
        for c in t:
            if c not in chars:
                return False
            chars[c] = chars[c] - 1
            
        for c in chars.values():
            if c != 0:
                return False

        return True

        