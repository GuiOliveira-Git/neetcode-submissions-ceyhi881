class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in aux:
                return [aux[complement], i]
            aux[n] = i
        return []