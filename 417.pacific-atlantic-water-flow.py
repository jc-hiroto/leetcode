#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (49.16%)
# Likes:    4114
# Dislikes: 906
# Total Accepted:    226.1K
# Total Submissions: 447.4K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        p_visited = set()
        a_visited = set()
        res = []
        for i in range(m):
            self.dfs(i, 0, heights, p_visited, m, n)
            self.dfs(i, n - 1, heights, a_visited, m, n)

        for j in range(n):
            self.dfs(0, j, heights, p_visited, m, n)
            self.dfs(m - 1, j, heights, a_visited, m, n)

        return list(p_visited & a_visited)

    def dfs(self, i, j, heights, visited, m, n):
        visited.add((i, j))
        for d in self.directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j] and (x, y) not in visited:
                self.dfs(x, y, heights, visited, m, n)
        # @lc code=end
