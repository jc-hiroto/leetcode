#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (47.69%)
# Likes:    3252
# Dislikes: 277
# Total Accepted:    254.7K
# Total Submissions: 512.9K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, handle multiple queries of the following
# type:
# 
# 
# Calculate the sum of the elements of matrix inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).
# 
# 
# Implement the NumMatrix class:
# 
# 
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix
# matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the
# elements of matrix inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
# 
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green
# rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue
# rectangle)
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^5 <= matrix[i][j] <= 10^5
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10^4 calls will be made to sumRegion.
# 
# 
#

# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
      n = len(matrix) + 1
      m = len(matrix[0]) + 1
      self.dp = [[0] * m for _ in range(n)]
      for i in range(1, n):
        for j in range(1, m):
          self.dp[i][j] = matrix[i-1][j-1] + self.dp[i][j-1] + self.dp[i-1][j] - self.dp[i-1][j-1]      

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
      return self.dp[r2+1][c2+1] - self.dp[r2+1][c1] - self.dp[r1][c2+1] + self.dp[r1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

