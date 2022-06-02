#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (42.66%)
# Likes:    3446
# Dislikes: 157
# Total Accepted:    230.5K
# Total Submissions: 519.9K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
# 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# 
# 
# The length of a clear path is the number of visited cells of this path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#

# @lc code=start
from collections import deque
import re


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [-1, 1], [1, -1], [-1, -1]
        ]
        q = deque([(0, 0, 1)])   
        seen = set()
        seen.add((0,0))
        while q:
            i, j ,distance = q.popleft()
            if i == n-1 and j == n-1:
                return distance
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen and grid[x][y] == 0:
                    seen.add((x, y))
                    q.append((x, y, distance+1))
        return -1
        # @lc code=end

