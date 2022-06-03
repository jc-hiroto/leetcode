#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (38.92%)
# Likes:    4094
# Dislikes: 95
# Total Accepted:    165.1K
# Total Submissions: 424.6K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
# 
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
# 
# Note: You cannot rotate an envelope.
# 
# 
# Example 1:
# 
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# Example 2:
# 
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
# 
# 
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, Es: List[List[int]]) -> int:
        # sort width then height reverse
        # sort reverse height is to deal with boxes with same width, prevent from selecting multiple boxes with same width
        # [2, 3], [5, 4], [6, 7], [6, 5], [6, 4], [7, 6] -> Heights = [3, 4, 7] -> [3, 4, 5] -> [3, 4, 5] -> [3, 4, 5, 6]
        Es.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for w, h in Es:
            left = bisect_left(dp, h)  # use binary search to find the insert position
            if left == len(dp):
                # if height is larger than any number in dp, insert to the end of list
                dp.append(h) 
            else:
                # else overwrite the original number 
                # (When happened at the end of the list, this can overwrite it to a smaller following number)
                dp[left] = h
        
        return len(dp)
        
# @lc code=end

