#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (61.05%)
# Likes:    1578
# Dislikes: 386
# Total Accepted:    157.7K
# Total Submissions: 251.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array matrix, return the transpose of matrix.
# 
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [[None]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res
# @lc code=end

