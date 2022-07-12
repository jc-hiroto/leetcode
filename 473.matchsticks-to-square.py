#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (40.32%)
# Likes:    2205
# Dislikes: 164
# Total Accepted:    92.6K
# Total Submissions: 231.5K
# Testcase Example:  '[1,1,2,2,2]'
#
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the i^th matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Constraints:
#
#
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        total /= 4
        matchsticks.sort(reverse=True)

        @lru_cache(None)
        def dfs(e1, e2, e3, e4, index, edge):
            if index == len(matchsticks):
                return e1 == e2 == e3 == e4 == edge
            if e1 > edge or e2 > edge or e3 > edge or e4 > edge:
                return False
            return dfs(e1 + matchsticks[index], e2, e3, e4, index + 1, edge) or \
                dfs(e1, e2 + matchsticks[index], e3, e4, index + 1, edge) or \
                dfs(e1, e2, e3 + matchsticks[index], e4, index + 1, edge) or \
                dfs(e1, e2, e3, e4 + matchsticks[index], index + 1, edge)
        return dfs(0, 0, 0, 0, 0, total)
        # @lc code=end
