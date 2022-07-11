/*
 * @lc app=leetcode id=199 lang=cpp
 *
 * [199] Binary Tree Right Side View
 *
 * https://leetcode.com/problems/binary-tree-right-side-view/description/
 *
 * algorithms
 * Medium (59.59%)
 * Likes:    7290
 * Dislikes: 401
 * Total Accepted:    734.2K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,null,5,null,4]'
 *
 * Given the root of a binary tree, imagine yourself standing on the right side
 * of it, return the values of the nodes you can see ordered from top to
 * bottom.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3,null,5,null,4]
 * Output: [1,3,4]
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,null,3]
 * Output: [1,3]
 *
 *
 * Example 3:
 *
 *
 * Input: root = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 100].
 * -100 <= Node.val <= 100
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
   public:
    vector<int> rightSideView(TreeNode* root) {
        vector<vector<int>> level;
        vector<int> res;
        levelTraversal(root, 0, level);
        for (vector<int> v : level) {
            res.push_back(v.back());
        }
        return res;
    }
    void levelTraversal(TreeNode* node, int depth, vector<vector<int>>& level) {
        if (node == nullptr) return;
        if (level.size() == depth) {
            level.push_back({});
        }
        level[depth].push_back(node->val);
        levelTraversal(node->left, depth + 1, level);
        levelTraversal(node->right, depth + 1, level);
    }
};
// @lc code=end
