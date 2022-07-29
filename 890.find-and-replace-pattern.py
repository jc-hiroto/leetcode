#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (75.60%)
# Likes:    2514
# Dislikes: 137
# Total Accepted:    121.8K
# Total Submissions: 158.8K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# Given a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.
#
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
#
# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.
#
#
# Example 1:
#
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation, since a and b map to the same letter.
#
#
# Example 2:
#
#
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pmap = {}
        p = []
        for c in pattern:
            if c not in pmap:
                pmap[c] = len(pmap)
            p.append(pmap[c])
        res = []
        for word in words:
            wmap = {}
            w = []
            for c in word:
                if c not in wmap:
                    wmap[c] = len(wmap)
                w.append(wmap[c])
            if w == p:
                res.append(word)
        return res
# @lc code=end
