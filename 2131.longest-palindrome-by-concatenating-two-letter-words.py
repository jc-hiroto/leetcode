#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
#
# algorithms
# Medium (38.40%)
# Likes:    501
# Dislikes: 13
# Total Accepted:    17.4K
# Total Submissions: 43.9K
# Testcase Example:  '["lc","cl","gg"]'
#
# You are given an array of strings words. Each element of words consists of
# two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words
# and concatenating them in any order. Each element can be selected at most
# once.
#
# Return the length of the longest palindrome that you can create. If it is
# impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.
#
#
# Example 1:
#
#
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of
# length 6.
# Note that "clgglc" is another longest palindrome that can be created.
#
#
# Example 2:
#
#
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" =
# "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
#
#
# Example 3:
#
#
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is
# "xx".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^5
# words[i].length == 2
# words[i] consists of lowercase English letters.
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        mapping = defaultdict(int)
        for word in words:
            p = f"{word[1]}{word[0]}"
            if mapping[p] > 0:
                res += 4
                mapping[p] -= 1
            else:
                mapping[word] += 1
        for word in mapping:
            if word[0] == word[1] and mapping[word] > 0:
                res += 2
                break
        return res

# @lc code=end
