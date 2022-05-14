#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (58.75%)
# Likes:    3684
# Dislikes: 1292
# Total Accepted:    321.7K
# Total Submissions: 530.3K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
# 
# Implement the NestedIterator class:
# 
# 
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
# the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested
# list and false otherwise.
# 
# 
# Your code will be tested with the following pseudocode:
# 
# 
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
# ⁠   append iterator.next() to the end of res
# return res
# 
# 
# If res matches the expected flattened list, then your code will be judged as
# correct.
# 
# 
# Example 1:
# 
# 
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,4,6].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.fled = []
        def flatten(ls):
            for item in ls:
                if not item.isInteger():
                    flatten(item.getList())
                else:
                    self.fled.append(item.getInteger())
                    
        flatten(nestedList)
                
            
    
    def next(self) -> int:
        return self.fled.pop(0)
        
    
    def hasNext(self) -> bool:
        return bool(len(self.fled))
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

