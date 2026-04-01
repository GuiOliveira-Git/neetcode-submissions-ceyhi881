class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [s]
            else:
                anagrams[s_sorted].append(s)
        
        return list(anagrams.values())