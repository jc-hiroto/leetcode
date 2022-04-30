#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val
    def inorder(self, node: TreeNode) -> None:
        if not node:
            return
        self.inorder(node.left)
        if self.prev and self.prev.val > node.val:
            if not self.node1:
                self.node1 = self.prev
            if self.node1:
                self.node2 = node
        self.prev = node
        self.inorder(node.right)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Use in-order traversal to check if the tree is valid
        # If not, swap the values of the two nodes
        self.prev = None
        self.node1 = None
        self.node2 = None
        self.inorder(root)
        self.swap(self.node1, self.node2)

        
        
# @lc code=end

