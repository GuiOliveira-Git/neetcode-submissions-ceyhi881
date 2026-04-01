class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_count = defaultdict(int)

        for c in s:
            c_count[c] += 1

        for c in t:
            c_count[c] -= 1
            if c_count[c] < 0:
                return False
        
        return True