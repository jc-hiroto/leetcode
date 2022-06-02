#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (49.69%)
# Likes:    6281
# Dislikes: 101
# Total Accepted:    362.2K
# Total Submissions: 707.2K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                value = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i > 0     and value < matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < m - 1 and value < matrix[i+1][j] else 0,
                    dfs(i, j-1) if j > 0     and value < matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < n - 1 and value < matrix[i][j+1] else 0,
                )
            return dp[i][j]
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(dfs(x, y) for x in range(m) for y in range(n))
# @lc code=end

