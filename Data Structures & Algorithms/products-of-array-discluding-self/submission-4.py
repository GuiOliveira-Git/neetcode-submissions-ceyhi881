class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
        Output: [48,24,12,8]
        """
        output = []
        for i_i, i in enumerate(nums):
            product = 1
            for i_j, j in enumerate(nums):
                if i_i == i_j:
                    continue
                product = product * j
            output.append(product)
        return output