#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.38%)
# Likes:    7763
# Dislikes: 860
# Total Accepted:    775.8K
# Total Submissions: 1.8M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start
class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res = []
        r1, r2 = 0, len(m) - 1
        c1, c2 = 0, len(m[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2+1):
                res.append(m[r1][i])
            for i in range(r1 + 1, r2 + 1):
                res.append(m[i][c2])
            if r1 < r2 and c1 < c2:
                for i in range(c2 - 1, c1, -1):
                    res.append(m[r2][i])
                for i in range(r2, r1, -1):
                    res.append(m[i][c1])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res
        # @lc code=end
