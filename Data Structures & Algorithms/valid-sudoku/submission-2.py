class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Function to check if a list has duplicates (excluding '.')
        def has_duplicates(nums):
            # Filter out '.' and keep only the numbers
            filtered_nums = []
            for num in nums:
                if num != '.':
                    filtered_nums.append(num)

            # Create a set to track seen numbers
            seen = set()
            for num in filtered_nums:
                if num in seen:
                    return True  # Duplicate found
                seen.add(num)
            
            return False  # No duplicates found

        # Check each row for duplicates
        for row in board:
            if has_duplicates(row):
                return False

        # Check each column for duplicates
        for col in range(9):
            # Collect all elements in the current column
            column = [board[row][col] for row in range(9)]
            if has_duplicates(column):
                return False

        # Check each 3x3 sub-box for duplicates
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                # Collect all elements in the current 3x3 sub-box
                box = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        box.append(board[row][col])
                if has_duplicates(box):
                    return False

        # If no duplicates are found in rows, columns, and 3x3 sub-boxes, return True
        return True
