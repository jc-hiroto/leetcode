#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (38.59%)
# Likes:    19073
# Dislikes: 3849
# Total Accepted:    2.8M
# Total Submissions: 7.3M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = tail = None
        while l1 and l2:
            node = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10 
            if not root: root = node
            if tail: tail.next = node
            tail = node
            l1, l2 = l1.next, l2.next
        while l1:
            sum_val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            tail.next = tail = ListNode(sum_val)
            l1 = l1.next
        while l2:
            sum_val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            tail.next = tail = ListNode(sum_val)
            l2 = l2.next

        tail.next = ListNode(carry) if carry else None
        
        return root

        
        
# @lc code=end

