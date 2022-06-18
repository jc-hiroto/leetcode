#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (36.51%)
# Likes:    1589
# Dislikes: 397
# Total Accepted:    66.5K
# Total Submissions: 170.9K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Design a special dictionary with some words that searchs the words in it by a
# prefix and a suffix.
# 
# Implement the WordFilter class:
# 
# 
# WordFilter(string[] words) Initializes the object with the words in the
# dictionary.
# f(string prefix, string suffix) Returns the index of the word in the
# dictionary, which has the prefix prefix and the suffix suffix. If there is
# more than one valid index, return the largest of them. If there is no such
# word in the dictionary, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# 
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
# "a" and suffix = 'e".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.
# 
# 
#

# @lc code=start
from collections import defaultdict


Trie = lambda: defaultdict(Trie)

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                node = self.trie
                node["weight"] = weight
                word_for_insert = word[i:]+"#"+word
                for c in word_for_insert:
                    node = node[c]
                    node["weight"] = weight

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for c in suffix+"#"+prefix:
            if c not in node:
                return -1
            node = node[c]
        return node["weight"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end

