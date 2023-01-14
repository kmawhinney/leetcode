class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l <= r:
            mid = (r + l) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
      
# Explanation
"""
Treat at normal binary search, with the added step of finding where mid is in the matrix.

To find the row it is in, you do: mid // cols (e.g. 5 // 4 = 1, so 5 is in the row with index 1)
To find the col it is in, you do: mid % cols (e.g. 5 % 4 = 1, so 5 is in the col with index 1)

Using the above examples, that would mean 5 is at matrix[1][1]
"""
