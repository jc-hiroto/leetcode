#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (64.45%)
# Likes:    6845
# Dislikes: 226
# Total Accepted:    899.5K
# Total Submissions: 1.3M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
#
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
#
# Constraints:
#
#
# 1 <= numRows <= 30
#
#
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows <= 2:
            return res[:numRows]
        for i in range(2, numRows):
            res.append([1] + [res[i - 1][j] + res[i - 1][j + 1]
                       for j in range(i - 1)] + [1])
        return res

# @lc code=end
