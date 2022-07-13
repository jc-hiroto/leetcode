#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (44.36%)
# Likes:    8442
# Dislikes: 286
# Total Accepted:    872.7K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc code=start
from bisect import bisect_left, bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first_col = [row[0] for row in matrix]
        # last_col = [row[-1] for row in matrix]
        # if target in first_col or target in last_col:
        #     return True
        # first = bisect_left(first_col, target) - 1
        # last = bisect_left(last_col, target)
        # print(first, last)
        # if first != last:
        #     return False
        # row = matrix[first]
        # return target in row

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# @lc code=end
