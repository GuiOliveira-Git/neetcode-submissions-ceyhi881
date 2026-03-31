class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(nums):
            filtered_nums = []
            for num in nums:
                if num != '.':
                    filtered_nums.append(num)
            return len(filtered_nums) != len(set(filtered_nums))

        # Checking rows
        for row in board:
            if has_duplicates(row):
                return False

        # Checking columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if has_duplicates(column):
                return False

        # Checking 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        box.append(board[row][col])
                if has_duplicates(box):
                    return False
        
        return True
