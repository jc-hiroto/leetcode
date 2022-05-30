#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (56.65%)
# Likes:    1864
# Dislikes: 96
# Total Accepted:    148.1K
# Total Submissions: 259.1K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.
# 
# 
# Example 1:
# 
# 
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# 
# 
# Example 2:
# 
# 
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# 
# 
# Example 3:
# 
# 
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict
from itertools import combinations


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = defaultdict(int)
        res = 0
        for word in words:
            for ch in set(word):
                d[word] |= 1 << (ord(ch) - ord('a'))

        for wd1, wd2 in combinations(d.keys(), 2):
            if d[wd1] & d[wd2] == 0:
                res = max(len(wd1) * len(wd2), res)

        return res
# @lc code=end

