#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Medium (34.75%)
# Likes:    4477
# Dislikes: 247
# Total Accepted:    288K
# Total Submissions: 810.3K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1:
                return True
            return (i >= 0 and s1[i] == s3[i+j+1] and dp(i-1, j)) or (j >= 0 and s2[j] == s3[i+j+1] and dp(i, j-1))
        return len(s1) + len(s2) == len(s3) and dp(len(s1) - 1, len(s2) - 1)
# @lc code=end
