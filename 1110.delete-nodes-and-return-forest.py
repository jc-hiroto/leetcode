#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (69.28%)
# Likes:    2880
# Dislikes: 87
# Total Accepted:    161.3K
# Total Submissions: 232.7K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# 
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest. You may return the
# result in any order.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        del_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in del_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root

        helper(root, True)
        return res
        
# @lc code=end

