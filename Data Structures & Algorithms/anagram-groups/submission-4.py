class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            seen[s_sorted].append(s)
        return list(seen.values())