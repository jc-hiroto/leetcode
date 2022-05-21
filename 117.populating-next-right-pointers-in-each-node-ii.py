#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (46.59%)
# Likes:    4364
# Dislikes: 253
# Total Accepted:    472.4K
# Total Submissions: 979.1K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow-up:
# 
# 
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tree_lv_order = self.levelOrder(root)
        print(tree_lv_order)
        for level in tree_lv_order:
            for i in range(len(level)):
                node = level[i]
                if i == len(level) - 1:
                    continue
                else:
                    node.next = level[i+1]

    def levelOrder(self, node):
        res = []
        if node is None:
            return res
        q = collections.deque()
        q.append(node)
        print(node)
        print(q)
        while q:
            curSize = len(q)
            level = []
            while curSize > 0:
                curNode = q.popleft()
                level.append(curNode)
                curSize -= 1
                if curNode.left is not None:
                    q.append(curNode.left)
                if curNode.right is not None:
                    q.append(curNode.right)
            res.append(level)
# @lc code=end

