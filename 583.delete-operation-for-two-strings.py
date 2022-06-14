#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (55.80%)
# Likes:    3712
# Dislikes: 58
# Total Accepted:    148.7K
# Total Submissions: 257.8K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
# 
# In one step, you can delete exactly one character in either string.
# 
# 
# Example 1:
# 
# 
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# 
# Example 2:
# 
# 
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[1000] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

