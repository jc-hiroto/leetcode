/*
 * @lc app=leetcode id=86 lang=cpp
 *
 * [86] Partition List
 *
 * https://leetcode.com/problems/partition-list/description/
 *
 * algorithms
 * Medium (47.86%)
 * Likes:    4020
 * Dislikes: 533
 * Total Accepted:    369.4K
 * Total Submissions: 749.4K
 * Testcase Example:  '[1,4,3,2,5,2]\n3'
 *
 * Given the head of a linked list and a value x, partition it such that all
 * nodes less than x come before nodes greater than or equal to x.
 *
 * You should preserve the original relative order of the nodes in each of the
 * two partitions.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [1,4,3,2,5,2], x = 3
 * Output: [1,2,2,4,3,5]
 *
 *
 * Example 2:
 *
 *
 * Input: head = [2,1], x = 2
 * Output: [1,2]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the list is in the range [0, 200].
 * -100 <= Node.val <= 100
 * -200 <= x <= 200
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
   public:
    ListNode* partition(ListNode* head, int x) {
        ListNode node1(0), node2(0);
        ListNode *cur1 = &node1, *cur2 = &node2;
        while (head) {
            if (head->val < x) {
                cur1->next = head;
                cur1 = cur1->next;
            } else {
                cur2->next = head;
                cur2 = cur2->next;
            }
            head = head->next;
        }
        cur1->next = node2.next;
        cur2->next = nullptr;
        return node1.next;
    }
};
// @lc code=end
