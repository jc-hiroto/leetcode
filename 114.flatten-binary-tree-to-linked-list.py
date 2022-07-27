#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (57.78%)
# Likes:    8165
# Dislikes: 480
# Total Accepted:    656.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
#
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return

        # def preorder(node):
        #     if not node:
        #         return
        #     self.ptr.right = TreeNode(node.val)
        #     self.ptr.left = None
        #     self.ptr = self.ptr.right
        #     preorder(node.left)
        #     preorder(node.right)

        # dummy = TreeNode(0)
        # self.ptr = dummy
        # preorder(root)
        # root.right = dummy.right.right if dummy.right else None
        # root.left = None

        def revPreOrder(node):
            if node.right:
                revPreOrder(node.right)
            if node.left:
                revPreOrder(node.left)
            node.left, node.right = None, self.head
            self.head = node

        if root:
            revPreOrder(root)


# @lc code=end
