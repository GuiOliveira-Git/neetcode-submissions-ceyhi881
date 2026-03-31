class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: nums = [2,20,4,10,3,4,5]
        Output: 4
        [2,2,3,4,5,10,20]
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        max_count = 1
        for i, n in enumerate(nums):
            if i == len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                continue
            if nums[i] == nums[i+1] - 1:
                count+=1
                max_count = max(max_count, count)
                continue
            count=1

        return max_count