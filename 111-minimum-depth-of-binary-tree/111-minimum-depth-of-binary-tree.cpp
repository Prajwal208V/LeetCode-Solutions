/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        //If we have no tree then min depth is o
        if(root == nullptr) {
            return 0;
        }
        //If tree has one node only then min depth is 1
        if(root->left == nullptr and root->right == nullptr) {
            return 1;
        }
        //If tree only has right subtree and no left subtree
        if(root->left == nullptr) {
            return 1 + minDepth(root->right);
        }
        //If tree only has left subtree and no right subtree
        if(root->right == nullptr) {
            return 1 + minDepth(root->left);
        }
        //If tree has both left and right subtree present
        else {
            return 1 + min(minDepth(root->left), minDepth(root->right));
        }
    }
};