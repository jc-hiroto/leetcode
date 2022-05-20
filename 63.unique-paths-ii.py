#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (37.52%)
# Likes:    5154
# Dislikes: 388
# Total Accepted:    543.3K
# Total Submissions: 1.4M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either
# down or right at any point in time.
# 
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
# 
# Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
# 
# The testcases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        m = len(og)
        n = len(og[0])

        if og[0][0] == 1:
            return 0

        og[0][0] = 1

        for i in range(1, m):
            og[i][0] = int(og[i][0] == 0 and og[i-1][0] == 1)

        for j in range(1, n):
            og[0][j] = int(og[0][j] == 0 and og[0][j-1] == 1)

        for i in range(1, m):
            for j in range(1,n):
                if og[i][j] == 0:
                    og[i][j] = og[i - 1][j] + og[i][j - 1]
                else:
                    og[i][j] = 0
        return og[m-1][n-1]

# @lc code=end

