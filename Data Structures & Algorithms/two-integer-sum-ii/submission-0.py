class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers=[1,2,3,4]
        target=3
        """
        num_to_pos = {}
        for i, n in enumerate(numbers):
            num_to_pos[n] = i+1
        """
        1 to 1
        2 to 2
        3 to 3
        4 to 4
        """
        for number, position in num_to_pos.items():
            comp = target - number
            if comp in num_to_pos:
                return [position, num_to_pos[comp]]

        return []