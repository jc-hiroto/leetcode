/*
 * @lc app=leetcode id=208 lang=cpp
 *
 * [208] Implement Trie (Prefix Tree)
 *
 * https://leetcode.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (58.11%)
 * Likes:    7639
 * Dislikes: 93
 * Total Accepted:    627.6K
 * Total Submissions: 1.1M
 * Testcase Example:
 '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * A trie (pronounced as "try") or prefix tree is a tree data structure used to
 * efficiently store and retrieve keys in a dataset of strings. There are
 * various applications of this data structure, such as autocomplete and
 * spellchecker.
 *
 * Implement the Trie class:
 *
 *
 * Trie() Initializes the trie object.
 * void insert(String word) Inserts the string word into the trie.
 * boolean search(String word) Returns true if the string word is in the trie
 * (i.e., was inserted before), and false otherwise.
 * boolean startsWith(String prefix) Returns true if there is a previously
 * inserted string word that has the prefix prefix, and false otherwise.
 *
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
 * [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
 * Output
 * [null, null, true, false, true, null, true]
 *
 * Explanation
 * Trie trie = new Trie();
 * trie.insert("apple");
 * trie.search("apple");   // return True
 * trie.search("app");     // return False
 * trie.startsWith("app"); // return True
 * trie.insert("app");
 * trie.search("app");     // return True
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= word.length, prefix.length <= 2000
 * word and prefix consist only of lowercase English letters.
 * At most 3 * 10^4 calls in total will be made to insert, search, and
 * startsWith.
 *
 *
 */

// @lc code=start
struct TrieNode {
    bool end;
    TrieNode* children[26];
    TrieNode() {
        end = false;
        memset(children, NULL, sizeof(children));
    }
};

class Trie {
   private:
    TrieNode* root;

   public:
    /** Initialize your data structure here. */
    Trie() { root = new TrieNode(); }
    ~Trie() { clear(root); }
    void clear(TrieNode* root) {
        for (int i = 0; i < 26; i++) {
            if (root->children[i]) clear(root->children[i]);
        }
        delete root;
    }
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* dummy = root;
        for (char c : word) {
            if (!dummy->children[c - 'a'])
                dummy->children[c - 'a'] = new TrieNode();
            dummy = dummy->children[c - 'a'];
        }
        dummy->end = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* dummy = root;
        for (char c : word) {
            if (!dummy->children[c - 'a']) return false;
            dummy = dummy->children[c - 'a'];
        }
        return dummy && dummy->end;
    }

    /** Returns if there is any word in the trie that starts with the given
     * prefix. */
    bool startsWith(string word) {
        TrieNode* dummy = root;
        for (char c : word) {
            if (!dummy->children[c - 'a']) return false;
            dummy = dummy->children[c - 'a'];
        }
        return dummy;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end
