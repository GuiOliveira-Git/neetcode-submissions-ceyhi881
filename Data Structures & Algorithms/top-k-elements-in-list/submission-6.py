class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        return [n for n, _ in seen.most_common(k)]