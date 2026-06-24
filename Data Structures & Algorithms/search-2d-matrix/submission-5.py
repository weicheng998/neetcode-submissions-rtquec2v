class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        left = 0
        right = n_row * n_col - 1

        while left <= right:
            mid = (left + right) // 2
            # Map middle index back to position in matrix
            row, col = mid // n_col, mid % n_col
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
